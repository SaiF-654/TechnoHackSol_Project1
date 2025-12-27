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
                // Run pytest - dependencies are already installed in the Docker image
                // Use '.' to run all tests in current directory
                sh 'python -m pytest . --junitxml=test-results.xml'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
        
        stage('Cleanup') {
            steps {
                script {
                    // Clean up Docker images to save space
                    sh 'docker image prune -f || true'
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
