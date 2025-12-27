pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'my-python-app'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
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
                docker {
                    image 'python:3.14.2-alpine3.23'
                    reuseNode true
                }
            }
            steps {
                sh 'pip install -r requirements.txt'  # Ensure pytest is installed
                sh 'python -m pytest --junitxml=test-results.xml'  # Remove "|| true"
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
    }
}
