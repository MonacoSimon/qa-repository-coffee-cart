pipeline {
    agent any

    environment {
        COMPOSE_FILE = "${WORKSPACE}/docker-compose.yml"
    }

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

                stage('API Tests Newman') {
                    steps {
                        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                            sh '''
                                docker run --rm \
                                  --volumes-from $(hostname) \
                                  postman/newman:alpine \
                                  run ${WORKSPACE}/api-testing/postman/collections/api-testing-coffee-cart.postman_collection.json \
                                  -e ${WORKSPACE}/api-testing/postman/enviroment/environment-coffee-cart.postman_environment.json \
                                  --env-var "urlBase=https://coffee-cart.app/" \
                                  -r cli,json,junit \
                                  --reporter-json-export ${WORKSPACE}/results-docker/newman/report.json \
                                  --reporter-junit-export ${WORKSPACE}/results-docker/newman/report.xml
                            '''
                        }
                    }
                }

                stage('Cypress') {
                    steps {
                        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                            sh 'docker-compose up --build --abort-on-container-exit cypress-tests'
                        }
                    }
                }

                stage('Jmeter') {
                    steps {
                        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                            sh '''
                                mkdir -p ${WORKSPACE}/results-docker/jmeter
                                docker run --rm \
                                  --volumes-from $(hostname) \
                                  justb4/jmeter:latest \
                                  /bin/sh -c "
                                    found=0
                                    for test in ${WORKSPACE}/performance/jmeter/test-plan/*.jmx; do
                                      [ -f \\"\\$test\\" ] || continue
                                      found=1
                                      filename=\\$(basename \\$test .jmx)
                                      timestamp=\\$(date +%Y%m%d-%H%M%S)
                                      echo Ejecutando: \\$filename
                                      jmeter -n -f -t \\$test -l ${WORKSPACE}/results-docker/jmeter/\\$filename.jtl -e -o ${WORKSPACE}/results-docker/jmeter/\\$filename-report-\\$timestamp -j ${WORKSPACE}/results-docker/jmeter/\\$filename.log
                                      echo Terminado: \\$filename
                                    done
                                    if [ \\$found -eq 0 ]; then
                                      echo No se encontraron archivos .jmx
                                      exit 1
                                    fi
                                  "
                            '''
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

            archiveArtifacts artifacts: 'results-docker/**', allowEmptyArchive: true

            junit 'results-docker/**/*.xml'
        }

        success {

            echo 'Todas las pruebas se ejecutaron correctamente.'
        }

        unstable {

            echo 'Algunas pruebas fallaron, pero el pipeline continuó.'
        }

        failure {

            echo 'El pipeline falló.'
        }
    }
}