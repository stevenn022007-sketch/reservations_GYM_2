# modules/inscripciones.py

# Traemos la herramienta para pintar la pantalla con textos de colores
from rich.console import Console
# Traemos los dos botones que fabricamos para abrir y guardar los archivos del computador
from modules.data import cargar_datos, guardar_datos
# Traemos las reglas del juego final para controlar si hay o no espacio en los salones
import modules.reto_final as reto_final

# Activamos el pintor de la pantalla para poder usar colores
console = Console()

# Dejamos anotadas las tres direcciones de los archivos donde guardamos toda la información
Ruta_Json = "data/inscripciones.json"
Ruta_Clases = "data/clases.json"
Ruta_Miembros = "data/miembros.json"

# =====================================================================
#  SUBMENÚ EXCLUSIVO DE INSCRIPCIONES
# =====================================================================
def menu_inscripciones():
    """
    Este es el control central de la pantalla de inscripciones.
    Se queda repitiéndose en un círculo infinito hasta que el usuario decida salir.
    """
    while True:
        # Mostramos el letrero con los títulos y las opciones del menú
        console.print("\n[bold magenta]=== 📝 GESTIÓN DE INSCRIPCIONES Y CUPOS ===[/bold magenta]")
        console.print("[bold cyan]1.[/bold cyan] Inscribir Miembro en Clase (Reto Cupos)")
        console.print("[bold cyan]2.[/bold cyan] Dar de Baja Miembro de Clase")
        console.print("[bold cyan]3.[/bold cyan] Consultar Miembros por Clase")
        console.print("[bold cyan]4.[/bold cyan] Consultar Clases de un Miembro")
        console.print("[bold red]0.[/bold red] Volver al Menú Principal")
        
        # Le pedimos al usuario que escriba un número y le borramos los espacios vacíos que deje por error
        opcion = console.input("\n[bold yellow]Seleccione una opción: [/bold yellow]").strip()

        # Si el usuario escribe 1, arranca el proceso para meter a alguien a una clase
        if opcion == "1":
            flujo_inscripcion()
        # Si escribe 2, arranca el proceso para sacar a alguien de una clase
        elif opcion == "2":
            flujo_baja()
        # Si escribe 3, intenta mostrar quiénes están metidos en un salón
        elif opcion == "3":
            try:
                # Pide el número de la clase (por ejemplo: 1)
                id_c = int(console.input("[green]Ingrese el número de la clase a consultar (ej: 1): [/green]"))
                # Abre la lista de personas registradas en el gimnasio
                base_m = cargar_datos(Ruta_Miembros)
                # Llama a la función que los dibuja en la pantalla
                mostrar_miembros_clase(base_m, id_c)
            except ValueError:
                # Si el usuario escribe letras en vez de un número, muestra este aviso para que no se apague el programa
                console.print("[red]⚠ Entrada inválida.[/red]")
        # Si escribe 4, intenta mostrar a qué clases asiste una persona específica
        elif opcion == "4":
            try:
                # Pide el número de la persona (por ejemplo: 3)
                id_m = int(console.input("[green]Ingrese el número del miembro a consultar (ej: 1): [/green]"))
                # Abre la lista de clases disponibles
                base_c = cargar_datos(Ruta_Clases)
                # Llama a la función que las dibuja en la pantalla
                mostrar_clases_miembro(base_c, id_m)
            except ValueError:
                # Si escribe letras en vez de números, frena el error y avisa
                console.print("[red]⚠ Entrada inválida.[/red]")
        # Si escribe 0, rompe el círculo infinito de este submenú y regresa al menú de antes
        elif opcion == "0":
            break 
        # Si escribe cualquier otra cosa (un 9, una letra, etc.), avisa que no es una opción válida
        else:
            console.print("[red]⚠ Opción inválida en este submenú.[/red]")

