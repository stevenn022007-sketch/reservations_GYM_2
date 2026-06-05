# --------------CRUD--------MIEMBROS-----------------
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from modules.data import cargar_datos, guardar_datos 
# Qué necesita un miembro? -> id, nombre, tipo de suscripción
# console = Console()  # Inicializamos la consola de Rich para usarla en este módulo
#rich es una biblioteca de Python que permite crear interfaces de usuario en la terminal con estilos y colores. 
# En este código, se utiliza para imprimir mensajes estilizados y para manejar la entrada del usuario de manera más atractiva.
console = Console()
Ruta_Json = "data/miembros.json"

# -------MENU MIEMBROS-----------------
#el menú llama a las funciones que están debajo de él, y Python lee el archivo de arriba hacia abajo
def menu_miembros():
    while True:
        console.clear()
        menu_texto = (
            "[bold cyan]── 🏋️ GESTIÓN DE MIEMBROS 🏋️ ──[/bold cyan]\n\n"
            "[bold green]1.[/bold green] 👀 Ver Miembros\n"
            "[bold green]2.[/bold green] ➕ Crear Miembro\n"
            "[bold green]3.[/bold green] ❌ Eliminar Miembro\n"
            "[bold green]4.[/bold green] 📝 Editar Miembro\n\n"
            "[bold red]5.[/bold red] 🔙 Volver al Menú Principal"
        )
        '''Envuelve el texto en un recuadro visual. title es el texto que aparece arriba del recuadro, border_style es el color del borde y expand=False hace que el recuadro solo ocupe el ancho necesario en lugar de toda la pantalla.'''
        menu_panel = Panel(
            menu_texto,
            title="[bold yellow]👥 Miembros[/bold yellow]",
            border_style="cyan",
            expand=False
        )
        console.print(menu_panel)
        '''Captura el error cuando el usuario escribe letras en lugar de números. Sin esto el programa crashearía(significa que se detiene abruptamente y deja de funcionar debido a un error).'''
        try:
            opcion = int(console.input("\n[bold orange1]👉 Ingrese la opción (1 a 5): [/bold orange1]"))
        except ValueError:
            console.print("\n[bold red]⚠ Error: Por favor, introduce solo números.[/bold red]")
            continue
        #Evalúa qué número eligió el usuario y llama la función correspondiente.
        match opcion:
            case 1:
                miembros = cargar_datos(Ruta_Json)
                ver_miembros(miembros)
            case 2:
                miembros = cargar_datos(Ruta_Json)
                crear_miembro(miembros)
            case 3:
                miembros = cargar_datos(Ruta_Json)
                eliminar_miembro(miembros)
            case 4:
                miembros = cargar_datos(Ruta_Json)
                actualizar_miembro(miembros)
            case 5:
                console.print("\n[bold cyan]🔙 Volviendo al menú principal...[/bold cyan]\n")
                break
            case _:
                console.print("\n[bold red]❌ Opción inválida. Intenta de nuevo.[/bold red]")


# -------VER MIEMBROS-----------------
# que  tiene que hacer esta funcion? -> leer el diccionario de miembros y mostrarlo en una tabla
def ver_miembros(gimnasio=None):
    console.clear()
    # Cargamos los datos reales del JSON directamente
    gimnasio = cargar_datos(Ruta_Json)
    console.print("\n[bold cyan]👀 LISTA DE MIEMBROS[/bold cyan]")

    # Verificar si el diccionario está vacío
    if not gimnasio:
        console.print("[red]⚠ No hay miembros registrados.[/red]\\n")
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
    console.print("\n")
    console.input("[bold white]Presione [Enter] para volver al menú de miembros...[/bold white]")
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

        if miembros:
            ids_numericos = [int(id_actual) for id_actual in miembros.keys() if id_actual.isdigit()]
            nuevo_id = f"{max(ids_numericos) + 1}"
        else:
            nuevo_id = "1"

        # Guardar el nuevo miembro en el diccionario
        dato_miembro = {
            "nombre": nombre,
            "tipo_suscripcion": tipo
        }
        miembros[nuevo_id] = dato_miembro
        guardar_datos(Ruta_Json, miembros) 
        console.print(f"[bold ]✅ Miembro '{nombre}' creado con ID {nuevo_id}[/bold]\n")

    except ValueError:
        console.print("[red]⚠ Error: Ingresa solo números donde se piden.[/red]")

#----------------------ELIMINAR MIEMBRO----------------------

def eliminar_miembro(lista_miembros):
    lista_miembros = cargar_datos(Ruta_Json)
    eliminar_por_id = console.input("[green]Ingrese el ID del miembro que deseas eliminar: [/green]").lower()
    
    if eliminar_por_id in lista_miembros:
        lista_miembros.pop(eliminar_por_id)
        guardar_datos(Ruta_Json, lista_miembros)  # ← guardar en JSON
        console.print(f"[bold green]✅ El ID {eliminar_por_id} fue eliminado exitosamente[/bold green]")
    else:
        console.print(f"[bold red]❌ El ID {eliminar_por_id} no se encuentra en la base de datos[/bold red]")

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
        entrada_plan = console.input("[green]Elige (1 o 2) para actualizar, de lo contrario presiona ENTER: [/green]")

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
        console.print("[bold green]✨ ¡Miembro actualizado con éxito! ✨[/bold green]\n")
    else:
        console.print(f"❌❌❌El miembro con ese id {str_id_miembro} no existe❌❌❌")
