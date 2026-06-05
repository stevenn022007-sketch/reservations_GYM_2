# modules/control_cupos.py
from rich.console import Console

console = Console()

def validar_y_restar_cupo(clases_dict, str_id_clase) -> bool:
    """
    [RETO FINAL]
    Verifica si una clase tiene espacio disponible. 
    Si tiene, reduce el contador en 1 y retorna True. De lo contrario, True/False.
    """
    info_clase = clases_dict[str_id_clase]
    
    # Asegurar la existencia de la propiedad dinámica 'cupos_disponibles'
    if "cupos_disponibles" not in info_clase:
        info_clase["cupos_disponibles"] = info_clase.get("cupo_maximo", 0)

    # Validación estricta
    if info_clase["cupos_disponibles"] <= 0:
        console.print(f"[red]❌ ERROR RETO FINAL: La clase '{info_clase.get('nombre_clase')}' alcanzó su capacidad máxima ({info_clase.get('cupo_maximo')}). Inscripción rechazada.[/red]")
        return False
        
    # Restar cupo
    info_clase["cupos_disponibles"] -= 1
    console.print(f"[blue]📉 Cupo reservado en '{info_clase['nombre_clase']}'. Disponibles ahora: {info_clase['cupos_disponibles']}[/blue]")
    return True


def devolver_cupo_disponible(clases_dict, str_id_clase):
    """
    [RETO FINAL]
    Incrementa el cupo disponible cuando un miembro se da de baja.
    """
    if str_id_clase in clases_dict:
        info_clase = clases_dict[str_id_clase]
        if "cupos_disponibles" not in info_clase:
            info_clase["cupos_disponibles"] = info_clase.get("cupo_maximo", 0)
            
        info_clase["cupos_disponibles"] += 1
        console.print(f"[blue]📈 Cupo liberado en '{info_clase['nombre_clase']}'. Disponibles ahora: {info_clase['cupos_disponibles']}[/blue]")