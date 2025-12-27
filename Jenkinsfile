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
        
        stage('Build & Test') {
            agent {
                docker {
                    image 'python:3.14.2-alpine3.23'
                    reuseNode true
                }
            }
            steps {
                // Install dependencies
                sh 'pip install --no-cache-dir -r requirements.txt'
                
                // Run tests
                sh 'python -m pytest . --junitxml=test-results.xml'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed - check test results above'
        }
        success {
            echo '✅ Pipeline SUCCESS! All tests passed.'
        }
        failure {
            echo '❌ Pipeline FAILED! Check the logs above.'
        }
    }
}
