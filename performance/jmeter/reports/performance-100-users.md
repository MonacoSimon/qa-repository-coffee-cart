# Performance Analysis Report – Coffee Cart (100 usuarios)

## Objetivo

Evaluar el comportamiento de la aplicación web Coffee Cart bajo una carga de 100 
usuarios concurrentes, analizando tiempos de respuesta, estabilidad y capacidad de 
procesamiento.

---

## Métricas obtenidas

* Usuarios concurrentes: 100
* Tiempo promedio (average): 89 ms
* Tiempo mínimo (min): 41 ms
* Tiempo máximo (max): 352 ms
* Mediana (median): 68 ms
* Percentil 90 (P90): 133 ms
* Percentil 95 (P95): 140 ms
* Percentil 99 (P99): 174 ms
* Tasa de error: 0 %
* Throughput: 3.3 requests/segundo

---

## Análisis de resultados

### Tiempo de respuesta

El tiempo promedio de 89 ms indica que la aplicación mantiene un rendimiento muy bueno 
incluso bajo una carga de 100 usuarios concurrentes.

La mediana de 68 ms muestra que la mayoría de las solicitudes continúan respondiéndose 
rápidamente y de forma estable.

El tiempo máximo registrado fue de 352 ms, valor considerablemente inferior a escenarios 
donde el sistema comienza a degradarse severamente bajo carga.

En términos generales, los tiempos de respuesta permanecen bajos y consistentes.

---

### Percentiles

* P90: 133 ms
* P95: 140 ms
* P99: 174 ms

Estos resultados indican que:

* el 90 % de las solicitudes respondió en menos de 133 ms
* el 95 % respondió en menos de 140 ms
* incluso el 99 % mantuvo tiempos inferiores a 174 ms

La baja variación entre percentiles demuestra un comportamiento estable y homogéneo bajo 
concurrencia elevada.

No se observan outliers extremos ni degradaciones significativas.

---

### Estabilidad

La tasa de error fue de 0 %, lo que indica que:

* todas las solicitudes fueron procesadas correctamente
* no se registraron fallos funcionales
* la aplicación mantuvo estabilidad durante toda la prueba

Esto evidencia una buena capacidad para soportar carga concurrente elevada.

---

### Throughput

El throughput alcanzó 3.3 requests por segundo, mostrando una mejora respecto a pruebas 
anteriores.

El aumento del throughput acompañado de tiempos de respuesta bajos indica que el sistema 
logra escalar adecuadamente bajo mayor concurrencia.

Esto representa un indicador positivo de capacidad de procesamiento.

---

## Análisis general

La aplicación mostró un comportamiento sólido bajo una carga de 100 usuarios concurrentes.

Se observa:

* tiempos de respuesta bajos y estables
* ausencia total de errores
* buena consistencia entre percentiles
* aumento progresivo del throughput
* ausencia de degradación severa bajo carga

El sistema mantiene estabilidad incluso incrementando considerablemente la cantidad de 
usuarios concurrentes.

---

## Conclusión

La aplicación Coffee Cart respondió correctamente bajo una carga de 100 usuarios 
concurrentes, manteniendo estabilidad y un rendimiento consistente.

Los tiempos de respuesta permanecieron bajos en todos los percentiles y no se registraron 
errores funcionales durante la ejecución.

El incremento del throughput respecto a pruebas anteriores sugiere que el sistema escala 
adecuadamente bajo mayores niveles de concurrencia.

Se recomienda:

* continuar realizando pruebas con cargas superiores
* ejecutar pruebas de estrés y endurance
* monitorear recursos de infraestructura durante ejecuciones prolongadas
* analizar comportamiento ante picos extremos de concurrencia

En su estado actual, la aplicación demuestra buena capacidad de escalabilidad y estabilidad 
para escenarios concurrentes altos.
