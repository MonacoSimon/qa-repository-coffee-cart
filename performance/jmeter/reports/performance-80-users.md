# Performance Analysis Report – Coffee Cart (80 usuarios)

## Objetivo

Evaluar el comportamiento de la aplicación web Coffee Cart bajo una carga de 80 usuarios 
concurrentes, analizando tiempos de respuesta, estabilidad y capacidad de procesamiento.

---

## Métricas obtenidas

* Usuarios concurrentes: 80
* Tiempo promedio (average): 91 ms
* Tiempo mínimo (min): 40 ms
* Tiempo máximo (max): 504 ms
* Mediana (median): 67 ms
* Percentil 90 (P90): 136 ms
* Percentil 95 (P95): 147 ms
* Percentil 99 (P99): 152 ms
* Tasa de error: 0 %
* Throughput: 2.7 requests/segundo

---

## Análisis de resultados

### Tiempo de respuesta

El tiempo promedio de 91 ms continúa siendo bajo incluso bajo una carga de 80 usuarios 
concurrentes, lo que indica un comportamiento eficiente del sistema.

La mediana de 67 ms muestra que la mayoría de las solicitudes fueron respondidas rápidamente
 y de manera consistente.

Aunque el tiempo máximo alcanzó 504 ms, este valor parece corresponder a un caso aislado 
y no afecta significativamente el comportamiento general de la aplicación.

---

### Percentiles

* P90: 136 ms
* P95: 147 ms
* P99: 152 ms

Estos valores indican que:

* el 90 % de las solicitudes respondió en menos de 136 ms
* el 95 % respondió en menos de 147 ms
* incluso el 99 % se mantuvo en valores bajos y estables

La cercanía entre los percentiles evidencia una distribución homogénea de los tiempos de 
respuesta.

A pesar del valor máximo registrado de 504 ms, los percentiles demuestran que la gran 
mayoría de las requests mantuvo tiempos bajos.

---

### Estabilidad

La tasa de error fue de 0 %, indicando que:

* todas las solicitudes fueron procesadas correctamente
* no hubo fallos funcionales bajo carga
* la aplicación mantuvo estabilidad durante toda la prueba

Esto refleja buena tolerancia a concurrencia moderada-alta.

---

### Throughput

El throughput alcanzó 2.7 requests por segundo, superior a pruebas anteriores.

Esto indica que el sistema logró procesar una mayor cantidad de solicitudes por unidad de 
tiempo manteniendo tiempos de respuesta bajos.

El aumento del throughput sin degradación significativa es un indicador positivo de 
escalabilidad.

---

## Análisis general

La aplicación mostró un comportamiento estable y eficiente bajo una carga de 80 usuarios 
concurrentes.

Se observa:

* tiempos de respuesta consistentemente bajos
* estabilidad en percentiles altos
* ausencia total de errores
* incremento del throughput respecto a cargas menores

El sistema mantiene buen rendimiento incluso aumentando considerablemente la concurrencia.

El único valor atípico corresponde al tiempo máximo de 504 ms, aunque no impacta de 
forma significativa en el comportamiento global.

---

## Conclusión

La aplicación Coffee Cart respondió correctamente bajo una carga de 80 usuarios 
concurrentes, manteniendo estabilidad y tiempos de respuesta bajos.

Los percentiles muestran un comportamiento consistente y sin degradaciones importantes, 
mientras que el throughput aumentó respecto a pruebas anteriores.

La ausencia de errores y la estabilidad general sugieren que la aplicación puede manejar 
adecuadamente escenarios concurrentes moderadamente altos.

Se recomienda:

* continuar incrementando la carga para evaluar el punto de saturación
* ejecutar pruebas de estrés para detectar límites operativos
* monitorear recursos del sistema durante cargas más intensas
* analizar el origen de los picos aislados de latencia

En su estado actual, la aplicación demuestra un buen nivel de rendimiento y escalabilidad 
para cargas concurrentes moderadamente altas.