# =====================================================================
#  FLUJOS INTERNOS DE CONTROL
# =====================================================================
def flujo_inscripcion():
    # Muestra un letrero amarillo avisando que inicia la inscripción
    console.print("\n[bold yellow]📝 PROCESO DE INSCRIPCIÓN A CLASE[/bold yellow]")
    try:
        # Pide los números enteros del alumno y de la clase
        id_m_num = int(console.input("[green]Ingrese el número de ID del miembro (ej: 1): [/green]"))
        id_c_num = int(console.input("[green]Ingrese el número de ID de la clase (ej: 1): [/green]"))
    except ValueError:
        # Si el usuario digita mal y pone letras, detiene el proceso con este aviso
        console.print("[red]⚠ Error: Los identificadores deben ser numéricos.[/red]")
        return # Cancela y se sale de este proceso

    # Le pega la palabra texto para armar los códigos internos: "miembro_1" y "clase_1"
    str_id_miembro = f"miembro_{id_m_num}"
    str_id_clase = f"clase_{id_c_num}"

    # Va al disco duro y trae los papeles actualizados de los miembros y de las clases
    base_miembros = cargar_datos(Ruta_Miembros)
    base_clases = cargar_datos(Ruta_Clases)

    # Revisa si el código del miembro no existe en tus papeles. Si no existe, cancela todo.
    if str_id_miembro not in base_miembros:
        console.print(f"[red]❌ El miembro {str_id_miembro} no existe.[/red]")
        return
    # Revisa si la clase no existe en tus papeles. Si no existe, cancela todo.
    if str_id_clase not in base_clases:
        console.print(f"[red]❌ La clase {str_id_clase} no existe.[/red]")
        return

    # Llama al otro archivo para comprobar si quedan sillas vacías en esa clase y resta una silla
    if reto_final.validar_y_restar_cupo(base_clases, str_id_clase):
        # Si había espacio, intenta hacer la unión oficial del alumno con la clase
        exito_vinculo = vincular_miembros(base_miembros, base_clases, str_id_miembro, str_id_clase)
        
        # Si la unión se logró sin problemas (no estaba repetido)...
        if exito_vinculo:
            # Guarda en el computador la lista de clases con la silla que acabamos de restar
            guardar_datos(Ruta_Clases, base_clases)
            console.print("[bold green]💾 Los cupos del gimnasio se han guardado con éxito.[/bold green]")
        else:
            # Si el miembro ya estaba metido en esa clase, se cancela la unión y le devolvemos la silla que le habíamos quitado
            reto_final.devolver_cupo_disponible(base_clases, str_id_clase)

def flujo_baja():
    # Muestra un letrero rojo avisando que inicia el retiro
    console.print("\n[bold red]🥶 PROCESO DE DESVINCULACIÓN (DAR DE BAJA)[/bold red]")
    try:
        # Pide los números del alumno y de la clase que va a abandonar
        id_m_num = int(console.input("[green]Ingrese el número de ID del miembro (ej: 1): [/green]"))
        id_c_num = int(console.input("[green]Ingrese el número de ID de la clase (ej: 1): [/green]"))
    except ValueError:
        # Frena el error si meten letras
        console.print("[red]⚠ Error: Los identificadores deben ser numéricos.[/red]")
        return

    # Vuelve a armar los nombres clave con texto: "miembro_1" y "clase_1"
    str_id_miembro = f"miembro_{id_m_num}"
    str_id_clase = f"clase_{id_c_num}"

    # Trae los datos de las clases desde el computador
    base_clases = cargar_datos(Ruta_Clases)

    # Llama a la función para borrar la inscripción. Si encuentra el registro y lo borra exitosamente...
    if desvincular_miembro_de_clase(str_id_miembro, str_id_clase):
        # Llama al otro archivo para sumarle una silla libre al salón (porque se fue un alumno)
        reto_final.devolver_cupo_disponible(base_clases, str_id_clase)
        # Guarda la lista de clases con su silla recuperada en el computador
        guardar_datos(Ruta_Clases, base_clases)
        console.print("[bold green]✅ Cupo reestablecido en la base de datos.[/bold green]")

#-------------------Vincular miembro-------------------
def vincular_miembros(gimnasio_dict, clases_dict, str_id_miembro, str_id_clase):
    # Carga la lista actual de todas las inscripciones que existen guardadas en el archivo
    inscripciones = cargar_datos(Ruta_Json)

    # Revisa una por una las inscripciones para ver si esa persona ya está metida en esa misma clase
    inscrito = any(
        datos["id_miembro"] == str_id_miembro and datos["id_clase"] == str_id_clase
        for datos in inscripciones.values()
    )

    # Si la revisión dice que es verdad (que ya estaba inscrito), muestra advertencia y detiene todo devolviendo "Falso"
    if inscrito:
        console.print("[yellow]El miembro ya esta inscrito en esta clase.[/yellow]")
        return False
    
    # Crea un código nuevo automático sumándole 1 a la cantidad total de inscripciones (Ej: "inscripcion_5")
    nuevo_id = f"inscripcion_{len(inscripciones) + 1}"
    # Mete el nuevo registro en la lista con el código del miembro y el de la clase
    inscripciones[nuevo_id] = {
        "id_miembro": str_id_miembro,
        "id_clase": str_id_clase
    }
    # Sella y guarda el archivo de inscripciones en el disco duro para que no se pierda
    guardar_datos(Ruta_Json, inscripciones)

    # Busca en tus carpetas el nombre de la persona real y el nombre de la clase real
    nombre_m = gimnasio_dict[str_id_miembro]["nombre"]
    nombre_c = clases_dict[str_id_clase]["nombre_clase"]
    
    # Pinta un letrero verde bonito avisando que la persona y la clase se unieron con éxito
    console.print(f"[bold green]✅ {nombre_m} ha sido vinculado a la clase de {nombre_c}.[/bold green]")
    return True # Devuelve "Verdadero" avisando que todo salió perfecto

