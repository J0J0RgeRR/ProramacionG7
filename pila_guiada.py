import os 
pila= []

def limpiarPantalla():
    os.system("cls")
def pausar():
    while True:
        respuesta= input("Presione enter para continuar con el programa...")
        if respuesta == "":
            break
        else:
            print("Solo debe presionar Enter.")
def apilar():
    libro = input("ingrese el nombre del libro:")
    pila.append(libro)
    print(f"Libro agregado: {libro}")

def desapilar():
    if len(pila) == 0:
        print("La pila esta vacia")
    else:
        libro= pila.pop()
        print(f"Libro desapilado: {libro}")

def mostrarPila():
    if not pila:
        return "No hay libros registrados"
    else:
        return f"pila actual: {pila} Libro en el tope: {pila[-1]}"
        

while True:
  limpiarPantalla() 
  print("===Pila de libros===")
  print("1.Apilar libro.")
  print("2.Desapilar libro.")
  print("3.Mostrar la pila y el tope de esta.")
  print("4.Salir")

  try:
      opcion= int(input("Seleccione la opcion que desea:"))

      if opcion == 1:
          apilar()
          pausar()
      elif opcion == 2:
          desapilar()
          pausar()
      elif opcion == 3:
          print(mostrarPila())
          pausar()
      elif opcion == 4:
          print("Programa finalizado, muchas gracias por usarlo.")
          break
      else:
          print("Debe elegir una opcion entre el 1 y el 4 ")
          pausar()
  except ValueError:
      print("Debe ingresar un numero. ")
      pausar()
      