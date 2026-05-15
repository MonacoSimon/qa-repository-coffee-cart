# Performance Analysis Report – Coffee Cart (50 usuarios)

## Objetivo

Evaluar el comportamiento de la aplicación web Coffee Cart bajo una carga de 50 usuarios 
concurrentes, analizando tiempos de respuesta, estabilidad y capacidad de procesamiento.

---

## Métricas obtenidas

* Usuarios concurrentes: 50
* Tiempo promedio (average): 91 ms
* Tiempo mínimo (min): 43 ms
* Tiempo máximo (max): 167 ms
* Mediana (median): 66 ms
* Percentil 90 (P90): 139 ms
* Percentil 95 (P95): 141 ms
* Percentil 99 (P99): 160 ms
* Tasa de error: 0 %
* Throughput: 1.9 requests/segundo

---

## Análisis de resultados

### Tiempo de respuesta

El tiempo promedio de 91 ms indica un rendimiento muy bueno incluso bajo una carga de 
50 usuarios concurrentes.

La mediana de 66 ms demuestra que la mayoría de las solicitudes fueron procesadas 
rápidamente y de forma consistente.

El tiempo máximo de 167 ms se mantiene relativamente bajo, sin evidenciar picos 
críticos de latencia.

Esto sugiere que la aplicación mantiene estabilidad y capacidad de respuesta aun 
incrementando la concurrencia.

---

### Percentiles

* P90: 139 ms
* P95: 141 ms
* P99: 160 ms

Estos valores muestran que:

* el 90 % de las solicitudes respondió en menos de 139 ms
* el 95 % respondió en menos de 141 ms
* incluso el 1 % más lento se mantuvo por debajo de 160 ms

La baja diferencia entre percentiles refleja una distribución muy estable y homogénea en 
los tiempos de respuesta.

No se observan outliers severos ni degradaciones importantes bajo carga.

---

### Estabilidad

La tasa de error fue de 0 %, indicando que:

* todas las solicitudes fueron procesadas correctamente
* no hubo fallos funcionales durante la ejecución
* la aplicación mantuvo disponibilidad total bajo concurrencia

Esto evidencia un comportamiento estable y confiable.

---

### Throughput

El throughput registrado fue de 1.9 requests por segundo.

El sistema mantuvo procesamiento continuo y estable de solicitudes durante toda la prueba.

Combinado con los bajos tiempos de respuesta, esto indica un comportamiento eficiente 
bajo la carga aplicada.

---

## Análisis general

La aplicación mostró un rendimiento sólido bajo una carga de 50 usuarios concurrentes.

Se observa:

* tiempos de respuesta bajos y consistentes
* ausencia total de errores
* estabilidad en todos los percentiles
* inexistencia de picos extremos de latencia

A diferencia de escenarios donde el aumento de usuarios genera degradación significativa, 
en este caso la aplicación mantuvo 
métricas muy similares e incluso mejores que pruebas anteriores.

---

## Conclusión

La aplicación Coffee Cart presentó un comportamiento estable y eficiente bajo una 
carga de 50 usuarios concurrentes.

Los tiempos de respuesta permanecieron bajos y homogéneos, incluso en los percentiles 
más altos, sin aparición de outliers críticos.

La ausencia de errores y la consistencia general indican que el sistema puede manejar 
correctamente escenarios de concurrencia moderada.

Se recomienda:

* continuar aumentando gradualmente la carga para identificar límites de escalabilidad
* realizar pruebas prolongadas para detectar degradación por consumo de recursos
* monitorear uso de CPU, memoria y red durante ejecuciones más intensas
* complementar con pruebas de estrés y endurance

En su estado actual, la aplicación demuestra un rendimiento adecuado y estable para 
escenarios concurrentes moderados.
