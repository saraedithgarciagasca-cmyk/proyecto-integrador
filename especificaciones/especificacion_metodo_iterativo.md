# Especificación de la clase `MetodoIterativo`

**Archivo:** `clases/metodo_iterativo.py`

## 1. Identificación

| Campo | Descripción |
|---|---|
| Nombre | `MetodoIterativo` |
| Objetivo | Resolver un objeto `SistemaEcuaciones` por los métodos de Jacobi o Gauss-Seidel. |
| Responsabilidad | Aplicar las fórmulas iterativas, calcular el error de cada iteración, aplicar el criterio de paro, guardar la tabla de iteraciones y presentar el resultado. **No** captura ni valida la matriz (eso corresponde a `SistemaEcuaciones`). |

## 2. Atributos

| Nombre | Tipo | Significado | Valor inicial |
|---|---|---|---|
| `self.sistema` | `SistemaEcuaciones` | Sistema que se va a resolver | Objeto recibido |
| `self.tolerancia` | `float` | Error máximo aceptado | Valor recibido (por omisión `0.0001`) |
| `self.max_iteraciones` | `int` | Límite de iteraciones | Valor recibido (por omisión `100`) |
| `self.nombre_metodo` | `str` | Método aplicado en la última resolución | `""` |
| `self.iteraciones` | `list` de `dict` | Registro de cada iteración: `{"k": int, "x": list, "error": float}` | `[]` |
| `self.solucion` | `list` de `float` | Última aproximación obtenida | `[]` |
| `self.convergio` | `bool` | Indica si se alcanzó la tolerancia | `False` |
| `self.diverge` | `bool` | Indica si los valores dejaron de ser finitos | `False` |

## 3. Constructor `__init__`

```text
__init__(self, sistema, tolerancia=0.0001, max_iteraciones=100)
```

- **Recibe:** el objeto `sistema`, la `tolerancia` y el `max_iteraciones`.
- **Inicializa:**
  1. Si `tolerancia <= 0` → `ValueError`.
  2. Si `max_iteraciones < 1` o `max_iteraciones > 1000` → `ValueError`.
  3. Asigna `self.sistema`, `self.tolerancia`, `self.max_iteraciones`.
  4. Asigna los valores iniciales de `nombre_metodo`, `iteraciones`, `solucion`, `convergio` y `diverge` indicados en la tabla de atributos.

## 4. Métodos

### 4.1 `resolver_jacobi(self)`

| Campo | Descripción |
|---|---|
| Objetivo | Resolver el sistema por el método de Jacobi. |
| Entradas | Ninguna. |
| Atributos utilizados | `sistema`, `tolerancia`, `max_iteraciones`, `nombre_metodo`, `iteraciones`, `solucion`, `convergio`, `diverge` |
| Algoritmo | 1. Llamar a `_reiniciar("Jacobi")`. 2. `anterior` = lista de *n* ceros. 3. Para `k` de 1 a `max_iteraciones`: a) crear `nuevo` de *n* ceros; b) para cada `i`: `suma` = Σ $a_{ij}$ · `anterior[j]` con `j ≠ i`; `nuevo[i]` = ($b_i$ − `suma`) / $a_{ii}$; c) `error` = `_calcular_error(nuevo, anterior)`; d) guardar `{"k": k, "x": nuevo, "error": error}` en `iteraciones`; e) `solucion` = `nuevo`; f) si algún valor no es finito → `diverge = True` y terminar; g) si `error < tolerancia` → `convergio = True` y terminar; h) `anterior` = `nuevo`. |
| Resultado | Devuelve `self.solucion`. |
| Validaciones | Detección de divergencia con `math.isfinite`. |

$$
x_i^{(k)} = \frac{b_i - \displaystyle\sum_{j \neq i} a_{ij}\, x_j^{(k-1)}}{a_{ii}}
$$

### 4.2 `resolver_gauss_seidel(self)`

