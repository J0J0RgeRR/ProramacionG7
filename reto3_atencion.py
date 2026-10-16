from collections import deque

cola = deque()
turno = 1


def registrar_cliente():
    global turno

    nombre = input("Digite el nombre del cliente: ").strip()

    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
    else:
        cola.append((turno, nombre))
        print(f"Turno {turno} registrado para {nombre}.")
        turno += 1


def atender_cliente():
    if not cola:
        print("No hay clientes pendientes.")
    else:
        numero, nombre = cola.popleft()
        print(f"Atendiendo al turno {numero}: {nombre}")


def proximo_cliente():
    if not cola:
        print("No hay clientes pendientes.")
    else:
        numero, nombre = cola[0]
        print(f"Próximo cliente: Turno {numero} - {nombre}")


def mostrar_clientes():
    if not cola:
        print("No hay clientes en espera.")
    else:
        print("\nClientes en espera:")
        for numero, nombre in cola:
            print(f"Turno {numero} - {nombre}")


def cantidad_pendientes():
    print(f"Cantidad de clientes pendientes: {len(cola)}")


while True:
    print("\n--- MENÚ DE TURNOS ---")
    print("1. Registrar cliente")
    print("2. Atender cliente")
    print("3. Consultar próximo cliente")
    print("4. Mostrar clientes en espera")
    print("5. Mostrar cantidad de pendientes")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_cliente()

    elif opcion == "2":
        atender_cliente()

    elif opcion == "3":
        proximo_cliente()

    elif opcion == "4":
        mostrar_clientes()

    elif opcion == "5":
        cantidad_pendientes()

    elif opcion == "6":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")