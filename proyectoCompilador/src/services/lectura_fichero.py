def leer_fichero(path:str)->str:
    try:
        with open(path, 'r') as file:
            contenido = file.read()
            return contenido
    except FileNotFoundError:
        print("El archivo no existe.")
    except PermissionError:
        print("No tienes permiso para leer el archivo.")
    except Exception as e:
        print("Ocurrió un error:", e)
        
def escritura_fichero(path:str,texto:str)->None:
    try:
        with open(path, '+w') as file:
            file.write(texto)
            file.close()
    except FileNotFoundError:
        print("El archivo no existe.")
    except PermissionError:
        print("No tienes permiso para leer el archivo.")
    except Exception as e:
        print("Ocurrió un error:", e)
        