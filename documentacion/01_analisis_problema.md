# 01. Análisis del problema

## 1. Nombre del problema y asignatura

- **Problema:** Solución de sistemas de ecuaciones lineales mediante los métodos iterativos de Jacobi y Gauss-Seidel.
- **Asignatura donde se estudió:** Análisis Numérico.

## 2. Descripción, justificación y planteamiento original

### Descripción

Un sistema de *n* ecuaciones lineales con *n* incógnitas se escribe en forma matricial como $A\,x = b$, donde $A$ es la matriz de coeficientes, $x$ el vector de incógnitas y $b$ el vector de términos independientes.

Los métodos de Jacobi y Gauss-Seidel no resuelven el sistema de forma directa: parten de un vector inicial (normalmente ceros) y, en cada iteración, despejan cada incógnita de su ecuación para obtener una aproximación nueva. El proceso se repite hasta que la diferencia entre dos aproximaciones consecutivas es menor que una tolerancia o hasta alcanzar un número máximo de iteraciones.

- **Jacobi:** cada nueva incógnita se calcula usando **solo** los valores de la iteración anterior.
- **Gauss-Seidel:** cada nueva incógnita se calcula usando los valores **más recientes** disponibles (los ya calculados en la misma iteración).

### Justificación

Resolver estos métodos a mano exige muchas operaciones repetitivas y es fácil cometer errores de arrastre en las tablas de iteraciones. El problema tiene entradas, procesos y salidas claramente identificables, incluye reglas y decisiones (diagonal distinta de cero, dominancia diagonal, criterio de paro, convergencia) y se puede organizar en dos clases con responsabilidades diferentes: una que representa el sistema y otra que aplica los métodos iterativos. Por ello es adecuado para una aplicación de consola en Python.

### Planteamiento original

Resolver el siguiente sistema por los métodos de Jacobi y de Gauss-Seidel, con vector inicial $x^{(0)} = (0, 0, 0)$ y tolerancia $0.0001$:

$$
\begin{aligned}
3x_1 - 0.1x_2 - 0.2x_3 &= 7.85 \\
0.1x_1 + 7x_2 - 0.3x_3 &= -19.3 \\
0.3x_1 - 0.2x_2 + 10x_3 &= 71.4
\end{aligned}
$$

## 3. Entradas

| Nombre | Tipo de dato | Restricciones | Significado |
|---|---|---|---|
| `n` | `int` | Entero entre 2 y 10 | Número de ecuaciones e incógnitas del sistema |
| `coeficientes` | `list` de `list` de `float` | Matriz de *n* × *n*; números reales; ningún elemento de la diagonal principal puede ser 0 | Matriz $A$ de coeficientes |
| `independientes` | `list` de `float` | Lista de *n* números reales | Vector $b$ de términos independientes |
| `tolerancia` | `float` | Mayor que 0 | Error máximo aceptado para detener las iteraciones |
| `max_iteraciones` | `int` | Entero entre 1 y 1000 | Número máximo de iteraciones permitidas |
| `opcion` | `int` | Una de las opciones del menú | Acción que el usuario desea realizar |

## 4. Procesos

### 4.1 Validación del sistema

1. La matriz debe ser cuadrada (*n* × *n*) y el vector $b$ debe tener *n* elementos.
2. Ningún elemento de la diagonal principal puede ser cero: $a_{ii} \neq 0$ (de lo contrario no se puede despejar $x_i$).

### 4.2 Verificación de dominancia diagonal

El sistema es diagonalmente dominante si en cada renglón se cumple:

$$
|a_{ii}| > \sum_{j \neq i} |a_{ij}|
$$

Si se cumple, la convergencia de ambos métodos está garantizada. Si no se cumple, se avisa al usuario de que el método **puede no converger**, pero el cálculo se permite.

### 4.3 Método de Jacobi

Para cada iteración $k = 1, 2, \dots$ y cada incógnita $i$:

$$
x_i^{(k)} = \frac{b_i - \displaystyle\sum_{j \neq i} a_{ij}\, x_j^{(k-1)}}{a_{ii}}
$$

### 4.4 Método de Gauss-Seidel

Para cada iteración $k = 1, 2, \dots$ y cada incógnita $i$:

$$
x_i^{(k)} = \frac{b_i - \displaystyle\sum_{j < i} a_{ij}\, x_j^{(k)} - \sum_{j > i} a_{ij}\, x_j^{(k-1)}}{a_{ii}}
$$

### 4.5 Cálculo del error y criterio de paro

En cada iteración se calcula el error absoluto máximo entre dos aproximaciones consecutivas:

$$
E^{(k)} = \max_{i} \left| x_i^{(k)} - x_i^{(k-1)} \right|
$$

- Si $E^{(k)} < \text{tolerancia}$, el método **converge** y se detiene.
- Si se alcanza `max_iteraciones` sin cumplir la tolerancia, se informa que el método **no convergió**.
- Si algún valor deja de ser un número finito (crece sin control), se detiene e informa que el método **diverge**.

### 4.6 Comprobación de la solución

Se sustituye la solución obtenida en cada ecuación y se calcula $\sum_j a_{ij}\, x_j$ para compararla con $b_i$.

## 5. Salidas esperadas

1. El sistema capturado mostrado en forma de ecuaciones.
2. Indicación de si el sistema es o no diagonalmente dominante.
3. Tabla de iteraciones: número de iteración, valores de $x_1, \dots, x_n$ y error de cada iteración.
4. Resultado: método utilizado, si convergió o no, número de iteraciones realizadas y solución aproximada.
5. Comprobación: valor de cada ecuación evaluada con la solución, comparado con el término independiente.
6. Mensajes de error cuando una entrada no es válida.

