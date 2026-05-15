#!/bin/bash

set -e

BASE_DIR=$(pwd)

TEST_PLAN_DIR="$BASE_DIR/test-plan"
RESULTS_DIR="$BASE_DIR/results-docker"

mkdir -p "$RESULTS_DIR"

echo "========================================="
echo "Ejecutando pruebas de rendimiento con JMeter"
echo "========================================="
echo "Directorio de planes de prueba: $TEST_PLAN_DIR"
echo "Directorio de resultados: $RESULTS_DIR"
echo ""

if [ -z "$(ls -A $TEST_PLAN_DIR/*.jmx 2>/dev/null)" ]; then
    echo "Error: No se encontraron archivos .jmx en $TEST_PLAN_DIR"
    exit 1
fi

echo "Planes de prueba encontrados:"
ls -1 "$TEST_PLAN_DIR"/*.jmx | xargs -n 1 basename
for test in "$TEST_PLAN_DIR"/*.jmx; do
    filename=$(basename "$test" .jmx)
    timestamp=$(date +%Y%m%d-%H%M%S)

    echo "Ejecutando: $filename"

    docker run --rm \
        -v "$TEST_PLAN_DIR":/tests \
        -v "$RESULTS_DIR":/results \
        justb4/jmeter:latest \
        -n \
        -t /tests/$(basename "$test") \
        -l /results/${filename}.jtl \
        -e \
        -o /results/${filename}-report-$timestamp \
        -j /results/${filename}.log

    echo "Finalizado: $filename"
    echo "Reporte generado: results-docker/${filename}-report-$timestamp/index.html"
done

echo "Resultados guardados en: $RESULTS_DIR"
