from data import cargar_datos, guardar_datos

ruta = "data/clases.json"
HORARIOS_VALIDOS = ["mañana","tarde","noche"]

def inspeccionar_clases():
    Datos_actuales = cargar_datos(ruta)
    for clase, datos in Datos_actuales.items():
        print("-----------------------------")
        print(f"ID de la clase: {clase}")
        for clave, valor in datos.items():
            print(f"{clave}, : {valor}")
            
            
def crear_clase():
    entrada_de_datos = cargar_datos(ruta)
    
    inspeccionar_clases()
    
    while True:
            nombre_clase = input("ingrese el nombre de la nueva clase: ")
            instructor = input("Ingrese un nuevo instructor, si no escriba el nombre del anterior instructor: ")
            
            if nombre_clase != "" and instructor != "":
                break
            print("Intenta de nuevo, ninguno de los campos puede quedar vacio...")
            
    # Validación del horario con opciones permitidas
    while True:
        horario_clase = input("Ingrese el horario de la clase (Mañana, Tarde o Noche): ").strip().lower()
        if horario_clase not in HORARIOS_VALIDOS:
            print(f"Horario inválido. Las opciones válidas son: {', '.join(HORARIOS_VALIDOS)}.")
            
        if horario_clase in HORARIOS_VALIDOS:
            break
    while True:
        try:
            cupo_maximo = int(input("Ingrese el cupo máximo de la clase: "))
            if cupo_maximo <= 0:
                print("El cupo debe ser un número entero mayor que 0.")     
        except ValueError:
            print("El cupo debe ser un valor numérico entero.")
        else:
            break
    #Creamos un Nuevo id automatico 
    nuevo_id = f"{len(entrada_de_datos) + 1}"
    
    # Crear el diccionario de la nueva clase usando nuevo_id como clave
    
    datos_clase = {
            "nombre_clase": nombre_clase,
            "instructor": instructor,
            "horario": horario_clase,
            "cupo_maximo": cupo_maximo
    }
    
    # se añade un subdiccionario nuevo con el ID automatioc y igual al dato clase que ingrese el usuario.
    entrada_de_datos[nuevo_id] = datos_clase
    guardar_datos(ruta, entrada_de_datos )


def eliminar_clases():
    entrada_de_datos = cargar_datos(ruta)
    inspeccionar_clases()
    
    eliminar_clase_por_id = input("Ingrese la clase que desea eliminar por ID: ").lower()
    
    if eliminar_clase_por_id in entrada_de_datos:
        entrada_de_datos.pop(eliminar_clase_por_id)
        print(f"El ID {eliminar_clase_por_id} fue eliminado exitosamente")
        #guardar datos:
        guardar_datos(ruta, entrada_de_datos)
    
    
def actualizar_clase():
    entrada_datos = cargar_datos(ruta)
    
    id_miembro = input("Ingrese el ID de la clase para actualizar: ")
    
    if id_miembro in entrada_datos:
        while True:
            nuevo_nombre_clase = input("ingrese el nombre de la nueva clase: ")
            nuevo_instructor = input("Ingrese un nuevo instructor, si no escriba el nombre del anterior instructor: ")
            if nuevo_nombre_clase != "" and nuevo_instructor != "":
                break
            print("Intenta de nuevo, ninguno de los campos puede quedar vacio...")
    
        while True:
            nuevo_horario_clase = input("Ingrese el horario de la nueva clase (Mañana, Tarde o Noche): ").strip().lower()
            if nuevo_horario_clase not in HORARIOS_VALIDOS:
                print(f"Horario inválido. Las opciones válidas son: {', '.join(HORARIOS_VALIDOS)}.")
                
            if nuevo_horario_clase in HORARIOS_VALIDOS:
                break
    
        while True:
            try:
                nuevo_cupo_maximo = int(input("Ingrese el cupo máximo de la nueva clase: "))
                if nuevo_cupo_maximo <= 0:
                    print("El cupo debe ser un número entero mayor que 0.")     
            except ValueError:
                print("El cupo debe ser un valor numérico entero.")
            else:
                break
            
        #modificar datos
        entrada_datos[id_miembro]["nombre_clase"] = nuevo_nombre_clase
        entrada_datos[id_miembro]["instructor"] = nuevo_instructor
        entrada_datos[id_miembro]["horario"] = nuevo_horario_clase
        entrada_datos[id_miembro]["cupo_maximo"] = nuevo_cupo_maximo
        guardar_datos(ruta, entrada_datos)
        inspeccionar_clases()
    else:
        print(f"❌❌❌La clase con ese id {id_miembro} no existe❌❌❌")
       
       
actualizar_clase() 

        
        
            
            
        
            

    
