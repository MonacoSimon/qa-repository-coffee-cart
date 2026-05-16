#!/bin/bash

set -e

echo "==================================="
echo " Verificación de entorno QA"
echo "==================================="

echo ""
echo "[1/5] Verificando Docker..."

if ! command -v docker &> /dev/null
then
    echo "ERROR: Docker no está instalado"
    exit 1
fi

echo "OK - Docker encontrado"

echo ""
echo "[2/5] Verificando Docker Compose..."

if ! docker compose version &> /dev/null
then
    echo "ERROR: Docker Compose no encontrado"
    exit 1
fi

echo "OK - Docker Compose encontrado"

echo ""
echo "[3/5] Verificando Docker daemon..."

if ! docker info &> /dev/null
then
    echo "ERROR: Docker daemon no está corriendo"
    exit 1
fi

echo "OK - Docker daemon activo"

echo ""
echo "[4/5] Verificando docker-compose.yml..."

if [ ! -f docker-compose.yml ]; then
    echo "ERROR: docker-compose.yml no encontrado"
    exit 1
fi

echo "OK - docker-compose.yml encontrado"

echo ""
echo "[5/5] Versiones instaladas"

docker --version
docker compose version

echo ""
echo "==================================="
echo " Entorno listo"
echo "==================================="
