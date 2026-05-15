#!/bin/bash

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
