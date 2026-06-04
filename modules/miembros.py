# --------------CRUD--------MIEMBROS-----------------
from rich.console import Console
from rich.table import Table
from modules.data import cargar_datos, guardar_datos 
# Qué necesita un miembro? -> id, nombre, tipo de suscripción
# console = Console()  # Inicializamos la consola de Rich para usarla en este módulo
#rich es una biblioteca de Python que permite crear interfaces de usuario en la terminal con estilos y colores. 
# En este código, se utiliza para imprimir mensajes estilizados y para manejar la entrada del usuario de manera más atractiva.
console = Console()
Ruta_Json = "data/miembros.json"
# -------VER MIEMBROS-----------------
# que  tiene que hacer esta funcion? -> leer el diccionario de miembros y mostrarlo en una tabla
def ver_miembros(gimnasio):
    gimnasio = cargar_datos(Ruta_Json)
    console.print("\n[bold cyan]👀 LISTA DE MIEMBROS[/bold cyan]")

    # Verificar si el diccionario está vacío
    if len(gimnasio) == 0:
        console.print("[red]⚠ No hay miembros registrados.[/red]\n")
        return

    # Crear la tabla con rich
    tabla = Table(title="Miembros del Gimnasio", border_style="cyan")

    # Definir las columnas de la tabla
    tabla.add_column("ID", style="yellow", justify="center")
    tabla.add_column("Nombre", style="white")
    tabla.add_column("Suscripción", style="green", justify="center")

    # Recorrer el diccionario y agregar cada miembro como fila
    for id_miembro, datos in gimnasio.items():
        tabla.add_row(
            id_miembro,
            datos["nombre"],
            datos["tipo_suscripcion"]
        )
        console.print(tabla)
 #-----------STEFYY- CREAR MIEMBRO----------------

#escribimos el mismo diccionario que esta en main para trabajar sobre los mismos datos
def crear_miembro(gimnasio):
    miembros = cargar_datos(Ruta_Json)
    console.print("\n[bold cyan]➕ CREAR NUEVO MIEMBRO[/bold cyan]")

    nombre = console.input("[green]Nombre del miembro: [/green]").strip()

    console.print("[green]Tipo de suscripción:[/green]")
    console.print("  [bold]1.[/bold] Mensual")
    console.print("  [bold]2.[/bold] Anual")

    try:
        opcion = int(console.input("[green]Elige (1 o 2): [/green]"))

        if opcion == 1:
            tipo = "Mensual"
        elif opcion == 2:
            tipo = "Anual"
        else:
            console.print("[red]⚠ Opción inválida.[/red]")
            return

        # Generar el ID automático contando cuántos miembros hay.

        nuevo_id = f"miembro_{len(miembros) + 1}"

        # Guardar el nuevo miembro en el diccionario
        miembros[nuevo_id] = {
            "nombre": nombre,
            "tipo_suscripcion": tipo
        }
        guardar_datos(Ruta_Json, miembros) 
        console.print(f"[bold ]✅ Miembro '{nombre}' creado con ID {nuevo_id}[/bold]\n")

    except ValueError:
        console.print("[red]⚠ Error: Ingresa solo números donde se piden.[/red]")

#----------------------ELIMINAR MIEMBRO----------------------

def eliminar_miembro(lista_miembros):
    lista_miembros = cargar_datos(Ruta_Json)
    eliminar_por_id = input("Ingrese el ID del miembro que deseas eliminar: ").lower()
    
    if eliminar_por_id in lista_miembros:
        lista_miembros.pop(eliminar_por_id)
        print(f"El ID {eliminar_por_id} fue eliminado exitosamente")
        
    else:
        print(f"El ID {eliminar_por_id} no se encuentra en la base de datos")


# -------------------EDITAR MIEMBRO----------------------

def actualizar_miembro (gimnasio: dict):
    gimnasio = cargar_datos(Ruta_Json)
    id_miembro = console.input("[green] id del miembro a editar: [/green]").strip()
    
    # nombre_clase = input("Nombre de la clase: ").strip()

    str_id_miembro = f"miembro_{id_miembro}"

    if str_id_miembro in gimnasio:
        info = gimnasio[str_id_miembro]
        print(f"¡Miembro encontrado!. proporciona los datos a editar del miembro: {str_id_miembro}")
        print("\nPresiona 'ENTER' sin escribir nada para mantener el valor actual\n")

        console.print(f"[green]El Nombre actual es:[/green] {info["nombre"]}")
        nuevo_nombre = console.input("[green]Elije el nuevo nombre, de lo contrario Presiona ENTER:[/green]")

        if nuevo_nombre != "":  #si el nuevo nombre no es el mismo no se actualiza, si es diferente se actualiza
            info["nombre"] = nuevo_nombre

        console.print(f"[green]Tipo de suscripción Actual:[/green] {info["tipo_suscripcion"]}")
        console.print("  Las Opciones para actualizar son:")
        console.print("  [bold]1.[/bold] Mensual")
        console.print("  [bold]2.[/bold] Anual")
        entrada_plan = int(console.input("[green]Elige (1 o 2) para actualizar, de lo contrario presiona ENTER: [/green]"))

        if entrada_plan != "":
            try:
                    nuevo_plan = int(entrada_plan)
                    if nuevo_plan == 1:
                        info["tipo_suscripcion"] = "Mensual"
                    elif nuevo_plan == 2:
                        info["tipo_suscripcion"] = "Anual"
                    else:
                        console.print("[red]⚠ Opción inválida. No se alteró el plan.[/red]")
            except ValueError:
                console.print("[red]⚠ Entrada inválida.[/red]")
                return

        # ------------Vinculo con json-------
                guardar_datos(Ruta_Json, gimnasio)
    else:
        print(f"❌❌❌El miembro con ese id {str_id_miembro} no existe❌❌❌")
