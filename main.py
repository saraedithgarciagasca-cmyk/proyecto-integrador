"""Programa principal: menú de consola para los métodos de Jacobi y Gauss-Seidel."""

from clases.sistema_ecuaciones import SistemaEcuaciones
from clases.metodo_iterativo import MetodoIterativo


def leer_entero(mensaje, minimo, maximo):
    """Pide un entero dentro del rango [minimo, maximo]."""
    while True:
        texto = input(mensaje)
        try:
            valor = int(texto)
        except ValueError:
            print("  Error: debe escribir un número entero.")
            continue
        if valor < minimo or valor > maximo:
            print(f"  Error: el valor debe estar entre {minimo} y {maximo}.")
            continue
        return valor


def leer_real(mensaje):
    """Pide un número real."""
    while True:
        texto = input(mensaje)
        try:
            return float(texto)
        except ValueError:
            print("  Error: debe escribir un número.")


def leer_real_positivo(mensaje):
    """Pide un número real mayor que 0."""
    while True:
        valor = leer_real(mensaje)
        if valor <= 0:
            print("  Error: el valor debe ser mayor que 0.")
            continue
        return valor


def capturar_sistema():
    """Pide n, la matriz de coeficientes y el vector de independientes."""
    n = leer_entero("Número de ecuaciones e incógnitas (2 a 10): ", 2, 10)
    coeficientes = []
    independientes = []
    for i in range(n):
        print(f"Ecuación {i + 1}:")
        fila = []
        for j in range(n):
            fila.append(leer_real(f"  Coeficiente de x{j + 1}: "))
        coeficientes.append(fila)
        independientes.append(leer_real("  Término independiente: "))

    try:
        return SistemaEcuaciones(coeficientes, independientes)
    except ValueError as error:
        print(f"  Error: {error}")
        return None


def cargar_ejercicio_original():
    """Crea el sistema del ejercicio original de Análisis Numérico."""
    coeficientes = [[3, -0.1, -0.2],
                    [0.1, 7, -0.3],
                    [0.3, -0.2, 10]]
    independientes = [7.85, -19.3, 71.4]
    return SistemaEcuaciones(coeficientes, independientes)


def resolver(sistema, metodo):
    """Pide tolerancia e iteraciones, crea el MetodoIterativo y resuelve."""
    if not sistema.es_diagonalmente_dominante():
        print("Aviso: el sistema NO es diagonalmente dominante; "
              "el método puede no converger.")

    tolerancia = leer_real_positivo("Tolerancia (por ejemplo 0.0001): ")
    max_iteraciones = leer_entero("Iteraciones máximas (1 a 1000): ", 1, 1000)
    resolvedor = MetodoIterativo(sistema, tolerancia, max_iteraciones)

    if metodo == "jacobi":
        resolvedor.resolver_jacobi()
    else:
        resolvedor.resolver_gauss_seidel()

    print()
    print(resolvedor.mostrar_tabla())
    print()
    print(resolvedor.mostrar_resultado())


def mostrar_menu():
    """Imprime las opciones del menú."""
    print()
    print("=" * 46)
    print("  MÉTODOS ITERATIVOS: JACOBI Y GAUSS-SEIDEL")
    print("=" * 46)
    print("1. Capturar sistema de ecuaciones")
    print("2. Cargar ejercicio original")
    print("3. Mostrar sistema y verificar dominancia diagonal")
    print("4. Resolver por el método de Jacobi")
    print("5. Resolver por el método de Gauss-Seidel")
    print("0. Salir")


def main():
    """Ciclo principal del menú."""
    sistema = None
    while True:
        mostrar_menu()
        opcion = leer_entero("Elija una opción: ", 0, 5)

        if opcion == 0:
            print("Fin del programa.")
            break
        if opcion == 1:
            nuevo = capturar_sistema()
            if nuevo is not None:
                sistema = nuevo
                print("Sistema capturado:")
                print(sistema.mostrar())
        elif opcion == 2:
            sistema = cargar_ejercicio_original()
            print("Ejercicio original cargado:")
            print(sistema.mostrar())
        elif sistema is None:
            print("Primero capture o cargue un sistema (opciones 1 o 2).")
        elif opcion == 3:
            print(sistema.mostrar())
            if sistema.es_diagonalmente_dominante():
                print("El sistema SÍ es diagonalmente dominante: "
                      "la convergencia está garantizada.")
            else:
                print("El sistema NO es diagonalmente dominante: "
                      "el método puede no converger.")
        elif opcion == 4:
            resolver(sistema, "jacobi")
        elif opcion == 5:
            resolver(sistema, "gauss-seidel")


if __name__ == "__main__":
    main()
