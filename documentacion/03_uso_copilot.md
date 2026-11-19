# 03. Uso de GitHub Copilot

## 1. ¿Cómo utilicé las especificaciones para solicitar código a Copilot?

Antes de escribir código redacté un archivo Markdown por clase (`especificacion_sistema_ecuaciones.md` y `especificacion_metodo_iterativo.md`) y otro para el programa principal (`especificacion_main.md`). En cada uno definí atributos con su tipo y valor inicial, lo que recibe `__init__`, el algoritmo de cada método y las reglas que no se podían cambiar.

Para pedir el código abrí la especificación de **una sola clase** en VS Code y le pedí a Copilot Chat que implementara esa clase siguiendo exactamente el archivo. Empecé por `SistemaEcuaciones`, porque `MetodoIterativo` depende de ella. Cuando la primera clase quedó revisada y probada, pasé a la segunda. Después hice el menú de `main.py` con las funciones de captura y, al final, integré las clases en las opciones del menú. Así nunca le pedí a Copilot toda la aplicación de una vez.

## 2. ¿Qué revisé o modifiqué del código generado?

- **Correspondencia con la especificación:** comparé nombre por nombre los atributos y métodos con los de la especificación. En `MetodoIterativo` se había agregado un método auxiliar que no estaba especificado para guardar la iteración y revisar el criterio de paro; lo quité y dejé esa lógica dentro de `resolver_jacobi()` y `resolver_gauss_seidel()`, como dice el algoritmo de la especificación.
- **Reglas:** revisé que la dominancia diagonal usara `>` estricto, que el criterio de paro fuera `error < tolerancia` y que el vector inicial fuera de ceros.
- **Separación de responsabilidades:** verifiqué que las clases no usaran `input()` ni `print()`; toda la captura y la impresión quedaron en `main.py`.
- **Formato de la tabla:** en las pruebas encontré que las columnas se pegaban con números muy grandes y agregué un espacio fijo antes de cada columna (ver CP-05 en `02_pruebas.md`).

## 3. ¿Copilot generó una respuesta incorrecta o distinta de lo solicitado?

Sí. Además del método auxiliar que no estaba en la especificación (punto anterior), el detalle más importante fue la diferencia entre Jacobi y Gauss-Seidel. Los dos métodos tienen casi el mismo código, y la única diferencia es de qué lista se toman los valores para la suma:

- En **Jacobi** la suma debe usar `anterior[j]` y la lista `nuevo` debe empezar en ceros.
- En **Gauss-Seidel** la lista `nuevo` debe empezar como **copia** de `anterior` y la suma debe usar `nuevo[j]`, para aprovechar los valores ya calculados en la misma iteración.

Si se mezclan, el programa sigue funcionando y converge, pero da otro número de iteraciones y otros valores en la tabla. Lo detecté porque comparé la tabla del programa con la del ejercicio original: Jacobi debe dar 5 iteraciones y Gauss-Seidel 4, con valores específicos en cada fila. Revisé esas dos líneas en cada método hasta que las tablas coincidieron exactamente.

## 4. ¿Cómo comprobé el funcionamiento de clases y métodos?

1. **Cada clase por separado**, antes de continuar con la siguiente: creé objetos desde la terminal de Python y llamé a sus métodos. Por ejemplo, creé el `SistemaEcuaciones` del ejercicio original y comprobé que `mostrar()` imprimiera las ecuaciones, que `es_diagonalmente_dominante()` devolviera `True`, que `comprobar_solucion([3, -2.5, 7])` devolviera `[7.85, -19.3, 71.4]` y que un sistema con cero en la diagonal lanzara `ValueError`.
2. **Con el ejercicio original:** comparé fila por fila las tablas de Jacobi y Gauss-Seidel con las que resolví en Análisis Numérico.
3. **Con los cinco casos de prueba** de `02_pruebas.md` (caso normal de 4 × 4, caso límite, entradas inválidas y sistema no diagonalmente dominante), anotando el resultado esperado antes de ejecutar.
4. **Con la comprobación del propio programa:** al sustituir la solución, cada ecuación debe dar un valor casi igual a su término independiente.

## 5. ¿Qué ventajas y limitaciones observé?

**Ventajas**

- Ahorra tiempo en la parte repetitiva: ciclos anidados, formato de la tabla y funciones de validación de entradas.
- Con una especificación clara genera código que casi siempre respeta los nombres de atributos y métodos.
- Ayuda a escribir los mensajes de error y los comentarios de documentación.

**Limitaciones**

- No conoce las reglas del problema si no se las escribo; puede generar algo que "funciona" pero con un método numérico equivocado.
- A veces agrega cosas que no se pidieron (métodos o validaciones de más), por lo que hay que revisar todo contra la especificación.
- No prueba sus resultados: la verificación con datos conocidos la tengo que hacer yo.

## 6. ¿Por qué es necesario comprender el código producido con ayuda de IA?

Porque yo soy responsable del resultado. Un error como mezclar Jacobi con Gauss-Seidel no produce ningún mensaje de error: el programa da números que parecen correctos, pero no lo son. Solo comprendiendo el método y el código se puede detectar. Además, necesito poder explicar cada clase, atributo, método y objeto, modificar el programa si cambian los requisitos y corregir errores cuando aparecen en las pruebas. Si acepto código que no entiendo, no puedo garantizar que resuelva el problema que estudié en Análisis Numérico.
