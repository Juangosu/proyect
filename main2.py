# Main.py

# Grupo: Número de grupo
# Integrante 1: Nombre Apellido - Código
# Integrante 2: Nombre Apellido - Código
# Integrante 3: Nombre Apellido - Código
# Integrante 4: Nombre Apellido - Código
# Integrante 5: Nombre Apellido - Código

from Funciones2 import crear_matriz, mostrar_matriz, dibujar_linea, dibujar_elipse, dibujar_rectangulo


def menu():
    print("Menu")
    print("1. Agregar una línea")
    print("2. Agregar una elipse o círculo")
    print("3. Agregar un rectángulo o cuadrado")
    print("8. Salir del programa")


def main():
    ancho = 82
    alto = 42
    matriz = crear_matriz(ancho, alto)

    while True:
        menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            x1 = int(input("Ingrese la coordenada x1: "))
            y1 = int(input("Ingrese la coordenada y1: "))
            x2 = int(input("Ingrese la coordenada x2: "))
            y2 = int(input("Ingrese la coordenada y2: "))
            if 0 <= x1 < ancho and 0 <= y1 < alto and 0 <= x2 < ancho and 0 <= y2 < alto:
                dibujar_linea(matriz, x1, y1, x2, y2)
                mostrar_matriz(matriz)
            else:
                print("Coordenadas fuera de rango.")

        elif opcion == 2:
            xc = int(input("Ingrese la coordenada x del centro: "))
            yc = int(input("Ingrese la coordenada y del centro: "))
            rx = int(input("Ingrese el radio en x: "))
            ry = int(input("Ingrese el radio en y: "))
            if 0 <= xc < ancho and 0 <= yc < alto and xc + rx < ancho and yc + ry < alto:
                dibujar_elipse(matriz, xc, yc, rx, ry)
                mostrar_matriz(matriz)
            else:
                print("Coordenadas fuera de rango.")

        elif opcion == 3:
            x = int(input("Ingrese la coordenada x del punto inferior izquierdo: "))
            y = int(input("Ingrese la coordenada y del punto inferior izquierdo: "))
            base = int(input("Ingrese la base: "))
            altura = int(input("Ingrese la altura: "))
            if 0 <= x < ancho and 0 <= y < alto and x + base < ancho and y + altura < alto:
                dibujar_rectangulo(matriz, x, y, base, altura)
                mostrar_matriz(matriz)
            else:
                print("Coordenadas fuera de rango.")

        elif opcion == 8:
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
