pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t local-flask-app:latest .'
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker stop flask_app_container || true'
                    sh 'docker rm flask_app_container || true'
                    sh 'docker run -d --name app_container -p 3000:3000 local-flask-app:latest'
                }
            }
        }

        stage('Test Health Endpoint') {
            steps {
                sleep 5
                sh 'curl -f http://localhost:3000/health'
            }
        }
    }

    post {
        success {
            echo 'Build, deploy, and health check succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
