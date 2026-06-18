from modulos.canciones import (
    agregar_cancion,
    eliminar_cancion,
    mostrar_canciones,
    limpiar_lista,
)




from modulos.archivos import (
    guardar_canciones
)


def menu(lista_canciones):
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
                    agregar_cancion(lista_canciones)
                elif opcion == 2:
                    eliminar_cancion(lista_canciones)
                elif opcion == 3:
                    mostrar_canciones(lista_canciones)
                elif opcion == 4:
                    limpiar_lista(lista_canciones)
                elif opcion == 5:
                    print("Guardando datos...")
                    guardar_canciones(lista_canciones)
                    print("¡Datos guardados con éxito!")
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
