
# Simulador de editor de texto con pila LIFO

acciones = []


def registrar_accion(descripcion):
    if not descripcion:
        print("Error: la descripción no puede estar vacía.")
        return

    acciones.append(descripcion)
    print("Acción registrada:", descripcion)


def deshacer():
    if not acciones:
        print("No existen acciones para deshacer.")
        return

    ultima = acciones.pop()
    print("Se deshizo:", ultima)


def historial():
    if not acciones:
        print("No hay acciones pendientes.")
    else:
        print("Acciones pendientes:")

        for i, accion in enumerate(acciones, start=1):
            print(f"{i}. {accion}")


def mostrar_menu():
    print("\n===== EDITOR DE TEXTO =====")
    print("1. Registrar acción")
    print("2. Deshacer última acción")
    print("3. Mostrar acciones pendientes")
    print("4. Salir")


def main():
    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                descripcion = input(
                    "Escriba la acción realizada: "
                ).strip()

                registrar_accion(descripcion)

            elif opcion == 2:
                deshacer()

            elif opcion == 3:
                historial()

            elif opcion == 4:
                print("Programa finalizado.")
                break

            else:
                print("Opción inválida. Ingrese del 1 al 4.")

        except ValueError:
            print("Error: debe ingresar un número entero.")


if __name__ == "__main__":
    main()