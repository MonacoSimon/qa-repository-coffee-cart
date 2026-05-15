# Automation Testing - Cypress

Este módulo contiene pruebas automatizadas end-to-end (E2E) implementadas con Cypress sobre la aplicación Coffee Cart.

Las pruebas están diseñadas para ejecutarse tanto en entorno local como dentro de contenedores Docker, permitiendo integrarlas fácilmente en pipelines de CI/CD utilizando Jenkins y Docker Compose.

---

## Estructura del proyecto

```text
automation/
├── cypress/
│   ├── cypress/              # Casos de prueba E2E
│   ├── cypress.config.js     # Configuración de Cypress
│   ├── package.json          # Dependencias del proyecto
│   └── package-lock.json
├── Dockerfile                # Imagen Docker para ejecutar Cypress
├── run.sh                    # Script de ejecución local
└── README.md
```

---

## Objetivo

Validar el comportamiento funcional de la aplicación mediante pruebas automatizadas de interfaz simulando flujos reales de usuario.

Los escenarios automatizados cubren:

* navegación principal
* agregado de productos al carrito
* eliminación de productos
* validación del botón de compra
* validación de descuentos
* interacción hover sobre el carrito
* modal de confirmación mediante click derecho
* cambio dinámico del título de productos
* pruebas con publicidad habilitada
* validaciones de accesibilidad utilizando axe-core

---

## Casos de prueba implementados

| Archivo | Descripción |
|---|---|
| `add-product-cart.cy.js` | Agrega un producto al carrito |
| `remove-product-from-cart.cy.js` | Elimina productos del carrito |
| `add-multiple-products-to-cart.cy.js` | Agrega múltiples productos |
| `pay-for-a-product.cy.js` | Simula proceso de compra |
| `pay-hover.cy.js` | Verifica preview del carrito mediante hover |
| `button-add-to-cart.cy.js` | Valida botón de agregado |
| `change-caffee-title.cy.js` | Cambia el título del producto mediante doble click |
| `get-a-discount.cy.js` | Verifica promociones automáticas |
| `verify-button-github.cy.js` | Verifica acceso al repositorio GitHub |
| `add-advertising.cy.js` | Ejecuta pruebas con publicidad habilitada |
| `accesibility-with-axe.cy.js` | Validaciones de accesibilidad con axe-core |
| `index.cy.js` | Flujo principal general |

---

## Resultado de ejecución

Resumen de la última ejecución automatizada:

| Métrica | Resultado |
|---|---|
| Total de pruebas | 12 |
| Exitosas | 11 |
| Fallidas | 1 |
| Tiempo total | 55 segundos |
| Porcentaje exitoso | 92% |

La única prueba fallida corresponde a validaciones de accesibilidad:

```text
accesibility-with-axe.cy.js
```

El fallo detectado pertenece a una violación de contraste de colores (`color-contrast`) reportada por axe-core.

---

## Ejecución de pruebas

### 1. Ejecución local

Instalar dependencias:

```bash
cd cypress
npm install
```

Ejecutar pruebas:

```bash
npx cypress run
```

---

### 2. Ejecución mediante script

Dar permisos al script:

```bash
chmod +x run.sh
```

Ejecutar:

```bash
./run.sh
```

---

### 3. Ejecución con Docker

Construir imagen:

```bash
docker build -t coffee-cypress .
```

Ejecutar contenedor:

```bash
docker run --rm coffee-cypress
```

---

## Dockerfile utilizado

```Dockerfile
FROM cypress/included:latest

WORKDIR /e2e

COPY cypress/ ./

CMD ["cypress", "run"]
```

La imagen utiliza Cypress preinstalado y ejecuta automáticamente las pruebas al iniciar el contenedor.

---

## Configuración

La configuración principal se encuentra en:

```text
cypress/cypress.config.js
```

Se recomienda parametrizar la URL base:

```js
baseUrl: process.env.CYPRESS_BASE_URL || 'https://coffee-cart.app'
```

Esto permite reutilizar las pruebas en distintos entornos.

---

## Accesibilidad

Las pruebas de accesibilidad utilizan:

* Cypress Axe
* axe-core

Objetivo:

* detectar problemas críticos y severos WCAG
* validar contraste
* identificar errores de navegación accesible

Ejemplo:

```js
cy.injectAxe()

cy.checkA11y(null, {
  includedImpacts: ['critical', 'serious']
})
```

---

## Integración con CI/CD

Este módulo está preparado para pipelines automatizados utilizando Jenkins.

Flujo de integración:

```text
Jenkins
   ↓
Docker Compose
   ↓
Contenedor Cypress
   ↓
Ejecución automática de pruebas
   ↓
Generación de resultados
```

El objetivo es permitir ejecuciones repetibles y desacopladas del entorno local.

---

## Consideraciones

* Las pruebas dependen de la disponibilidad de la aplicación bajo prueba.
* Algunos elementos dinámicos requieren validaciones explícitas.
* Los flujos visuales pueden verse afectados por cambios de UI.
* Las pruebas de accesibilidad pueden detectar fallos reales de la aplicación.

---

## Tecnologías utilizadas

* Cypress
* JavaScript
* Docker
* Docker Compose
* Jenkins
* axe-core
* Cypress Axe

---

## Enfoque

El proyecto prioriza:

* automatización reproducible
* desacoplamiento entre tests y aplicación
* ejecución en contenedores
* integración continua
* validación funcional y accesibilidad
* mantenimiento sencillo de escenarios E2E
