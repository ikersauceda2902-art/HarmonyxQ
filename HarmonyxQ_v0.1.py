def mostrar_canciones():
    for i, cancion in enumerate(lista_canciones, start=1):
        print(f"{i}. {cancion['cancion']}")
        print("")
        print(f"Artista:{cancion['artista']}")
        print("")
        print(f"Genero:{cancion['genero']}")
        print("")
    return



def agregar_cancion():
    while True:
        artista = input("Ingrese el artista: ")
        cancion = input("Ingrese la cancion: ")
        genero = input("Ingrese el genero: ")
        lista_canciones.append(
            {
            "cancion" : cancion,
            "artista" : artista,
            "genero" : genero,
        }
        )
        verificacion = str(input("¿Desea añadir otra cancion? (S/N): "))
        if verificacion.upper() == "N":
            return
        elif verificacion.upper() == "S":
            continue
        else:
            print("Ingresa una opcion correcta")

def limpiar_lista():
    lista_canciones.clear()
    print("Su lista ha sido eliminada con exito")
    return

def eliminar_cancion():
    nombre = input("Cancion a eliminar: ")
    for cancion in lista_canciones:
        if cancion["cancion"] == nombre:
            lista_canciones.remove(cancion)
            recursion = input("¿Desea remover otra cancion? (S/N)")
            if recursion.upper() == "S":
                eliminar_cancion()
            elif recursion.upper() == "N":
                return
            else:
                print("algo salio mal :c")
                eliminar_cancion()



def menu():
    while True:
        print("(1) Agregar cancion\n(2) Eliminar cancion\n(3) Mostrar canciones\n(4) Limpiar lista\n(5) Salir")
        opcion = int(input(" Ingrese su opcion: "))
        if opcion == 1:
            agregar_cancion()
        elif opcion == 2:
            eliminar_cancion()
        elif opcion == 3:
            mostrar_canciones()
        elif opcion == 4:
            limpiar_lista()
        elif opcion == 5:
            print("¡Muchas gracias por tu uso!")
            print("Hecho por: Iker Gael Sauceda Nieto")
            print("Hecho el 17/06/2026 a las 2:36 AM")
            break
        else:
            print("ingresa una opcion correcta")
            return


lista_canciones = []
print("===HARMONIQ===")
print(" Este programa sirve para almacenar tus canciones.\n¡Espero disfrutes esta pequeña prueba!")
menu()

