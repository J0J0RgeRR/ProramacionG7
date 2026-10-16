from collections import deque

cola = deque()

def registrar_paciente(nombre):
    cola.append(nombre)
    print(f"Registrado: {nombre}")

def atender_paciente():
    if not cola:
        print("No hay pacientes en espera")
    else:
        paciente = cola.popleft()
        print(f"Atendiendo a: {paciente}")

def mostrar_cola():
    if not cola:
        print("La cola está vacía")
    else:
        print("Pacientes en espera:")
        for posicion, paciente in enumerate(cola, 1):
            print(f"{posicion}. {paciente}")


while True:
    print("\n--- MENÚ ---")
    print("1. Registrar paciente")
    print("2. Atender paciente")
    print("3. Mostrar pacientes")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Digite el nombre del paciente: ")
        registrar_paciente(nombre)

    elif opcion == "2":
        atender_paciente()

    elif opcion == "3":
        mostrar_cola()

    elif opcion == "4":
        print("Programa finalizado")
        break

    else:
        print("Opción no válida")