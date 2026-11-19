# Solución de sistemas de ecuaciones lineales por métodos iterativos (Jacobi y Gauss-Seidel)

Proyecto Integrador — Programación II · Universidad Iberoamericana

**Alumna:** Sara García

## Descripción

Aplicación de consola en Python que resuelve sistemas de *n* ecuaciones lineales con *n* incógnitas ($A\,x = b$) mediante los métodos iterativos de **Jacobi** y **Gauss-Seidel**. El programa valida el sistema, verifica la dominancia diagonal, muestra la tabla de iteraciones con el error de cada una, indica si el método convergió y comprueba la solución sustituyéndola en las ecuaciones.

## Asignatura original

Análisis Numérico.

## Objetivo

Automatizar la solución de sistemas de ecuaciones lineales por Jacobi y Gauss-Seidel, aplicando los conocimientos de Programación II (variables, operaciones, decisiones, ciclos, listas, funciones, clases, atributos, constructores, métodos y objetos), y comprobar que los resultados coinciden con el ejercicio resuelto en Análisis Numérico.

## Funcionalidades

1. Capturar un sistema de 2 a 10 ecuaciones con validación de cada dato.
2. Cargar el ejercicio original de Análisis Numérico.
3. Mostrar el sistema y verificar si es diagonalmente dominante.
4. Resolver por el método de Jacobi.
5. Resolver por el método de Gauss-Seidel.
6. Mostrar la tabla de iteraciones, el resultado (convergió / no convergió / diverge) y la comprobación de la solución.

## Clases

| Clase | Archivo | Responsabilidad |
|---|---|---|
| `SistemaEcuaciones` | `clases/sistema_ecuaciones.py` | Guarda la matriz de coeficientes y el vector de términos independientes; valida el sistema, verifica la dominancia diagonal, lo muestra en forma de ecuaciones y comprueba una solución. |
| `MetodoIterativo` | `clases/metodo_iterativo.py` | Recibe un objeto `SistemaEcuaciones` y lo resuelve por Jacobi o Gauss-Seidel; calcula el error, aplica el criterio de paro, guarda la lista de iteraciones y presenta la tabla y el resultado. |

Las especificaciones de cada clase y del programa principal están en `especificaciones/`.

## Estructura del repositorio

```text
proyecto-integrador/
├── README.md
├── .gitignore
├── requirements.txt
├── main.py
├── clases/
│   ├── __init__.py
│   ├── sistema_ecuaciones.py
│   └── metodo_iterativo.py
├── especificaciones/
│   ├── especificacion_sistema_ecuaciones.md
│   ├── especificacion_metodo_iterativo.md
│   └── especificacion_main.md
├── documentacion/
│   ├── 01_analisis_problema.md
│   ├── 02_pruebas.md
│   └── 03_uso_copilot.md
└── evidencias/
    ├── problema_original/
    └── ejecuciones/
```

## Requisitos

- Python 3.10 o superior.
- No requiere dependencias externas (solo la biblioteca estándar).
- Herramientas utilizadas: Visual Studio Code, Git, GitHub y GitHub Copilot.

## Instalación

```bash
git clone https://github.com/Saraedithgarciagasca-CMYK/proyecto-integrador.git
cd proyecto-integrador
python -m venv .venv
```

Activar el entorno virtual:

- Windows: `.venv\Scripts\activate`
- macOS / Linux: `source .venv/bin/activate`

Instalar dependencias (el archivo no contiene dependencias externas):

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

## Ejemplo

Ejercicio original (opción 2 del menú) resuelto por Gauss-Seidel con tolerancia 0.0001:

```text
3x1 - 0.1x2 - 0.2x3 = 7.85
0.1x1 + 7x2 - 0.3x3 = -19.3
0.3x1 - 0.2x2 + 10x3 = 71.4

Tabla de iteraciones - Gauss-Seidel
   k             x1             x2             x3          Error
----------------------------------------------------------------
   1       2.616667      -2.794524       7.005610       7.005610
   2       2.990557      -2.499625       7.000291       0.373890
   3       3.000032      -2.499988       6.999999       0.009475
   4       3.000000      -2.500000       7.000000       0.000032

Método: Gauss-Seidel
Convergió en 4 iteraciones (tolerancia = 0.0001).
Solución aproximada:
  x1 = 3.000000
  x2 = -2.500000
  x3 = 7.000000
```

## Pruebas

Los cinco casos de prueba (caso original, caso normal, caso límite, entrada inválida y regla de dominancia diagonal), con resultados esperados y obtenidos, están en [`documentacion/02_pruebas.md`](documentacion/02_pruebas.md). Las capturas están en `evidencias/ejecuciones/`.

## Documentación

- [Análisis del problema](documentacion/01_analisis_problema.md)
- [Pruebas y validación](documentacion/02_pruebas.md)
- [Uso de GitHub Copilot](documentacion/03_uso_copilot.md)
