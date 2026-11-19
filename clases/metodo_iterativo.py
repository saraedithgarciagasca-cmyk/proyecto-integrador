"""Clase MetodoIterativo: resuelve un SistemaEcuaciones por Jacobi o Gauss-Seidel."""

import math


class MetodoIterativo:
    """Aplica los métodos iterativos de Jacobi y Gauss-Seidel a un sistema."""

    def __init__(self, sistema, tolerancia=0.0001, max_iteraciones=100):
        if tolerancia <= 0:
            raise ValueError("La tolerancia debe ser mayor que 0.")
        if max_iteraciones < 1 or max_iteraciones > 1000:
            raise ValueError("Las iteraciones máximas deben estar entre 1 y 1000.")

        self.sistema = sistema
        self.tolerancia = tolerancia
        self.max_iteraciones = max_iteraciones
        self.nombre_metodo = ""
        self.iteraciones = []
        self.solucion = []
        self.convergio = False
        self.diverge = False

    def resolver_jacobi(self):
        """Resuelve el sistema usando solo los valores de la iteración anterior."""
        self._reiniciar("Jacobi")
        n = self.sistema.n
        a = self.sistema.coeficientes
        b = self.sistema.independientes
        anterior = [0.0] * n

        for k in range(1, self.max_iteraciones + 1):
            nuevo = [0.0] * n
            for i in range(n):
                suma = 0.0
                for j in range(n):
                    if j != i:
                        suma += a[i][j] * anterior[j]
                nuevo[i] = (b[i] - suma) / a[i][i]

            error = self._calcular_error(nuevo, anterior)
            self.iteraciones.append({"k": k, "x": nuevo, "error": error})
            self.solucion = nuevo

            if not all(math.isfinite(valor) for valor in nuevo):
                self.diverge = True
                break
            if error < self.tolerancia:
                self.convergio = True
                break
            anterior = nuevo

        return self.solucion

    def resolver_gauss_seidel(self):
        """Resuelve el sistema usando los valores más recientes disponibles."""
        self._reiniciar("Gauss-Seidel")
        n = self.sistema.n
        a = self.sistema.coeficientes
        b = self.sistema.independientes
        anterior = [0.0] * n

        for k in range(1, self.max_iteraciones + 1):
            nuevo = anterior.copy()
            for i in range(n):
                suma = 0.0
                for j in range(n):
                    if j != i:
                        suma += a[i][j] * nuevo[j]
                nuevo[i] = (b[i] - suma) / a[i][i]

            error = self._calcular_error(nuevo, anterior)
            self.iteraciones.append({"k": k, "x": nuevo, "error": error})
            self.solucion = nuevo

            if not all(math.isfinite(valor) for valor in nuevo):
                self.diverge = True
                break
            if error < self.tolerancia:
                self.convergio = True
                break
            anterior = nuevo

        return self.solucion

    def _reiniciar(self, nombre):
        """Deja el objeto listo para una nueva resolución."""
        self.nombre_metodo = nombre
        self.iteraciones = []
        self.solucion = []
        self.convergio = False
        self.diverge = False

    def _calcular_error(self, nuevo, anterior):
        """Error absoluto máximo entre dos aproximaciones consecutivas."""
        error = 0.0
        for i in range(len(nuevo)):
            diferencia = abs(nuevo[i] - anterior[i])
            if diferencia > error:
                error = diferencia
        return error

    def mostrar_tabla(self):
        """Devuelve la tabla de iteraciones como texto."""
        if not self.iteraciones:
            return "No se ha resuelto el sistema."

        n = self.sistema.n
        encabezado = f"{'k':>4}"
        for i in range(n):
            encabezado += f"{'x' + str(i + 1):>14}"
        encabezado += f"{'Error':>14}"

        lineas = [f"Tabla de iteraciones - {self.nombre_metodo}",
                  encabezado, "-" * len(encabezado)]
        for registro in self.iteraciones:
            linea = f"{registro['k']:>4}"
            for valor in registro["x"]:
                linea += f"{valor:>14.6f}"
            linea += f"{registro['error']:>14.6f}"
            lineas.append(linea)
        return "\n".join(lineas)

    def mostrar_resultado(self):
        """Devuelve el resumen del resultado y la comprobación de la solución."""
        if not self.iteraciones:
            return "No se ha resuelto el sistema."

        total = len(self.iteraciones)
        lineas = [f"Método: {self.nombre_metodo}"]
        if self.diverge:
            lineas.append(f"El método diverge (valores no finitos en la iteración {total}).")
        elif self.convergio:
            lineas.append(f"Convergió en {total} iteraciones "
                          f"(tolerancia = {self.tolerancia:g}).")
        else:
            lineas.append(f"No convergió en {self.max_iteraciones} iteraciones "
                          f"(tolerancia = {self.tolerancia:g}).")

        lineas.append("Solución aproximada:")
        for i in range(self.sistema.n):
            lineas.append(f"  x{i + 1} = {self.solucion[i]:.6f}")

        if not self.diverge:
            lineas.append("Comprobación (ecuación evaluada vs. término independiente):")
            resultados = self.sistema.comprobar_solucion(self.solucion)
            for i in range(self.sistema.n):
                lineas.append(f"  Ecuación {i + 1}: {resultados[i]:.6f}  vs.  "
                              f"{self.sistema.independientes[i]:g}")
        return "\n".join(lineas)
