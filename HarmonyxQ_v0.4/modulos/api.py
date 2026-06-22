import requests



url = "https://itunes.apple.com/search?term={search_query}&media=music"


#artistName
#trackName
#primaryGenreName

def buscar_API():
    while True:
        lista_temporal = []
        search_query = input("Ingrese la cancion/artista/genero a buscar: ")
        print("")
        response = requests.get(f"https://itunes.apple.com/search?term={search_query}&media=music")
        datos_api = response.json()
        resultados = datos_api["results"]
        resultados = resultados[:5]
        for data in resultados:
            artista = data["artistName"]
            cancion = data["trackName"]
            genero = data["primaryGenreName"]
            dicc_temporal = {
            "artista" : artista,
            "cancion" : cancion,
            "genero" : genero
            }
            lista_temporal.append(dicc_temporal)

        for i,cancion in enumerate(lista_temporal, start=1):
            print(f"{i}.Cancion: {cancion['cancion']}")
            print(f"Artista:{cancion['artista']}")
            print(f"Genero:{cancion['genero']}")
            print("")
        lista_intenet = []
        while True:
            try:
                opcion = int(input("Ingrese la cancion/artista/genero que desea (1-5):"))
                canciones_internet = (lista_temporal[opcion-1])
                lista_intenet.append(canciones_internet)
                return lista_intenet
                break
            except ValueError:
                print("ingrese un número")
                continue
            except IndexError:
                print("ingrese una opcion correcta: (1-5)")
                continue


buscar_API()