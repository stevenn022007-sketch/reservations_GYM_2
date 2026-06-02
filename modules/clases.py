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
    id_miembro = int(input("ID del miembro a editar:"))
    
    # nombre_clase = input("Nombre de la clase: ").strip()

    str_id_miembro = f"clase_{id_miembro}"

    if str_id_miembro in lista_clases:
        info = lista_clases[str_id_miembro]
       
        print(f"Infomacion: {info}" )
    else:
        print(f"❌❌❌La clase con ese id {str_id_miembro} no exsiste❌❌❌")

    
actulizar_clase(clases)
    
    

     
    