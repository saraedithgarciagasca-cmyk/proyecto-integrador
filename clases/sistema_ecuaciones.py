"""Clase SistemaEcuaciones: representa un sistema de ecuaciones lineales A x = b."""


class SistemaEcuaciones:
    """Sistema de n ecuaciones lineales con n incógnitas."""

    def __init__(self, coeficientes, independientes):
        self.n = len(coeficientes)
        self.coeficientes = [[float(valor) for valor in fila] for fila in coeficientes]
        self.independientes = [float(valor) for valor in independientes]
        self.validar()

    def validar(self):
        """Comprueba que el sistema se pueda resolver con métodos iterativos."""
        if self.n < 2 or self.n > 10:
            raise ValueError("El sistema debe tener entre 2 y 10 ecuaciones.")

        for fila in self.coeficientes:
            if len(fila) != self.n:
                raise ValueError("La matriz de coeficientes debe ser cuadrada.")

        if len(self.independientes) != self.n:
            raise ValueError("El vector de términos independientes debe tener "
                             f"{self.n} elementos.")

        for i in range(self.n):
            if self.coeficientes[i][i] == 0:
                raise ValueError(f"El coeficiente de x{i + 1} en la ecuación {i + 1} "
                                 "(diagonal principal) no puede ser 0.")

    def es_diagonalmente_dominante(self):
        """Devuelve True si la matriz es estrictamente diagonalmente dominante."""
        for i in range(self.n):
            suma = 0.0
            for j in range(self.n):
                if j != i:
                    suma += abs(self.coeficientes[i][j])
            if abs(self.coeficientes[i][i]) <= suma:
                return False
        return True

    def mostrar(self):
        """Devuelve el sistema en forma de ecuaciones, una por línea."""
        lineas = []
        for i in range(self.n):
            ecuacion = ""
            for j in range(self.n):
                valor = self.coeficientes[i][j]
                texto = f"{abs(valor):g}x{j + 1}"
                if j == 0:
                    ecuacion += ("-" if valor < 0 else "") + texto
                else:
                    ecuacion += (" - " if valor < 0 else " + ") + texto
            ecuacion += f" = {self.independientes[i]:g}"
            lineas.append(ecuacion)
        return "\n".join(lineas)

    def comprobar_solucion(self, solucion):
        """Sustituye la solución en cada ecuación y devuelve el lado izquierdo."""
        if len(solucion) != self.n:
            raise ValueError(f"La solución debe tener {self.n} valores.")

        resultados = []
        for i in range(self.n):
            suma = 0.0
            for j in range(self.n):
                suma += self.coeficientes[i][j] * solucion[j]
            resultados.append(suma)
        return resultados
