pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'my-python-app'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm // Checks out the code from your repository
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }
        stage('Test') {
            agent {
                docker { image 'python:3.14.2-alpine3.23' }
            }
            steps {
                sh 'python -m pytest --junitxml=test-results.xml || true'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
    }
}
