import json
import os

def cargar_datos():
    nombre_archivo = "clases.json"
    
    # Verificamos si el archivo físico ya existe en la carpeta
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                # json.load transforma el texto del JSON de vuelta a un diccionario de Python
                datos = json.load(archivo)
                print("📂 ¡Datos cargados exitosamente desde el archivo JSON!")
                return datos
        except Exception as e:
            print(f"⚠️ Error al leer el archivo JSON: {e}. Se usarán datos vacíos.")
            return {}
    else:
        # Si el archivo no existe, retornamos un diccionario vacío (o tus clases por defecto)
        print("ℹ️ No se encontró un archivo JSON previo. Iniciando con base de datos limpia.")
        return {}
    