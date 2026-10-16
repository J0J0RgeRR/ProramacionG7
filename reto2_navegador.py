
# Simulador de navegación web con pila LIFO

historial = []
pagina_actual = None


def visitar_pagina(url):
    global pagina_actual

    if not url:
        print("Error: debe ingresar una página web.")
        return

    if pagina_actual is not None:
        historial.append(pagina_actual)

    pagina_actual = url
    print("Página visitada:", pagina_actual)


def regresar():
    global pagina_actual

    if not historial:
        print("No existen páginas anteriores.")
        return

    pagina_actual = historial.pop()
    print("Regresaste a:", pagina_actual)


def consultar_pagina():
    if pagina_actual is None:
        print("No hay ninguna página abierta.")
    else:
        print("Página actual:", pagina_actual)


def mostrar_historial():
    if not historial:
        print("No hay páginas anteriores pendientes.")
        return

    print("\n===== HISTORIAL DE RETROCESO =====")

    for i in range(len(historial) - 1, -1, -1):
        print(f"{len(historial) - i}. {historial[i]}")

    print("=================================")


def mostrar_menu():
    print("\n===== SIMULADOR DE NAVEGACIÓN =====")
    print("1. Visitar una página nueva")
    print("2. Regresar a la página anterior")
    print("3. Consultar página actual")
    print("4. Mostrar historial de retroceso")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                url = input("Ingrese la página web: ").strip()
                visitar_pagina(url)

            elif opcion == 2:
                regresar()

            elif opcion == 3:
                consultar_pagina()

            elif opcion == 4:
                mostrar_historial()

            elif opcion == 5:
                print("Navegador cerrado.")
                break

            else:
                print("Opción inválida. Ingrese del 1 al 5.")

        except ValueError:
            print("Error: debe ingresar un número entero.")


if __name__ == "__main__":
    main()