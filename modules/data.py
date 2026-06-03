import json
import os
# "OS" significa operation system sirve para interactuar con los archivos del compu 

def cargar_datos(ruta_archivo):
    
    # Verificamos si el archivo físico ya existe en la carpeta
    if os.path.exists(ruta_archivo):
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo: # Abre el archivo en modo lectura (r = Read)
                # "encoding" = codificacion y "utf-8" = Es una tabla de traduccion de caracteres, evita que los nombres se rompan 
                # json.load transforma el texto del JSON de vuelta a un diccionario de Python
                datos = json.load(archivo)
                print("📂 ¡Datos cargados exitosamente desde el archivo JSON!")
                return datos
        except Exception as e: # Evita que el programa se rompa devolviendolo vacio
            print(f"⚠️ Error al leer el archivo JSON: {e}. Se usarán datos vacíos.")
            return {}
    else:
        # Si el archivo no existe, retornamos un diccionario vacío (o tus clases por defecto)
        print("ℹ️ No se encontró un archivo JSON previo. Iniciando con base de datos limpia.")
        return {}
    

def guardar_datos(ruta_archivo, datos): # Agarra un diccionario de Python y lo pasa a JSON
    try:
        os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True) # Si no existen las carpetas en la ruta las crea automaticamente
# "os.makedirs" Esta diciendo que cree esa carpeta ahora mismo 
# "os.path.dirname(ruta_archivo)" Extrae el nombre de la carpeta y se encarga de recortar el nombre
# "exist_ok=True" Le esta diciendo a python que si la carpeta ya existe ignore la orden        
        
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo: # Abre el archivo en modo escritura (w = write) reemplazando el contenido
            # With es como un switch ayuda a apagar o encender la funcion sin que se quede bloqueada y abierta
            # "encoding" = codificacion y "utf-8" = Es una tabla de traduccion de caracteres, evita que los nombres se rompan 
            
            json.dump(datos, archivo, ensure_ascii=False, indent=4) 
# El "json.dump" es como una maquina para empacar, le dice agarra "datos" empacalos en "archivo"
# el "ensure_ascii=false" se refiere a que conserve los datos sin cambiarlos 
# y el "indent=4" es para que los deje ordenados 4 cm de separacion   
        return True #Le dice que la operacion fue exitosa 👍🏿
    
    except Exception as e: #Si falla por falta de espacio que muestre error
        print(f"Error al guardar los datos: {e}") 
        return False #Avisa que la operacion fallo, deteniendo todo y cancelandolo