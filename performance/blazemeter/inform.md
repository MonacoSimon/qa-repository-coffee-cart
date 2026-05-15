# Performance Analysis Report – BlazeMeter (50 Virtual Users)

## Objetivo

Evaluar el comportamiento de la aplicación bajo una carga de 50 usuarios virtuales 
concurrentes utilizando BlazeMeter, analizando:

* tiempos de respuesta
* throughput
* estabilidad
* tasa de errores
* consumo de ancho de banda

---

# Métricas obtenidas

| Métrica | Valor |
|---|---|
| Usuarios virtuales máximos | 50 |
| Hits por segundo | 7.87 hits/s |
| Throughput promedio | 17.96 |
| Tiempo promedio de respuesta | 6285.36 ms |
| Percentil 90 | 30.02 s |
| Tasa de errores | 31.69 % |

---

# Análisis de resultados

## Tiempo de respuesta

El tiempo promedio de respuesta es de:

```text
6285.36 ms (~6.2 segundos)
```

Este valor es elevado para una carga de solo 50 usuarios concurrentes y evidencia problemas 
importantes de rendimiento.

Un usuario final percibiría:

* lentitud en navegación
* demoras en acciones
* mala experiencia de uso
* sensación de aplicación inestable

---

## Percentil 90 (P90)

El percentil 90 alcanzó:

```text
30.02 segundos
```

Esto significa que:

* el 10 % de las solicitudes tarda más de 30 segundos
* existen requests extremadamente lentas
* el sistema presenta alta variabilidad bajo carga

Este comportamiento suele indicar:

* saturación de recursos
* cuellos de botella
* problemas de concurrencia
* degradación progresiva

---

# Tasa de errores

La tasa de errores registrada fue:

```text
31.69 %
```

Este es el indicador más crítico del análisis.

Implica que:

* aproximadamente 1 de cada 3 requests falla
* el sistema pierde estabilidad bajo carga
* existen limitaciones importantes de escalabilidad

Los errores pueden estar relacionados con:

* timeouts
* saturación del backend
* errores HTTP 5xx
* limitaciones de conexiones
* problemas de memoria o CPU

---

# Throughput

El throughput promedio fue:

```text
17.96
```

y el sistema procesó:

```text
7.87 hits por segundo
```

Esto indica que:

* la aplicación continúa procesando tráfico
* existe capacidad parcial de respuesta
* el rendimiento no escala correctamente respecto al volumen de usuarios

La relación entre:

* alto tiempo de respuesta
* alta tasa de errores
* throughput moderado

sugiere degradación significativa bajo concurrencia.

---

# Consumo de ancho de banda

El ancho de banda promedio registrado indica actividad constante entre cliente y servidor.

Sin embargo, debido a:

* tiempos elevados
* errores frecuentes
* requests lentas

es probable que existan:

* retransmisiones
* esperas prolongadas
* acumulación de conexiones activas

---

# Estabilidad general

La aplicación no logró mantener estabilidad bajo una carga de 50 usuarios virtuales.

Se observa:

* degradación severa de performance
* incremento extremo en tiempos de respuesta
* alta cantidad de errores
* comportamiento inconsistente

Aunque el sistema sigue respondiendo parcialmente, la experiencia de usuario se considera 
deficiente.

---

# Posibles causas técnicas

Los resultados pueden estar asociados a:

* saturación del backend
* consultas lentas a base de datos
* recursos insuficientes
* falta de balanceo
* problemas de concurrencia
* bloqueos internos
* límites de conexiones simultáneas
* ausencia de caching

---

# Recomendaciones

## Infraestructura

* aumentar recursos CPU/RAM
* revisar límites de contenedores Docker
* optimizar configuración del servidor

---

## Backend

* optimizar queries
* reducir operaciones bloqueantes
* implementar caching
* revisar manejo de concurrencia

---

## Testing

* ejecutar pruebas escalonadas
* analizar comportamiento entre 20, 50 y 100 usuarios
* monitorear consumo de recursos durante carga

---

## Observabilidad

Implementar monitoreo con:

* CloudWatch
* Grafana
* Prometheus
* métricas de contenedores Docker

---

# Conclusión

La aplicación presenta problemas importantes de escalabilidad bajo una carga de 50 usuarios 
virtuales.

Los indicadores más críticos son:

* 31.69 % de errores
* tiempo promedio superior a 6 segundos
* percentil 90 extremadamente alto (30 s)

Aunque el sistema continúa procesando requests, la estabilidad general es insuficiente 
para soportar carga concurrente de manera confiable.

Se requieren optimizaciones tanto a nivel infraestructura como aplicación antes de
 considerar escenarios productivos con concurrencia moderada o alta.
