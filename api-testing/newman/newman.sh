#!/bin/bash

newman run ../postman/collections/api-testing-coffee-cart.postman_collection.json --env-var "urlBase=https://coffee-cart.app/" 

echo "generando informe..."
newman run ../postman/collections/api-testing-coffee-cart.postman_collection.json --env-var "urlBase=https://coffee-cart.app/" -r htmlextra --reporter-htmlextra-export results-newman/report.html
echo "lo puede encontrar en results-docker como un html"
echo "para correrlo, ejecutar el comando: firefox report.html"
