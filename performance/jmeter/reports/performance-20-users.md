# Performance Analysis Report – Coffee Cart (20 usuarios)

## Objetivo

Evaluar el comportamiento de la aplicación web Coffee Cart bajo una carga de 20 usuarios 
concurrentes, analizando tiempos de respuesta, estabilidad y capacidad de procesamiento.

---

## Métricas obtenidas

* Usuarios concurrentes: 20
* Tiempo promedio (average): 100 ms
* Tiempo mínimo (min): 40 ms
* Tiempo máximo (max): 621 ms
* Mediana (median): 56 ms
* Percentil 90 (P90): 135 ms
* Percentil 95 (P95): 137 ms
* Percentil 99 (P99): 621 ms
* Tasa de error: 0 %
* Throughput: 1.9 requests/segundo

---

## Análisis de resultados

### Tiempo de respuesta

El tiempo promedio de 100 ms indica un rendimiento general bueno para una carga de 
20 usuarios concurrentes.

La mediana de 56 ms muestra que la mayoría de las solicitudes fueron respondidas rápidamente
 y con baja latencia.

El tiempo mínimo de 40 ms confirma que el sistema puede responder de forma muy eficiente 
en condiciones normales.

Sin embargo, el tiempo máximo de 621 ms evidencia la existencia de algunos picos de 
latencia aislados.

---

### Percentiles

* P90: 135 ms
* P95: 137 ms
* P99: 621 ms

Estos valores indican que:

* el 90 % de las solicitudes respondió en menos de 135 ms
* el 95 % respondió en menos de 137 ms
* solo el 1 % alcanzó tiempos elevados cercanos a 621 ms

Esto demuestra que el sistema mantiene tiempos de respuesta consistentes para casi 
todas las requests, aunque existen algunos outliers puntuales.

---

### Estabilidad

La tasa de error fue de 0 %, lo que indica que:

* todas las solicitudes fueron procesadas correctamente
* no hubo fallos funcionales durante la prueba
* la aplicación mantuvo estabilidad bajo concurrencia

Esto representa un comportamiento positivo desde el punto de vista funcional.

---

### Throughput

El throughput obtenido fue de 1.9 requests por segundo.

Esto indica que el sistema fue capaz de mantener procesamiento continuo de solicitudes 
durante toda la ejecución de la prueba.

Aunque el throughput no es especialmente alto, los tiempos de respuesta observados 
fueron bajos y estables.

---

## Análisis general

La aplicación mostró un comportamiento estable y consistente bajo una carga de 20 
usuarios concurrentes.

Se observa:

* tiempos de respuesta bajos en la mayoría de las solicitudes
* ausencia total de errores
* estabilidad general durante la ejecución
* algunos picos aislados reflejados en el percentil 99

El sistema parece responder correctamente para cargas moderadas y mantiene una buena 
experiencia de usuario en condiciones normales.

---

## Conclusión

La aplicación Coffee Cart respondió correctamente bajo una carga de 20 usuarios concurrentes,
 manteniendo tiempos de respuesta bajos y sin errores funcionales.

La mayoría de las solicitudes se resolvió en menos de 140 ms, lo que indica un rendimiento 
adecuado para escenarios de concurrencia moderada.

Aunque se detectaron algunos valores elevados en el percentil 99, estos casos fueron 
aislados y no afectaron el comportamiento general del sistema.

Se recomienda:

* continuar realizando pruebas con mayores niveles de concurrencia
* monitorear posibles picos de latencia
* evaluar escalabilidad bajo cargas más intensas
* analizar comportamiento del frontend y backend ante estrés prolongado

En su estado actual, la aplicación presenta un rendimiento estable y adecuado para 
escenarios de uso concurrente moderado.