## 6. Ejemplo original resuelto

### Datos

$$
A = \begin{pmatrix} 3 & -0.1 & -0.2 \\ 0.1 & 7 & -0.3 \\ 0.3 & -0.2 & 10 \end{pmatrix}, \qquad
b = \begin{pmatrix} 7.85 \\ -19.3 \\ 71.4 \end{pmatrix}, \qquad
x^{(0)} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}, \qquad \text{tolerancia} = 0.0001
$$

### Procedimiento

**Dominancia diagonal:**

- Renglón 1: $|3| > |-0.1| + |-0.2| = 0.3$ ✔
- Renglón 2: $|7| > |0.1| + |-0.3| = 0.4$ ✔
- Renglón 3: $|10| > |0.3| + |-0.2| = 0.5$ ✔

El sistema es diagonalmente dominante, por lo que ambos métodos convergen.

**Despejes:**

$$
x_1 = \frac{7.85 + 0.1x_2 + 0.2x_3}{3}, \qquad
x_2 = \frac{-19.3 - 0.1x_1 + 0.3x_3}{7}, \qquad
x_3 = \frac{71.4 - 0.3x_1 + 0.2x_2}{10}
$$

**Jacobi — primera iteración** (con $x^{(0)} = (0, 0, 0)$):

$$
x_1^{(1)} = \frac{7.85}{3} = 2.616667, \qquad
x_2^{(1)} = \frac{-19.3}{7} = -2.757143, \qquad
x_3^{(1)} = \frac{71.4}{10} = 7.14
$$

**Tabla de iteraciones — Jacobi:**

| k | $x_1$ | $x_2$ | $x_3$ | Error |
|---|---|---|---|---|
| 1 | 2.616667 | -2.757143 | 7.140000 | 7.140000 |
| 2 | 3.000762 | -2.488524 | 7.006357 | 0.384095 |
| 3 | 3.000806 | -2.499738 | 7.000207 | 0.011215 |
| 4 | 3.000022 | -2.500003 | 6.999981 | 0.000784 |
| 5 | 2.999999 | -2.500001 | 6.999999 | 0.000024 |

**Gauss-Seidel — primera iteración** (se usan los valores recién calculados):

$$
x_1^{(1)} = \frac{7.85}{3} = 2.616667, \qquad
x_2^{(1)} = \frac{-19.3 - 0.1(2.616667)}{7} = -2.794524, \qquad
x_3^{(1)} = \frac{71.4 - 0.3(2.616667) + 0.2(-2.794524)}{10} = 7.005610
$$

**Tabla de iteraciones — Gauss-Seidel:**

| k | $x_1$ | $x_2$ | $x_3$ | Error |
|---|---|---|---|---|
| 1 | 2.616667 | -2.794524 | 7.005610 | 7.005610 |
| 2 | 2.990557 | -2.499625 | 7.000291 | 0.373890 |
| 3 | 3.000032 | -2.499988 | 6.999999 | 0.009475 |
| 4 | 3.000000 | -2.500000 | 7.000000 | 0.000032 |

### Resultado

- **Jacobi:** converge en **5 iteraciones** con $x \approx (2.999999,\ -2.500001,\ 6.999999)$.
- **Gauss-Seidel:** converge en **4 iteraciones** con $x \approx (3.000000,\ -2.500000,\ 7.000000)$.
- Solución exacta: $x_1 = 3$, $x_2 = -2.5$, $x_3 = 7$.

La evidencia del trabajo original se encuentra en `evidencias/problema_original/`.

## 7. Alcance

La aplicación de consola permitirá:

1. Capturar un sistema de *n* ecuaciones con *n* incógnitas (2 ≤ *n* ≤ 10), validando cada dato.
2. Cargar el ejercicio original para comprobar los resultados.
3. Mostrar el sistema capturado y verificar si es diagonalmente dominante.
4. Resolver el sistema por el método de Jacobi.
5. Resolver el sistema por el método de Gauss-Seidel.
6. Mostrar la tabla de iteraciones, el resultado y la comprobación de la solución.
7. Salir del programa.

No forma parte del alcance: resolver sistemas no cuadrados, métodos directos (Gauss, Gauss-Jordan, LU) ni reordenar automáticamente las ecuaciones.

## 8. Comprobación de requisitos técnicos

| Requisito | Cómo se cumple |
|---|---|
| Problema trabajado en otra materia | Ejercicio de Análisis Numérico |
| Entradas, procesos y salidas identificables | Secciones 3, 4 y 5 |
| Reglas, validaciones o decisiones | Diagonal distinta de cero, dominancia diagonal, criterio de paro, convergencia/divergencia, rangos de *n*, tolerancia e iteraciones |
| Viable en consola con Python | Captura por teclado y resultados en texto/tablas |
| Al menos dos clases con responsabilidades diferentes | `SistemaEcuaciones` (datos y validación del sistema) y `MetodoIterativo` (aplicación de Jacobi y Gauss-Seidel) |
| Variables, operaciones, condiciones y ciclos | Sumas, restas, divisiones, valor absoluto; `if` para reglas; `for`/`while` para recorrer la matriz e iterar |
| Al menos una lista | Matriz de coeficientes, vector de independientes, solución y lista de iteraciones |
| Ejemplo original resuelto | Sección 6 |
| No es una operación sencilla con dos valores | Requiere matrices, ciclos anidados, criterio de paro y comparación de dos métodos |
