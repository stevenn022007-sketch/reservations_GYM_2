from data import cargar_datos, guardar_datos

def busqueda(ruta):
    ruta_archivo_json = ruta 
    
    entrada_de_datos = cargar_datos(ruta_archivo_json)
    opcion_usuario = input("Ingrese el item el cual desea consultar en la base de datos: ")
    RUTAS_DISPONIBLES = ["clases","miembros","inscripciones"]
    
    if RUTAS_DISPONIBLES in opcion_usuario:
        if RUTAS_DISPONIBLES[0] == "clases":
            entrada_de_datos
    
    