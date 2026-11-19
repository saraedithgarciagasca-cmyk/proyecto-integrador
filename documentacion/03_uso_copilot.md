# 03. Uso de GitHub Copilot

## 1. ¿Cómo utilicé las especificaciones para solicitar código a Copilot?

Primero hice los archivos de especificación: uno para cada clase (`especificacion_sistema_ecuaciones.md` y `especificacion_metodo_iterativo.md`) y otro para `main.py`. Ahí puse qué atributos lleva cada clase, qué recibe el `__init__`, qué hace cada método paso a paso y qué reglas no se podían cambiar.

Ya con eso, abría en VS Code la especificación de una sola clase y le pedía a Copilot Chat que la programara tal cual decía el archivo. Empecé con `SistemaEcuaciones` porque la otra clase la necesita. Hasta que esa quedó bien y la probé, me pasé a `MetodoIterativo`. Luego hice el menú de `main.py` y al final conecté las clases con el menú. Nunca le pedí todo el programa de un jalón.

## 2. ¿Qué revisé o modifiqué del código generado?

- Comparé los nombres de los atributos y métodos con los de la especificación para ver que fueran los mismos. En `MetodoIterativo` me salió un método extra que yo no había pedido (uno que guardaba la iteración y revisaba si ya se tenía que detener). Lo quité y dejé eso dentro de `resolver_jacobi()` y `resolver_gauss_seidel()`, que es como lo tenía en la especificación.
- Revisé las reglas: que la dominancia diagonal usara `>` y no `>=`, que se detuviera cuando `error < tolerancia` y que empezara con puros ceros.
- Me fijé que las clases no tuvieran `input()` ni `print()`, porque eso le toca a `main.py`.
- En las pruebas vi que cuando los números salían muy grandes las columnas de la tabla se pegaban y no se leía nada. Le agregué un espacio antes de cada columna y ya quedó (está en el CP-05 de `02_pruebas.md`).

## 3. ¿Copilot generó una respuesta incorrecta o distinta de lo solicitado?

Sí, lo del método extra que no estaba en la especificación (lo del punto anterior). No estaba mal, pero no era lo que yo había pedido.

Lo que más cuidé fue la diferencia entre Jacobi y Gauss-Seidel, porque el código de los dos es casi igual y es muy fácil confundirlos:

- En **Jacobi** la suma tiene que usar `anterior[j]` y la lista `nuevo` empieza en ceros.
- En **Gauss-Seidel** la lista `nuevo` empieza como copia de `anterior` y la suma usa `nuevo[j]`, para ir usando los valores que ya se calcularon en esa misma vuelta.

Si eso se cruza, el programa no marca ningún error y hasta converge, pero salen otras iteraciones y otros números. Por eso comparé las tablas del programa con las de mi libreta: Jacobi tenía que dar 5 iteraciones y Gauss-Seidel 4, con los mismos valores en cada fila.

## 4. ¿Cómo comprobé el funcionamiento de clases y métodos?

1. Probé cada clase sola antes de seguir con la otra. Desde la terminal de Python creé el sistema del ejercicio original y revisé que `mostrar()` sacara bien las ecuaciones, que `es_diagonalmente_dominante()` diera `True`, que `comprobar_solucion([3, -2.5, 7])` regresara `[7.85, -19.3, 71.4]` y que si ponía un cero en la diagonal me saliera el `ValueError`.
2. Comparé las tablas de Jacobi y Gauss-Seidel con las que hice en Análisis Numérico, fila por fila.
3. Hice los cinco casos de `02_pruebas.md` (el original, uno de 4 × 4, el caso límite, entradas inválidas y un sistema que no es diagonalmente dominante). Antes de correr cada uno anoté qué esperaba que saliera.
4. Usé la comprobación que hace el mismo programa: al sustituir la solución, cada ecuación tiene que dar casi lo mismo que su término independiente.

## 5. ¿Qué ventajas y limitaciones observé?

**Ventajas**

- Te ahorra mucho tiempo en lo repetitivo, como los ciclos, el formato de la tabla y las validaciones de lo que escribe el usuario.
- Si la especificación está clara, casi siempre respeta los nombres que le pones.
- Ayuda con los mensajes de error y los comentarios.

**Limitaciones**

- No sabe las reglas del problema si no se las dices, y te puede dar algo que corre pero con el método mal hecho.
- A veces mete cosas que no le pediste, así que hay que revisar todo contra la especificación.
- No comprueba si los resultados están bien; eso lo tienes que hacer tú con datos que ya conoces.

## 6. ¿Por qué es necesario comprender el código producido con ayuda de IA?

Porque al final la responsable del programa soy yo, no Copilot. Si se confunden Jacobi y Gauss-Seidel, el programa no truena: da números que parecen correctos y no lo son. La única forma de darte cuenta es entendiendo el método y el código. Además, tengo que poder explicar cada clase, atributo, método y objeto, hacer cambios si me los piden y arreglar lo que salga mal en las pruebas. Si copio código que no entiendo, no puedo estar segura de que de verdad resuelve el problema que vi en Análisis Numérico.
