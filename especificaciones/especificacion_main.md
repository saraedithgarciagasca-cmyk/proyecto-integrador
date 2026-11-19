# Especificación del programa principal `main.py`

## 1. Objetivo

Presentar un menú de consola que permita capturar un sistema de ecuaciones, crear los objetos de las clases `SistemaEcuaciones` y `MetodoIterativo`, llamar a sus métodos y mostrar los resultados.

## 2. Importaciones

```python
from clases.sistema_ecuaciones import SistemaEcuaciones
from clases.metodo_iterativo import MetodoIterativo
```

## 3. Menú

```text
==============================================
  MÉTODOS ITERATIVOS: JACOBI Y GAUSS-SEIDEL
==============================================
1. Capturar sistema de ecuaciones
2. Cargar ejercicio original
3. Mostrar sistema y verificar dominancia diagonal
4. Resolver por el método de Jacobi
5. Resolver por el método de Gauss-Seidel
0. Salir
```

## 4. Variables del programa principal

| Variable | Tipo | Significado | Valor inicial |
|---|---|---|---|
| `sistema` | `SistemaEcuaciones` o `None` | Sistema actual con el que se trabaja | `None` |
| `opcion` | `int` | Opción elegida en el menú | — |

## 5. Funciones auxiliares de captura

| Función | Objetivo | Validación |
|---|---|---|
| `leer_entero(mensaje, minimo, maximo)` | Pedir un entero dentro de un rango | Repite la pregunta mientras el dato no sea entero o esté fuera del rango |
| `leer_real(mensaje)` | Pedir un número real | Repite la pregunta mientras el dato no sea numérico |
| `leer_real_positivo(mensaje)` | Pedir un número real mayor que 0 | Repite la pregunta mientras el dato no sea numérico o sea ≤ 0 |
| `capturar_sistema()` | Pedir `n`, la matriz y el vector; crear y devolver un objeto `SistemaEcuaciones` | Si el constructor lanza `ValueError`, mostrar el mensaje y devolver `None` |
| `cargar_ejercicio_original()` | Crear y devolver el `SistemaEcuaciones` del ejercicio original | — |
| `resolver(sistema, metodo)` | Pedir tolerancia e iteraciones, crear `MetodoIterativo` y llamar al método indicado | Si el sistema no es diagonalmente dominante, avisar antes de resolver |
| `main()` | Ciclo del menú | Opción entre 0 y 5 |

## 6. Objetos a crear

1. `SistemaEcuaciones(coeficientes, independientes)` en las opciones 1 y 2.
2. `MetodoIterativo(sistema, tolerancia, max_iteraciones)` en las opciones 4 y 5.

## 7. Métodos a llamar y secuencia de operaciones

| Opción | Secuencia |
|---|---|
| 1 | `capturar_sistema()` → `leer_entero` para `n` (2 a 10) → `leer_real` para cada coeficiente $a_{ij}$ y cada $b_i$ → `SistemaEcuaciones(...)` → si es válido, se guarda en `sistema` y se muestra `sistema.mostrar()`. |
| 2 | `cargar_ejercicio_original()` → `SistemaEcuaciones(...)` con los datos del ejercicio original → se guarda en `sistema` y se muestra `sistema.mostrar()`. |
| 3 | Si `sistema` es `None` → aviso. Si no: imprimir `sistema.mostrar()` y el resultado de `sistema.es_diagonalmente_dominante()`. |
| 4 | Si `sistema` es `None` → aviso. Si no: `resolver(sistema, "jacobi")` → `leer_real_positivo` para la tolerancia → `leer_entero` para iteraciones (1 a 1000) → `MetodoIterativo(...)` → `resolver_jacobi()` → imprimir `mostrar_tabla()` y `mostrar_resultado()`. |
| 5 | Igual que la opción 4, pero llamando a `resolver_gauss_seidel()`. |
| 0 | Mostrar mensaje de despedida y terminar. |

**Datos del ejercicio original (opción 2):**

```text
coeficientes = [[3, -0.1, -0.2],
                [0.1, 7, -0.3],
                [0.3, -0.2, 10]]
independientes = [7.85, -19.3, 71.4]
```

## 8. Condiciones de salida

- El menú se repite con un ciclo `while` hasta que el usuario elige la opción `0`.
- Las opciones 3, 4 y 5 no se ejecutan si aún no hay un sistema capturado o cargado; se muestra `"Primero capture o cargue un sistema (opciones 1 o 2)."` y se regresa al menú.
- Una opción fuera del rango 0–5 o no numérica se rechaza y se vuelve a pedir.
- El programa inicia llamando a `main()` dentro de `if __name__ == "__main__":`.
