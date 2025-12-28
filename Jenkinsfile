pipeline {
    agent any

    environment {
        IMAGE_NAME = 'saifrehman123/django-jenkins'
        DOCKER_CREDENTIALS_ID = 'dockerhub-cred'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/SaiF-654/TechnoHackSol_Project1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    env.IMAGE_TAG = "${IMAGE_NAME}:${env.BUILD_NUMBER}"
                    sh "docker build -t ${env.IMAGE_TAG} ."
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: "${DOCKER_CREDENTIALS_ID}",
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                sh "docker push ${env.IMAGE_TAG}"
            }
        }

        stage('Deploy Dev and Staging') {
            steps {
                script {
                    // Stop/remove old containers if exist
                    sh "docker rm -f dev || true"
                    sh "docker rm -f staging || true"

                    // Run new containers
                    sh "docker run -d -p 8001:8000 --name dev ${env.IMAGE_TAG}"
                    sh "docker run -d -p 8002:8000 --name staging ${env.IMAGE_TAG}"
                }
            }
        }
    }

    post {
        success {
            echo "✅ Dev running on port 8001 | Staging running on port 8002"
        }
        failure {
            echo '❌ Deployment failed'
        }
    }
}

