import time
import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.box import ROUNDED

# Inicializamos la consola de Rich para los colores y estilos
console = Console()

# Intentar importar tus funciones de datos, si no, dejamos el mock para que no falle
try:
    from data import cargar_datos, guardar_datos
except ImportError:
    _MOCK_DB = {
        "1": {"nombre_clase": "Zumba Fit", "instructor": "María", "horario": "mañana", "cupo_maximo": 20},
        "2": {"nombre_clase": "Spinning", "instructor": "Juan", "horario": "tarde", "cupo_maximo": 15}
    }
    def cargar_datos(r): return _MOCK_DB
    def guardar_datos(r, d): global _MOCK_DB; _MOCK_DB = d

ruta = "data/clases.json"
HORARIOS_VALIDOS = ["mañana", "tarde", "noche"]

# ==============================================================================
# SUB-FUNCIONES VISUALES (EFECTOS LLAMATIVOS)
# ==============================================================================

def limpiar_pantalla():
    """Limpia la consola para que todo se vea ordenado."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_barra_carga(mensaje_bonito):
    """Muestra una barra de progreso animada y super llamativa."""
    with Progress(
        SpinnerColumn(spinner_name="bouncingBar", style="bold magenta"),
        TextColumn(f"[bold cyan]{mensaje_bonito}[/bold cyan]"),
        BarColumn(bar_width=30, style="bright_black", complete_style="bold green"),
        console=console,
        transient=True # Al terminar se borra para no ensuciar la pantalla
    ) as progress:
        tarea = progress.add_task("", total=100)
        while not progress.finished:
            progress.update(tarea, advance=10)
            time.sleep(0.05)

# ==============================================================================
# TU LÓGICA ORIGINAL ENRIQUECIDA CON RICH
# ==============================================================================

def inspeccionar_clases():
    datos_actuales = cargar_datos(ruta)
    
    # Creamos una tabla espectacular en lugar de los prints planos
    tabla = Table(
        title="✨ [bold lgt_green]LISTADO DE CLASES REGISTRADAS[/bold lgt_green] ✨",
        box=ROUNDED,
        border_style="bold magenta",
        header_style="bold reverse cyan"
    )
    
    tabla.add_column("🆔 ID", justify="center")
    tabla.add_column("📚 Clase", justify="left")
    tabla.add_column("👨‍🏫 Instructor", justify="left")
    tabla.add_column("🕒 Horario", justify="center")
    tabla.add_column("👥 Cupo Max", justify="right")

    for clase, datos in datos_actuales.items():
        tabla.add_row(
            f"[bold yellow]{clase}[/bold yellow]",
            str(datos.get("nombre_clase", "")),
            str(datos.get("instructor", "")),
            str(datos.get("horario", "")).capitalize(),
            f"[bold green]{datos.get('cupo_maximo', '')}[/bold green]"
        )
        
    console.print("\n")
    console.print(tabla)
    console.print("\n")

            
def crear_clase():
    console.print(Panel("🆕 [bold list_magenta]REGISTRAR NUEVA CLASE[/bold list_magenta]", border_style="cyan", box=ROUNDED))
    entrada_de_datos = cargar_datos(ruta)
    
    while True:
        # Usamos los colores de Rich dentro del input tradicional
        nombre_clase = console.input("📝 [bold yellow]Ingrese el nombre de la nueva clase:[/bold yellow] ")
        instructor = console.input("👨‍🏫 [bold yellow]Ingrese un nuevo instructor (o el anterior):[/bold yellow] ")
        
        if nombre_clase != "" and instructor != "":
            break
        console.print("[bold red]❌ Intenta de nuevo, ninguno de los campos puede quedar vacío...[/bold red]")
            
    # Validación del horario con opciones permitidas
    while True:
        horario_clase = console.input("🕒 [bold cyan]Ingrese el horario de la clase (Mañana, Tarde o Noche):[/bold cyan] ").strip().lower()
        if horario_clase not in HORARIOS_VALIDOS:
            console.print(f"[bold red]❌ Horario inválido.[/bold red] Las opciones válidas son: [bold yellow]{', '.join(HORARIOS_VALIDOS)}.[/bold yellow]")
            
        if horario_clase in HORARIOS_VALIDOS:
            break

    while True:
        try:
            cupo_maximo = int(console.input("👥 [bold magenta]Ingrese el cupo máximo de la clase:[/bold magenta] "))
            if cupo_maximo <= 0:
                console.print("[bold red]❌ El cupo debe ser un número entero mayor que 0.[/bold red]") 
                continue    
        except ValueError:
            console.print("[bold red]❌ El cupo debe ser un valor numérico entero.[/bold red]")
        else:
            break

    # Creamos un Nuevo id automatico 
    if entrada_de_datos:
        ids_numericos = [int(id_actual) for id_actual in entrada_de_datos.keys() if id_actual.isdigit()]
        nuevo_id = f"{max(ids_numericos) + 1}"
    else:
        nuevo_id = "1"
    
    datos_clase = {
        "nombre_clase": nombre_clase,
        "instructor": instructor,
        "horario": horario_clase,
        "cupo_maximo": cupo_maximo
    }
    
    entrada_de_datos[nuevo_id] = datos_clase
    
    # AGREGADO: Efecto visual de guardado
    mostrar_barra_carga("💾 Guardando nueva clase en el sistema...")
    
    guardar_datos(ruta, entrada_de_datos)
    console.print(f"[bold green]✅ ¡Clase #{nuevo_id} creada exitosamente![/bold green]")
    inspeccionar_clases()


def eliminar_clases():
    console.print(Panel("🗑️ [bold red]ELIMINAR CLASE DEL SISTEMA[/bold red]", border_style="red", box=ROUNDED))
    entrada_de_datos = cargar_datos(ruta)
    inspeccionar_clases()
    
    eliminar_clase_por_id = console.input("🚨 [bold yellow]Ingrese la clase que desea eliminar por ID:[/bold yellow] ").lower()
    
    if eliminar_clase_por_id in entrada_de_datos:
        entrada_de_datos.pop(eliminar_clase_por_id)
        
        # AGREGADO: Efecto de barra al eliminar
        mostrar_barra_carga(f"🔥 Eliminando clase #{eliminar_clase_por_id}...")
        
        console.print(f"[bold green]🗑️ El ID {eliminar_clase_por_id} fue eliminado exitosamente[/bold green]")
        guardar_datos(ruta, entrada_de_datos)
    else:
        console.print(f"[bold red]❌ El ID {eliminar_clase_por_id} no existe.[/bold red]")
    time.sleep(2)
    
    
def actualizar_clase():
    console.print(Panel("🔄 [bold orange3]ACTUALIZAR DATOS DE UNA CLASE[/bold orange3]", border_style="orange3", box=ROUNDED))
    entrada_datos = cargar_datos(ruta)
    inspeccionar_clases()
    
    id_miembro = console.input("🔍 [bold yellow]Ingrese el ID de la clase para actualizar:[/bold yellow] ")
    
    if id_miembro in entrada_datos:
        while True:
            nuevo_nombre_clase = console.input("📝 [bold cyan]Ingrese el nombre de la nueva clase:[/bold cyan] ")
            nuevo_instructor = console.input("👨‍🏫 [bold cyan]Ingrese un nuevo instructor (o el anterior):[/bold cyan] ")
            if nuevo_nombre_clase != "" and nuevo_instructor != "":
                break
            console.print("[bold red]❌ Intenta de nuevo, ninguno de los campos puede quedar vacío...[/bold red]")
    
        while True:
            nuevo_horario_clase = console.input("🕒 [bold cyan]Ingrese el horario de la nueva clase (Mañana, Tarde o Noche):[/bold cyan] ").strip().lower()
            if nuevo_horario_clase not in HORARIOS_VALIDOS:
                console.print(f"[bold red]❌ Horario inválido.[/bold red] Las opciones válidas son: [bold yellow]{', '.join(HORARIOS_VALIDOS)}.[/bold yellow]")
                
            if nuevo_horario_clase in HORARIOS_VALIDOS:
                break
    
        while True:
            try:
                nuevo_cupo_maximo = int(console.input("👥 [bold magenta]Ingrese el cupo máximo de la nueva clase:[/bold magenta] "))
                if nuevo_cupo_maximo <= 0:
                    console.print("[bold red]❌ El cupo debe ser un número entero mayor que 0.[/bold red]") 
                    continue    
            except ValueError:
                console.print("[bold red]❌ El cupo debe ser un valor numérico entero.[/bold red]")
            else:
                break
            
        # modificar datos
        entrada_datos[id_miembro]["nombre_clase"] = nuevo_nombre_clase
        entrada_datos[id_miembro]["instructor"] = nuevo_instructor
        entrada_datos[id_miembro]["horario"] = nuevo_horario_clase
        entrada_datos[id_miembro]["cupo_maximo"] = nuevo_cupo_maximo
        
        # AGREGADO: Efecto de barra al actualizar
        mostrar_barra_carga("⚡ Sincronizando cambios...")
        
        guardar_datos(ruta, entrada_datos)
        console.print("[bold green]✨ ¡Clase modificada con éxito! ✨[/bold green]")
        inspeccionar_clases()
    else:
        console.print(f"[bold red]❌❌❌ La clase con ese id {id_miembro} no existe ❌❌❌[/bold red]")
    time.sleep(2)


# ==============================================================================
# INTERFAZ DE MENÚ PRINCIPAL
# ==============================================================================

def menu_principal():
    """Bucle del menú para usar todas las funciones cómodamente."""
    while True:
        limpiar_pantalla()
        
        # Cabecera llamativa
        console.print(Panel(
            "[bold blink magenta]💪 FITNESS APP MANAGEMENT SYSTEM 💪[/bold blink magenta]\n[bold cyan]Control y gestión de horarios y clases[/bold cyan]", 
            border_style="bold green", 
            box=ROUNDED,
            expand=False
        ))
        
        # Opciones visuales del menú
        console.print("[bold magenta][1][/bold magenta] 📊 Visualizar Clases Activas")
        console.print("[bold magenta][2][/bold magenta] 🆕 Registrar una Nueva Clase")
        console.print("[bold magenta][3][/bold magenta] 🔄 Modificar una Clase Existente")
        console.print("[bold magenta][4][/bold magenta] 🗑️ Eliminar una Clase del Sistema")
        console.print("[bold red][5] ❌ Salir[/bold red]")
        console.print("—" * 40, style="bright_black")
        
        opcion = console.input("🚀 [bold yellow]Seleccione una opción (1-5):[/bold yellow] ").strip()
        
        if opcion == "1":
            limpiar_pantalla()
            inspeccionar_clases()
            console.input("\n[bold white]Presione [Enter] para volver al menú...[/bold white]")
        elif opcion == "2":
            limpiar_pantalla()
            crear_clase()
            console.input("\n[bold white]Presione [Enter] para volver al menú...[/bold white]")
        elif opcion == "3":
            limpiar_pantalla()
            actualizar_clase()
            console.input("\n[bold white]Presione [Enter] para volver al menú...[/bold white]")
        elif opcion == "4":
            limpiar_pantalla()
            eliminar_clases()
            console.input("\n[bold white]Presione [Enter] para volver al menú...[/bold white]")
        elif opcion == "5":
            limpiar_pantalla()
            mostrar_barra_carga("Cerrando el sistema de forma segura")
            console.print("[bold magenta]👋 ¡Gracias por usar Fitness App! Hasta pronto.[/bold magenta]\n")
            break
        else:
            console.print("[bold red]⚠ Opción inválida. Intente de nuevo.[/bold red]")
            time.sleep(1)

# Punto de entrada para ejecutar la app
if __name__ == "__main__":
    menu_principal()

            
            
        
            

    
