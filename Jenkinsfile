pipeline {
    agent any

    stages {

        stage('Clean up previous containers') {
            steps {
                sh '''
                    docker rm -f api-test-coffee-app 2>/dev/null || true
                    docker rm -f jmeter-test-coffee-app 2>/dev/null || true
                    docker rm -f zap-test-coffee-app 2>/dev/null || true
                    docker rm -f cypress-test-coffee-app 2>/dev/null || true

                    docker ps -a --filter "name=coffee" -q | xargs -r docker rm -f

                    docker network rm pipeline-coffee-cart_qa-network 2>/dev/null || true

                    docker network prune -f
                    docker-compose down -v --remove-orphans 2>/dev/null || true
                '''
            }
        }

        stage('Ejecutar pruebas') {

            stages {

                stage('Cypress') {
                    steps {
                        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                            sh 'docker-compose up --build --abort-on-container-exit cypress-tests'
                        }
                    }
                }

                stage('Jmeter') {
                    steps {
                        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                            sh 'docker-compose up --build --abort-on-container-exit jmeter-tests'
                        }
                    }
                }

                stage('Zap') {
                    steps {
                        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                            sh 'docker-compose up --build --abort-on-container-exit zap-tests'
                        }
                    }
                }

            }
        }
    }

    post {

        always {
            sh 'docker-compose down --remove-orphans || true'
        }

        success {
            echo 'Todas las pruebas se ejecutaron correctamente.'

            archiveArtifacts artifacts: 'results-docker/**', allowEmptyArchive: true

            junit 'results-docker/**/*.xml'
        }

        unstable {
            echo 'Algunas pruebas fallaron, pero el pipeline continuó.'
        }

        failure {
            echo 'El pipeline falló.'
        }
    }
}