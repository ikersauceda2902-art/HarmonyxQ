def mostrar_canciones():
        print("LISTA DE CANCIONES:\n=====================")
        if lista_canciones == []:
                print("")
                print("¡No hay canciones!")
                print("")
                print("=====================")
                return
        else:
            for i, cancion in enumerate(lista_canciones, start=1):
                print(f"{i}. {cancion['cancion']}")
                print("")
                print(f"Artista:{cancion['artista']}")
                print("")
                print(f"Genero:{cancion['genero']}")
                print("")
                print("=====================")




def agregar_cancion():
    while True:
            artista = input("Ingrese el artista: ")
            print("")
            cancion = input("Ingrese la cancion: ")
            print("")
            genero = input("Ingrese el genero: ")
            lista_canciones.append(
            {
            "cancion" : cancion,
            "artista" : artista,
            "genero" : genero,
        }
        )
            print("")
            try:
                verificacion = str(input("¿Desea añadir otra cancion? (S/N): "))
                if verificacion.upper() == "N":
                    print("")
                    print("=====================")
                    return
                elif verificacion.upper() == "S":
                    print("")
                    continue
                else:
                    print("Ingresa una opcion correcta")
                    print("")
            except ValueError:
                print("Debes ingresar una opcion")





def limpiar_lista():
    lista_canciones.clear()
    print("Su lista ha sido eliminada con exito")
    return




def eliminar_cancion():
    while True:
            nombre = input("Cancion a eliminar: ")
            cancion_borrar = None
            for cancion in lista_canciones:
                if cancion["cancion"] == nombre:
                    cancion_borrar = cancion
            if cancion_borrar != None:
                lista_canciones.remove(cancion_borrar)
                print("¡Cancion eliminada exitosamente!")
            else:
                print("La cancion no pudo ser encontrada :c")
            try:
                recursion = input("¿Desea remover otra cancion? (S/N): ")
                if recursion.upper() == "S":
                    print("")
                    continue
                elif recursion.upper() == "N":
                    print("")
                    return
                else:
                    print("algo salio mal :c")
                    continue
            except ValueError:
                print("Debes ingresar una opcion")
                print("")
                continue



def menu():
    while True:
            print("")
            print("=====================")
            print("MENU:")
            print("=====================")
            print("(1) Agregar cancion\n(2) Eliminar cancion\n(3) Mostrar canciones\n(4) Limpiar lista\n(5) Salir")
            print("")
            try:
                opcion = int(input(" >>>Ingrese su opcion: "))
                print("")
                if opcion == 1:
                    agregar_cancion()
                elif opcion == 2:
                    eliminar_cancion()
                elif opcion == 3:
                    mostrar_canciones()
                elif opcion == 4:
                    limpiar_lista()
                elif opcion == 5:
                    print("=====================")
                    print("¡Muchas gracias por tu uso!")
                    print("Hecho por: Iker Gael Sauceda Nieto")
                    print("Hecho el 17/06/2026 a las 2:36 AM")
                    print("=====================")
                    break
                else:
                    print("")
                    print("Ingresa una opcion correcta")
                    print("")
            except ValueError:
                print("Debes ingresar un numero")
                print("")




lista_canciones = []
print(r"""
===========================================================================
 __  __                                                      _____      
/\ \/\ \                                                 __ /\  __`\    
\ \ \_\ \      __     _ __    ___ ___      ___     ___  /\_\\ \ \/\ \   
 \ \  _  \   /'__`\  /\`'__\/' __` __`\   / __`\ /' _ `\\/\ \\ \ \ \ \  
  \ \ \ \ \ /\ \L\.\_\ \ \/ /\ \/\ \/\ \ /\ \L\ \/\ \/\ \\ \ \\ \ \\'\\ 
   \ \_\ \_\\ \__/.\_\\ \_\ \ \_\ \_\ \_\\ \____/\ \_\ \_\\ \_\\ \___\_\
    \/_/\/_/ \/__/\/_/ \/_/  \/_/\/_/\/_/ \/___/  \/_/\/_/ \/_/ \/__//_/

===========================================================================
""")

print(" Este programa sirve para almacenar tus canciones.\n¡Espero disfrutes esta pequeña prueba!")
menu()

