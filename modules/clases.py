clases = {
    "clase_1": {"nombre_clase:": "yoga", "instructor:": "Eliana", "horario:": "mañana", "cupo_maximo:": 20},
    "clase_2": {"nombre_clase:": "zumba", "instructor:": "Gabriel", "horario:": "noche", "cupo_maximo:": 25},
    "clase_3": {"nombre_clase:": "crossfit", "instructor:": "Lina", "horario:": "tarde", "cupo_maximo:": 15},
    "clase_4": {"nombre_clase:": "calistenia", "instructor:": "Leonardo", "horario:": "Jueves 8:00 AM a 10:00 AM", "cupo_maximo": 18},
}

def inspeccionar_clases(lista_clases):
    for clase, datos in lista_clases.items():
        print("-------------------------------")
        print(f"El ID de la clase es:  {clase} ")
        for clave, valor in datos.items():
            print(clave,valor)
    
def crear_clases(lista_clases):
    nombre_clase = input("Ingrese el nombre de la clase: ")
    instructor_clase = input("Ingrese el nombre del instructor: ")
    horario_clase = input("ingrese el horario de la clase 'Mañana, tarde o noche': ")

    try: 
        cupo_maximo = int(input("Ingrese el cupo de la clase: "))
    except ValueError:
        print("El dato tiene que ser numerico y entero")
           
    if cupo_maximo <= 0:
        print("El cupo no puede ser un numero negativo o 0")
        return
    
    nuevo_id = f"clase_{len(lista_clases) + 1}"
     
    lista_clases[nuevo_id] = {
        "nombre_clase": nombre_clase,
        "instructor" : instructor_clase,
        "horario": horario_clase,
        "Cupo_maximo": cupo_maximo 
    }
    
    print(f"la clase {nombre_clase} se agrego exitosamente con el ID {nuevo_id}")


def eliminar_clases(lista_clases):
    eliminar_clase_por_id = input("Ingrese la clase que desea eliminar por ID: ").lower()
    
    if eliminar_clase_por_id in lista_clases:
        lista_clases.pop(eliminar_clase_por_id)
        print(f"El ID {eliminar_clase_por_id} fue eliminado exitosamente")
        
        
def actulizar_clase (lista_clases: dict):
    id_miembro = input("Ingrese el ID de la clase para actualizar: ")
    
    # nombre_clase = input("Nombre de la clase: ").strip()
    if id_miembro in lista_clases:
        while True:
            nuevo_nombre_clase = input("ingrese el nombre de la nueva clase: ")
            nuevo_instructor = input("Ingrese un nuevo instructor, si no escriba el nombre del anterior instructor: ")
            nuevo_horario = input("Ingrese el nuevo horario de la clase 'mañana, tarde, noche': ")
            
            if nuevo_nombre_clase != "" and nuevo_instructor != "" and nuevo_horario != "":
                break
            print("Intenta de nuevo, ninguno de los campos puede quedar vacio...")
        
        while True:
            try:
                nuevos_cupos =int(input("Ingrese el nuevo cupo maximo de la clase: "))
                break
            except ValueError:
                print("Ingrese un numero y entero")

        #modificar datos
        lista_clases[id_miembro]["nombre_clase:"] = nuevo_nombre_clase
        lista_clases[id_miembro]["instructor:"] = nuevo_instructor
        lista_clases[id_miembro]["horario:"] = nuevo_horario
        lista_clases[id_miembro]["cupo_maximo:"] = nuevos_cupos
        
        print(lista_clases)

    else:
        print(f"❌❌❌La clase con ese id {id_miembro} no existe❌❌❌")

    
actulizar_clase(clases)
    
    

     
    