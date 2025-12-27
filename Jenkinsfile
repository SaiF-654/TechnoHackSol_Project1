pipeline {
    agent {
    docker {
        image 'python:3.14.2-alpine3.23'
        reuseNode true
        args '--user root'  // ← THIS SOLVES THE PERMISSION ERROR
    }
}
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install & Test') {
            agent {
                docker {
                    image 'python:3.14.2-alpine3.23'
                    reuseNode true
                    args '--user root'  // ← CRITICAL FIX: Run as root
                }
            }
            steps {
                // Install dependencies as root (no permission issues)
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
                    docker.build("my-python-app:${env.BUILD_ID}")
                }
            }
        }
    }
    
    post {
        success {
            echo '✅ Pipeline SUCCESS! All tests passed and Docker image built.'
        }
        failure {
            echo '❌ Pipeline FAILED! Check the logs above.'
        }
    }
}
