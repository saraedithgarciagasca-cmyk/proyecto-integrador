# 02. Pruebas y validación

Todas las pruebas se ejecutaron con `python main.py`. Las capturas de cada ejecución están en `evidencias/ejecuciones/`.

## Comparación con el ejercicio original

Primero se ejecutaron los mismos datos del ejercicio original (opción 2 del menú) y se compararon con las tablas de `01_analisis_problema.md`:

| Método | Iteraciones (original) | Iteraciones (programa) | Solución (original) | Solución (programa) | ¿Coincide? |
|---|---|---|---|---|---|
| Jacobi | 5 | 5 | (2.999999, -2.500001, 6.999999) | (2.999999, -2.500001, 6.999999) | Sí |
| Gauss-Seidel | 4 | 4 | (3.000000, -2.500000, 7.000000) | (3.000000, -2.500000, 7.000000) | Sí |

Los valores de cada fila de las tablas de iteraciones y los errores también coinciden con los del ejercicio original.

---

## CP-01. Caso original con resultado conocido

| Campo | Descripción |
|---|---|
| Identificador | CP-01 |
| Objetivo | Verificar que el programa reproduce el resultado del ejercicio original de Análisis Numérico con ambos métodos. |
| Entradas | Opción 2 (cargar ejercicio original). Opción 4 y opción 5 con tolerancia = 0.0001 e iteraciones máximas = 100. Sistema: $3x_1 - 0.1x_2 - 0.2x_3 = 7.85$; $0.1x_1 + 7x_2 - 0.3x_3 = -19.3$; $0.3x_1 - 0.2x_2 + 10x_3 = 71.4$ |
| Resultado esperado | Jacobi converge en 5 iteraciones con $x \approx (3, -2.5, 7)$; Gauss-Seidel converge en 4 iteraciones con $x \approx (3, -2.5, 7)$. |
| Resultado obtenido | Jacobi: convergió en 5 iteraciones, $x = (2.999999, -2.500001, 6.999999)$. Gauss-Seidel: convergió en 4 iteraciones, $x = (3.000000, -2.500000, 7.000000)$. |
| Estado | Correcto |
| Observaciones | Las tablas de iteraciones coinciden fila por fila con el trabajo original. Evidencia: `caso_original_jacobi.png`, `caso_original_gauss_seidel.png`. |

## CP-02. Caso normal adicional con datos válidos

| Campo | Descripción |
|---|---|
| Identificador | CP-02 |
| Objetivo | Comprobar el funcionamiento con un sistema de 4 × 4 capturado por teclado. |
| Entradas | Opción 1, $n = 4$. Sistema: $10x_1 - x_2 + 2x_3 = 6$; $-x_1 + 11x_2 - x_3 + 3x_4 = 25$; $2x_1 - x_2 + 10x_3 - x_4 = -11$; $3x_2 - x_3 + 8x_4 = 15$. Opciones 3, 4 y 5 con tolerancia = 0.0001 e iteraciones máximas = 100. |
| Resultado esperado | Sistema diagonalmente dominante. Ambos métodos convergen a la solución exacta $x = (1, 2, -1, 1)$; Gauss-Seidel en menos iteraciones que Jacobi. |
| Resultado obtenido | "SÍ es diagonalmente dominante". Jacobi: convergió en 13 iteraciones, $x = (0.999990, 2.000016, -1.000013, 1.000019)$. Gauss-Seidel: convergió en 6 iteraciones, $x = (1.000008, 2.000001, -1.000003, 0.999999)$. |
| Estado | Correcto |
| Observaciones | La comprobación muestra que cada ecuación evaluada es prácticamente igual a su término independiente. Evidencia: `prueba_02_caso_normal.png`. |

## CP-03. Caso límite permitido por el problema

| Campo | Descripción |
|---|---|
| Identificador | CP-03 |
| Objetivo | Probar el tamaño mínimo del sistema ($n = 2$) y el número mínimo de iteraciones (1). |
| Entradas | Opción 1, $n = 2$: $4x_1 + x_2 = 9$; $x_1 + 3x_2 = 5$. Opción 5 con tolerancia = 0.0001 e iteraciones máximas = 1; después opción 5 con iteraciones máximas = 100. |
| Resultado esperado | Con 1 iteración: se muestra una sola fila y el mensaje "No convergió en 1 iteraciones". Con 100 iteraciones: converge a $x = (2, 1)$. |
| Resultado obtenido | Con 1 iteración: $x = (2.250000, 0.916667)$, error = 2.25, "No convergió en 1 iteraciones". Con 100 iteraciones: convergió en 6 iteraciones, $x = (2.000001, 1.000000)$. |
| Estado | Correcto |
| Observaciones | El programa acepta los valores límite y respeta el criterio de paro por número máximo de iteraciones. Evidencia: `prueba_03_caso_limite.png`. |

## CP-04. Caso con entrada inválida

| Campo | Descripción |
|---|---|
| Identificador | CP-04 |
| Objetivo | Verificar las validaciones de entrada. |
| Entradas | Opción `7` (fuera de rango), opción `abc` (no numérica), opción 1 con $n = 11$ (fuera de rango) y después $n = 2$ con un cero en la diagonal: $0x_1 + 1x_2 = 1$; $1x_1 + 2x_2 = 2$. |
| Resultado esperado | Mensajes de error para cada dato inválido, se vuelve a pedir el dato y el sistema con cero en la diagonal se rechaza. |
| Resultado obtenido | "el valor debe estar entre 0 y 5", "debe escribir un número entero", "el valor debe estar entre 2 y 10" y "El coeficiente de x1 en la ecuación 1 (diagonal principal) no puede ser 0." El sistema no se guarda y se regresa al menú. |
| Estado | Correcto |
| Observaciones | El programa no se detiene por entradas inválidas. Evidencia: `prueba_04_entrada_invalida.png`. |

## CP-05. Regla relevante: sistema no diagonalmente dominante

| Campo | Descripción |
|---|---|
| Identificador | CP-05 |
| Objetivo | Verificar la regla de dominancia diagonal: aviso al usuario y comportamiento del método cuando no converge. |
| Entradas | Opción 1, $n = 2$: $x_1 + 5x_2 = 6$; $7x_1 + x_2 = 8$. Opción 3 y opción 4 con tolerancia = 0.0001 e iteraciones máximas = 10. |
| Resultado esperado | "NO es diagonalmente dominante", aviso antes de resolver, tabla de 10 iteraciones con valores que crecen y mensaje "No convergió en 10 iteraciones". |
| Resultado obtenido | Se muestran el aviso y el mensaje "No convergió en 10 iteraciones", pero en las iteraciones 8 a 10 las columnas de la tabla aparecen pegadas (por ejemplo `-1500624.000000-1500624.000000...`) y no se pueden leer. |
| Estado | Falla |
| Observaciones | La regla funciona, pero el formato de la tabla no separa columnas cuando los números tienen más de 14 caracteres. Evidencia: `prueba_05_regla_dominancia.png`. |
