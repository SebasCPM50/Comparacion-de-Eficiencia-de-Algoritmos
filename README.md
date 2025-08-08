# Comparacion-de-Eficiencia-de-Algoritmos
Actividad de Paradigmas de Programación Semestre 2025-2

El Propósito de la Tarea es:
Evaluar la eficacia de dos versiones del algoritmo para calcular el factorial de un número entero positivo: una versión recursiva y otra iterativa.  Con esta comparación, se busca:
- Comprender las diferencias entre algoritmos recursivos e iterativos.
- Medir el rendimiento (tiempo de ejecución y uso de memoria) de ambas implementaciones.
- Visualizar gráficamente los resultados obtenidos.
- Documentar el proceso de diseño y análisis en un repositorio estructurado y reproducible.

Implementación
Se implementaron dos funciones en Python y C.
facto_r(n) → Recursiva.
facto_i(n) → Iterativa.

Medición
Python:
Tiempo: módulo time
Memoria: módulo memory_profiler
C:
Tiempo: clock() de time.h
Memoria: herramienta valgrind con massif

Resultados
Iterativa más rápida y usa menos memoria para valores grandes.
Recursiva puede generar RecursionError en Python por límite de profundidad.

🔗 Cómo correr
Python:
```bash
pip install memory_profiler matplotlib
python graficas.py

C
gcc main.c -o factorial
./factorial

- Sebastián Chaux Palencia