| Campo | Descripción |
|---|---|
| Objetivo | Resolver el sistema por el método de Gauss-Seidel. |
| Entradas | Ninguna. |
| Atributos utilizados | Los mismos que `resolver_jacobi`. |
| Algoritmo | Igual que Jacobi, con una diferencia: `nuevo` inicia como **copia** de `anterior` y la suma usa `nuevo[j]` para todos los `j ≠ i`, de modo que los valores ya calculados en la iteración actual se aprovechan de inmediato. |
| Resultado | Devuelve `self.solucion`. |
| Validaciones | Detección de divergencia con `math.isfinite`. |

$$
x_i^{(k)} = \frac{b_i - \displaystyle\sum_{j < i} a_{ij}\, x_j^{(k)} - \sum_{j > i} a_{ij}\, x_j^{(k-1)}}{a_{ii}}
$$

### 4.3 `_reiniciar(self, nombre)`

| Campo | Descripción |
|---|---|
| Objetivo | Dejar el objeto listo para una nueva resolución. |
| Entradas | `nombre`: `str` con el nombre del método. |
| Atributos utilizados | `nombre_metodo`, `iteraciones`, `solucion`, `convergio`, `diverge` |
| Algoritmo | Asignar `nombre_metodo = nombre`, `iteraciones = []`, `solucion = []`, `convergio = False`, `diverge = False`. |
| Resultado | Ninguno. |
| Validaciones | Ninguna. |

### 4.4 `_calcular_error(self, nuevo, anterior)`

| Campo | Descripción |
|---|---|
| Objetivo | Calcular el error absoluto máximo entre dos aproximaciones. |
| Entradas | `nuevo`, `anterior`: listas de *n* números. |
| Atributos utilizados | Ninguno. |
| Algoritmo | Devolver el máximo de `abs(nuevo[i] - anterior[i])` para cada `i`. |
| Resultado | `float` |
| Validaciones | Ninguna. |

$$
E^{(k)} = \max_{i} \left| x_i^{(k)} - x_i^{(k-1)} \right|
$$

### 4.5 `mostrar_tabla(self)`

| Campo | Descripción |
|---|---|
| Objetivo | Construir la tabla de iteraciones. |
| Entradas | Ninguna. |
| Atributos utilizados | `iteraciones`, `sistema.n` |
| Algoritmo | Si `iteraciones` está vacía → devolver `"No se ha resuelto el sistema."`. Si no, armar un encabezado `k, x1, ..., xn, Error` y una línea por iteración con los valores redondeados a 6 decimales. Cada columna va precedida por un espacio fijo para que las columnas no se peguen cuando los números son muy grandes. |
| Resultado | `str` |
| Validaciones | Lista vacía. |

### 4.6 `mostrar_resultado(self)`

| Campo | Descripción |
|---|---|
| Objetivo | Construir el resumen del resultado y la comprobación. |
| Entradas | Ninguna. |
| Atributos utilizados | `nombre_metodo`, `iteraciones`, `solucion`, `convergio`, `diverge`, `tolerancia`, `sistema` |
| Algoritmo | Si `iteraciones` está vacía → devolver `"No se ha resuelto el sistema."`. Indicar el método; según `diverge` / `convergio` escribir "El método diverge", "Convergió en k iteraciones" o "No convergió en max_iteraciones iteraciones"; listar `x1 ... xn` con 6 decimales. Si no diverge, llamar a `sistema.comprobar_solucion(solucion)` y mostrar, para cada ecuación, el valor obtenido y el término independiente. |
| Resultado | `str` |
| Validaciones | Lista vacía; no comprobar cuando diverge. |

## 5. Reglas que Copilot no puede alterar

1. El vector inicial siempre es de ceros.
2. En **Jacobi** solo se usan valores de la iteración anterior; en **Gauss-Seidel** se usan los valores más recientes. No se deben mezclar.
3. El error es el **error absoluto máximo** entre dos iteraciones consecutivas.
4. El criterio de paro es `error < tolerancia` (estrictamente menor).
5. La tolerancia debe ser mayor que 0 y las iteraciones máximas entre 1 y 1000.
6. Si algún valor deja de ser finito, se detiene y se marca como divergente.
7. Cada iteración se guarda en la lista `iteraciones`, aunque el método no converja.
8. La clase no pide datos por teclado ni imprime; devuelve valores o texto.
