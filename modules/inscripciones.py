from rich.console import Console
from modules.data import cargar_datos, guardar_datos

console = Console()

Ruta_Json = "data/inscripciones.json"
#-------------------Vincular miembro-------------------
def vincular_miembros(gimnasio_dict, clases_dict, str_id_miembro, str_id_clase):
    inscripciones = cargar_datos(Ruta_Json)

    inscrito = any(
        datos["id_miembro"] == str_id_miembro and datos["id_clase"] == str_id_clase
        for datos in inscripciones.values()
    )

    if inscrito:
        console.print("[yellow]El miembro ya esta inscrito en esta clase.[/yellow]")
        return False
    
    nuevo_id = f"inscripcion_{len(inscripciones) + 1}"
    inscripciones[nuevo_id] = {
        "id_miembro": str_id_miembro,
        "id_clase": str_id_clase
    }
    guardar_datos(Ruta_Json, inscripciones)

    nombre_m = gimnasio_dict[str_id_miembro]["nombre"]
    nombre_c = clases_dict[str_id_clase]["nombre_clase"]
    
    console.print(f"[bold green]✅ {nombre_m} ha sido vinculado a la clase de {nombre_c}.[/bold green]")
    return True
#------------------Desvincular miembros------------------
def desvincular_miembro_de_clase(str_id_miembro, str_id_clase):
    inscripciones = cargar_datos(Ruta_Json)
    """
    Elimina la unión entre el miembro y la clase.
    """
    id_a_eliminar = None
    for k, v in inscripciones.items():
        if v["id_miembro"] == str_id_miembro and v["id_clase"] == str_id_clase:
            id_a_eliminar = k
            break

    if id_a_eliminar:
        inscripciones.pop(id_a_eliminar)
        guardar_datos(Ruta_Json, inscripciones)
        return True
    
    console.print("[yellow]❌ No se encontró la inscripción especificada.[/yellow]")
    return False

#------------------Visualizacion------------------
def mostrar_miembros_clase(gimnasio_dict, id_clase_num):
    inscripciones = cargar_datos(Ruta_Json)
    str_id_clase = f"{id_clase_num}"
    console.print(f"\n[bold cyan] Miembros inscritos en {str_id_clase.upper()}:[/bold cyan]")

    encontrados = False
    for datos in inscripciones.values():
        if datos["id_clase"] == str_id_clase:
            m_id =datos["id_miembro"]
            nombre_m = gimnasio_dict[m_id]["nombre"]if m_id in gimnasio_dict else "desconociod"
            console.print(f" -{m_id}: [bold]{nombre_m}[/bold]")
            encontrados = True

    if not encontrados:
        console.print("[yellow] No hay miembros en esta clase. [/yellow]")

def mostrar_clases_miembro(clases_dict, id_miembro_num):
    inscripciones = cargar_datos(Ruta_Json)
    str_id_miembro = f"miembro_{id_miembro_num}"
    console.print(f"\n[bold cyan] Clases asignadas {str_id_miembro.upper()}:[/bold cyan]")
    
    encontrados = False
    for datos in inscripciones.values():
        if datos["id_miembro"] == str_id_miembro:
            c_id = datos["id_clase"]
            
            info_c = clases_dict.get(c_id, {})
            nombre_c = info_c.get("nombre_clase", "Desconocida")
            
            console.print(f"  - {c_id}: [bold]{nombre_c}[/bold]")
            encontrados = True
            
    if not encontrados:
        console.print("[yellow]  Este miembro no tiene clases asignadas.[/yellow]")