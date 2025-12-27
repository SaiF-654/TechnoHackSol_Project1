pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'python --version'
                sh 'pip install --user -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
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
                sh 'docker build -t my-python-app:latest .'
            }
        }
    }
    
    post {
        success {
            echo '✅ Pipeline SUCCESS! All tests passed and Docker image built.'
            sh 'echo "Build Number: ${BUILD_NUMBER}"'
        }
        failure {
            echo '❌ Pipeline FAILED! Check the logs above.'
        }
    }
}
