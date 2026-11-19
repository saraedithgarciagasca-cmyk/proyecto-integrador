# Especificación de la clase `SistemaEcuaciones`

**Archivo:** `clases/sistema_ecuaciones.py`

## 1. Identificación

| Campo | Descripción |
|---|---|
| Nombre | `SistemaEcuaciones` |
| Objetivo | Representar un sistema de *n* ecuaciones lineales con *n* incógnitas de la forma $A\,x = b$. |
| Responsabilidad | Guardar la matriz de coeficientes y el vector de términos independientes, validar que el sistema se pueda resolver con métodos iterativos, verificar la dominancia diagonal, mostrar el sistema en forma de ecuaciones y comprobar una solución. **No** aplica los métodos de Jacobi ni Gauss-Seidel. |

## 2. Atributos

| Nombre | Tipo | Significado | Valor inicial |
|---|---|---|---|
| `self.n` | `int` | Número de ecuaciones e incógnitas | Número de renglones de `coeficientes` |
| `self.coeficientes` | `list` de `list` de `float` | Matriz $A$ de *n* × *n* | Copia de la matriz recibida, convertida a `float` |
| `self.independientes` | `list` de `float` | Vector $b$ de *n* elementos | Copia del vector recibido, convertida a `float` |

## 3. Constructor `__init__`

```text
__init__(self, coeficientes, independientes)
```

- **Recibe:**
  - `coeficientes`: lista de listas de números (matriz *n* × *n*).
  - `independientes`: lista de números (*n* elementos).
- **Inicializa:**
  1. `self.n` con `len(coeficientes)`.
  2. `self.coeficientes` con una copia de cada renglón convertida a `float`.
  3. `self.independientes` con una copia convertida a `float`.
  4. Llama a `self.validar()`; si el sistema no es válido se lanza `ValueError` y el objeto no se crea.

## 4. Métodos

### 4.1 `validar(self)`

| Campo | Descripción |
|---|---|
| Objetivo | Comprobar que el sistema cumple las condiciones para aplicar métodos iterativos. |
| Entradas | Ninguna (usa atributos). |
| Atributos utilizados | `n`, `coeficientes`, `independientes` |
| Algoritmo | 1. Si `n` < 2 o `n` > 10 → `ValueError`. 2. Para cada renglón: si su longitud ≠ `n` → `ValueError`. 3. Si `len(independientes)` ≠ `n` → `ValueError`. 4. Para cada `i`: si `coeficientes[i][i] == 0` → `ValueError` indicando la ecuación. |
| Resultado | No devuelve valor; termina sin error si el sistema es válido. |
| Validaciones | Tamaño entre 2 y 10, matriz cuadrada, vector del mismo tamaño, diagonal sin ceros. |

### 4.2 `es_diagonalmente_dominante(self)`

| Campo | Descripción |
|---|---|
| Objetivo | Determinar si la matriz es estrictamente diagonalmente dominante por renglones. |
| Entradas | Ninguna. |
| Atributos utilizados | `n`, `coeficientes` |
| Algoritmo | Para cada renglón `i`: calcular `suma` = suma de `abs(coeficientes[i][j])` para `j ≠ i`. Si `abs(coeficientes[i][i]) <= suma` → devolver `False`. Al terminar el ciclo → devolver `True`. |
| Resultado | `bool` |
| Validaciones | Ninguna adicional (el sistema ya fue validado en el constructor). |

### 4.3 `mostrar(self)`

| Campo | Descripción |
|---|---|
| Objetivo | Construir el texto del sistema en forma de ecuaciones. |
| Entradas | Ninguna. |
| Atributos utilizados | `n`, `coeficientes`, `independientes` |
| Algoritmo | Para cada renglón `i`, armar una línea con cada término `coeficiente·x_j` (con su signo `+` o `-`) seguida de `= independientes[i]`. Unir las líneas con saltos de línea. |
| Resultado | `str` con una ecuación por línea, por ejemplo: `3x1 - 0.1x2 - 0.2x3 = 7.85` |
| Validaciones | Ninguna. |

### 4.4 `comprobar_solucion(self, solucion)`

| Campo | Descripción |
|---|---|
| Objetivo | Sustituir una solución en cada ecuación para verificarla. |
| Entradas | `solucion`: lista de *n* números. |
| Atributos utilizados | `n`, `coeficientes` |
| Algoritmo | Para cada renglón `i`, calcular `suma` = Σ `coeficientes[i][j] * solucion[j]` y agregarla a una lista `resultados`. |
| Resultado | `list` de `float` con el valor del lado izquierdo de cada ecuación. |
| Validaciones | Si `len(solucion)` ≠ `n` → `ValueError`. |

## 5. Reglas que Copilot no puede alterar

1. El tamaño del sistema debe estar entre 2 y 10.
2. La matriz debe ser cuadrada y el vector $b$ debe tener el mismo tamaño.
3. Ningún elemento de la diagonal principal puede ser 0; se rechaza con `ValueError`.
4. La dominancia diagonal es **estricta**: se usa `>` y no `>=`.
5. La clase no pide datos por teclado ni imprime; solo devuelve valores o texto. La captura se hace en `main.py`.
6. Los datos recibidos se copian; la clase no modifica las listas originales.
