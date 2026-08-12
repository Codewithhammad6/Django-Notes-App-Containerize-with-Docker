@Library("shared") _
pipeline {
    agent {
        label "hammi"
    }

    stages {

        stage('Clone Repository') {
            steps {
                clone(
                    "https://github.com/Codewithhammad6/Django-Notes-App-Containerize-with-Docker",
                    "main"
                )
            }
        }

        stage('Build Images') {
            steps {
                dockerbuild()
            }
        }

        stage('Tag Images') {
            steps {
                dockerTag(
                    'hammadch123',
                    [
                        'smc-frontend': 'notes-frontend-jenkins',
                        'smc-django_app1': 'notes-backend-jenkins',
                        'smc-nginx': 'notes-nginx-jenkins'
                    ]
                )
            }
        }

        stage('Push Images') {
            steps {
                dockerPush(
                    'hammadch123',
                    'dockerhubcred',
                    [
                        'notes-frontend-jenkins',
                        'notes-backend-jenkins',
                        'notes-nginx-jenkins'
                    ]
                )
            }
        }

        stage('Run Application') {
            steps {
                echo 'Starting application using Docker Compose'
                sh 'docker compose up -d'
            }
        }
    }
}
