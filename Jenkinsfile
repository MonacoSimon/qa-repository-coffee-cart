pipeline{
    agent any
    stages{

        
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


        stage('Ejecutar pruebas'){
            stages {
                

                stage('API Tests Newman') {
                steps {
                    sh '''
                        set -e

                        BASE_DIR=$(pwd)

                        RESULTS_DIR="$BASE_DIR/results-docker"

                        mkdir -p "$RESULTS_DIR"

                        echo "Ejecutando Newman con Docker..."

                        docker run --rm -t \
                        -v "$BASE_DIR/postman":/etc/newman \
                        -v "$RESULTS_DIR":/results \
                        postman/newman:alpine \
                        run /etc/newman/collections/api-testing-coffee-cart.postman_collection.json \
                        -e /etc/newman/enviroment/environment-coffee-cart.postman_environment.json \
                        --env-var "urlBase=https://coffee-cart.app/" \
                        -r cli,json \
                        --reporter-json-export /results/report.json

                        echo "Ejecución finalizada"
                    '''
                    }
                }

                stage('Cypress'){
                    steps{
                        sh 'docker-compose up --build --abort-on-container-exit cypress-tests'
                    }
                }

                stage('Jmeter'){
                    steps{
                        sh 'docker-compose up --build --abort-on-container-exit jmeter-tests'
                    }
                }

                stage ('Zap'){
                    steps{
                        sh 'docker-compose up --build --abort-on-container-exit zap-tests'
                    }
                }
            }
        }

    }

    post{
        always {
            sh 'docker-compose down --remove-orphans || true'
        }

    success {
        echo 'Todas las pruebas se ejecutaron correctamente.'
        archiveArtifacts artifacts: 'results-docker/**', allowEmptyArchive: true
        junit 'results-docker/**/*.xml'
        }
    }
}