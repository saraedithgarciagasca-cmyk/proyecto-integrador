"""Programa principal: menú de consola para los métodos de Jacobi y Gauss-Seidel."""


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
    while True:
        mostrar_menu()
        opcion = leer_entero("Elija una opción: ", 0, 5)

        if opcion == 0:
            print("Fin del programa.")
            break
        print("Opción en construcción.")


if __name__ == "__main__":
    main()
