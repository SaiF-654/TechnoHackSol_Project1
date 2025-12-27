pipeline {
    agent any

    environment {
        IMAGE_NAME = 'saifrehman123/django-jenkins'
        DOCKER_CREDENTIALS_ID = 'dockerhub-cred'
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
                    // Stop old containers
                    sh "docker rm -f dev staging 2>/dev/null || true"

                    // Run new containers with health check
                    sh """
                        docker run -d \\
                          -p 8001:8000 \\
                          --name dev \\
                          --health-cmd="curl -f http://localhost:8000/ || exit 1" \\
                          --health-interval=30s \\
                          ${env.IMAGE_TAG}

                        docker run -d \\
                          -p 8002:8000 \\
                          --name staging \\
                          --health-cmd="curl -f http://localhost:8000/ || exit 1" \\
                          --health-interval=30s \\
                          ${env.IMAGE_TAG}
                    """
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