#------------------Desvincular miembros------------------
def desvincular_miembro_de_clase(str_id_miembro, str_id_clase):
    """
    Elimina la unión entre el miembro y la clase.
    """
    # Abre los registros de inscripciones guardados en tu computador
    inscripciones = cargar_datos(Ruta_Json)
    id_a_eliminar = None # Una variable vacía para anotar el código que vamos a borrar
    
    # Revisa todas las inscripciones buscando el código exacto de esa persona en esa clase
    for k, v in inscripciones.items():
        if v["id_miembro"] == str_id_miembro and v["id_clase"] == str_id_clase:
            id_a_eliminar = k # Al encontrarlo, guarda el código (ej: "inscripcion_3")
            break # Deja de buscar porque ya lo encontramos

    # Si logramos encontrar algo y la variable ya no está vacía...
    if id_a_eliminar:
        # Arranca y elimina ese registro de la lista por completo
        inscripciones.pop(id_a_eliminar)
        # Guarda los cambios con la lista actualizada sin ese registro en el computador
        guardar_datos(Ruta_Json, inscripciones)
        return True # Avisa con un "Verdadero" que sí se pudo borrar
    
    # Si terminó la búsqueda y no encontró nada, avisa que esa inscripción no existía y devuelve "Falso"
    console.print("[yellow]❌ No se encontró la inscripción especificada.[/yellow]")
    return False

#------------------Visualizacion------------------
def mostrar_miembros_clase(gimnasio_dict, id_clase_num):
    # Trae todas las uniones de inscripciones desde el computador
    inscripciones = cargar_datos(Ruta_Json)
    # Convierte el número que escribió el usuario en el formato completo (ej: de 1 pasa a "clase_1")
    str_id_clase = f"clase_{id_clase_num}"
    console.print(f"\n[bold cyan] Miembros inscritos en {str_id_clase.upper()}:[/bold cyan]")

    encontrados = False # Un interruptor para saber si encontramos al menos a una persona
    # Empieza a revisar todos los registros de inscripciones
    for datos in inscripciones.values():
        # Si el registro pertenece a la clase que estamos buscando...
        if datos["id_clase"] == str_id_clase:
            m_id = datos["id_miembro"] # Saca el código del alumno (ej: "miembro_2")
            # Busca en el archivo del gimnasio cómo se llama ese código real. Si no aparece, lo bautiza "desconocido"
            nombre_m = gimnasio_dict[m_id]["nombre"] if m_id in gimnasio_dict else "desconocido"
            # Muestra el nombre en la pantalla con un puntito de lista
            console.print(f" -{m_id}: [bold]{nombre_m}[/bold]")
            encontrados = True # Enciende el interruptor porque sí encontramos a alguien

    # Si al final de revisar todo, el interruptor siguió apagado, avisa que el salón está vacío
    if not encontrados:
        console.print("[yellow] No hay miembros en esta clase. [/yellow]")

def mostrar_clases_miembro(clases_dict, id_miembro_num):
    # Abre el archivo de inscripciones del computador
    inscripciones = cargar_datos(Ruta_Json)
    # Convierte el número del alumno en su código completo (ej: de 2 pasa a "miembro_2")
    str_id_miembro = f"miembro_{id_miembro_num}"
    console.print(f"\n[bold cyan] Clases asignadas {str_id_miembro.upper()}:[/bold cyan]")
    
    encontrados = False # Otro interruptor para saber si la persona tiene clases o no
    # Revisa cada una de las inscripciones del gimnasio
    for datos in inscripciones.values():
        # Si la inscripción le pertenece al alumno que estamos consultando...
        if datos["id_miembro"] == str_id_miembro:
            c_id = datos["id_clase"] # Saca el código de la clase (ej: "clase_3")
            
            # Va a los papeles de clases y saca la información de esa clase. Si no hay nada, crea un bloque vacío
            info_c = clases_dict.get(c_id, {})
            # Extrae el nombre real del texto (ej: "yoga"). Si no lo encuentra, lo llama "Desconocida"
            nombre_c = info_c.get("nombre_clase", "Desconocida")
            
            # Pinta en la pantalla el código y el nombre de la actividad
            console.print(f"  - {c_id}: [bold]{nombre_c}[/bold]")
            encontrados = True # Activa el interruptor porque encontramos al menos una clase
            
    # Si terminó la lista y el alumno no tenía nada registrado, muestra este mensaje amarillo
    if not encontrados:
        console.print("[yellow]  Este miembro no tiene clases asignadas.[/yellow]")

# =====================================================================
#  BLOQUE DE EJECUCIÓN DIRECTA (Para pruebas sin pasar por main.py)
# =====================================================================
# Esta línea le dice a Python: "Si el usuario le da Play DIRECTAMENTE a este archivo inscripciones.py..."
if __name__ == "__main__":
    try:
        # Arranca de inmediato el menú de inscripciones para poder hacer pruebas rápidas
        menu_inscripciones()
    except KeyboardInterrupt:
        # Si el usuario presiona las teclas de emergencia para apagar la consola (Ctrl + C), frena la caída y se despide bonito
        console.print("\n[bold red]👋 Ejecución interrumpida.[/bold red]\n")