def mostrar_canciones(lista_canciones):
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




def agregar_cancion(lista_canciones):
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





def limpiar_lista(lista_canciones):
    lista_canciones.clear()
    print("Su lista ha sido eliminada con exito")
    return




def eliminar_cancion(lista_canciones):
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