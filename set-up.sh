#!/bin/bash
set -e

echo "==================================="
echo " Verificacion de entorno QA"
echo "==================================="
echo ""

echo "[1/6] Verificando Docker..."
if ! command -v docker &> /dev/null; then
    echo "ERROR: Docker no esta instalado"
    exit 1
fi
echo "OK - Docker encontrado"
echo ""

echo "[2/6] Verificando Docker Compose..."
if ! docker compose version &> /dev/null; then
    echo "ERROR: Docker Compose no encontrado"
    exit 1
fi
echo "OK - Docker Compose encontrado"
echo ""

echo "[3/6] Verificando Docker daemon..."
if ! docker info &> /dev/null; then
    echo "ERROR: Docker daemon no esta corriendo"
    exit 1
fi
echo "OK - Docker daemon activo"
echo ""

echo "[4/6] Verificando docker-compose.yml..."
if [ ! -f docker-compose.yml ]; then
    echo "ERROR: docker-compose.yml no encontrado"
    exit 1
fi
echo "OK - docker-compose.yml encontrado"
echo ""

echo "[5/6] Verificando Python3..."
if ! command -v python3 &> /dev/null; then
    echo "AVISO: python3 no encontrado - requerido para cloud-testing"
    echo "       Instalar con: sudo apt install python3 python3-venv python3-pip"
else
    echo "OK - $(python3 --version)"
fi
echo ""

echo "[6/6] Verificando entorno cloud-testing..."
if [ -d "cloud-testing" ]; then
    if [ ! -d "cloud-testing/venv" ]; then
        echo "Creando entorno virtual en cloud-testing/venv..."
        cd cloud-testing
        python3 -m venv venv
        source venv/bin/activate
        pip install --quiet -r requirements.txt
        deactivate
        cd ..
        echo "OK - Entorno virtual creado e instalado"
    else
        echo "OK - Entorno virtual ya existe"
    fi
    if [ ! -f "cloud-testing/localstack/docker-compose.yml" ]; then
        echo "AVISO: cloud-testing/localstack/docker-compose.yml no encontrado"
    else
        echo "OK - LocalStack docker-compose encontrado"
        echo ""
        echo "Para levantar LocalStack localmente:"
        echo "  cd cloud-testing/localstack && docker compose up -d"
        echo "  bash ../aws/scripts/setup_all.sh"
    fi
else
    echo "AVISO: directorio cloud-testing no encontrado"
fi
echo ""

echo "==================================="
echo " Versiones instaladas"
echo "==================================="
docker --version
docker compose version
python3 --version 2>/dev/null || echo "python3: no disponible"
echo ""
echo "==================================="
echo " Entorno listo"
echo "==================================="