pipeline{
    agent any
    stages{


        stage('Clean up previous containers') {
            steps {
                sh 'docker compose down --remove-orphans || true'
            }
        }


        stage('Ejecutar pruebas'){
            parallel{
                
                stage('Cypress'){
                    steps{
                        sh 'docker compose up cypress-tests'
                    }
                }

                stage('Apis'){
                    steps{
                        sh 'docker compose up api-tests'
                    }
                }

                stage('Jmeter'){
                    steps{
                        sh 'docker compose up jmeter-tests'
                    }
                }

                stage ('Zap'){
                    steps{
                        sh 'docker compose up zap-tests'
                    }
                }

            }
        }

    }

    post{
        always {
            sh 'docker compose down --remove-orphans || true'
    }
    success {
        echo 'Todas las pruebas se ejecutaron correctamente.'
        archiveArtifacts artifacts: 'results-docker/**', allowEmptyArchive: true
        junit 'results-docker/**/*.xml'
        }
    }
}