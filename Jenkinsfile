pipeline {
    agent {label 'First'}

    stages {
        stage('Clone') {
            steps {
                git url:'https://github.com/IradIcaTE/Random_Quote_api.git', branch: 'main'
            }
        }

        stage('Build Image'){
            steps {
                script {
                    sh 'docker build -t random-queue-api ./app'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 --name quote_container random-quote-api'
                }
            }
        }
    }
}