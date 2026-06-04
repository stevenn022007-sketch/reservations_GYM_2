# main.py
import readchar
from rich.console import Console
from rich.panel import Panel

# Importaciones ajustadas para no generar advertencias en Ruff
from modules.data import guardar_datos
import modules.miembros as miembros
import modules.clases as clases
import modules.inscripciones as inscripciones
import modules.reto_final as reto_final

console = Console()

RUTA_MIEMBROS = "data/miembros.json"

def esperar_tecla():
    console.print("\n[bold magenta]➔ Presione cualquier tecla para regresar al menú...[/bold magenta]")
    readchar.readkey()

def mostrar_menu():
    # Limpieza estética de consola
    console.print("\033[H\033[2J", end="") 
    menu_texto = (
        "[bold cyan]1.[/bold cyan] 👥 Ver Lista de Miembros\n"
        "[bold cyan]2.[/bold cyan] ➕ Registrar Nuevo Miembro\n"
        "[bold cyan]3.[/bold cyan] ✏️  Editar Datos de Miembro\n"
        "[bold cyan]4.[/bold cyan] ❌ Eliminar un Miembro\n"
        "[dashed cyan]--------------------------------------------------[/dashed cyan]\n"
        "[bold green]5.[/bold green] 🏋️‍♂️ Ver Todas las Clases\n"
        "[bold green]6.[/bold green] ➕ Crear Nueva Clase de Gimnasio\n"
        "[bold green]7.[/bold green] ✏️  Actualizar Datos de Clase\n"
        "[bold green]8.[/bold green] ❌ Eliminar una Clase\n"
        "[dashed cyan]--------------------------------------------------[/dashed cyan]\n"
        "[bold yellow]9.[/bold yellow] 📝 Inscribir Miembro en Clase ([bold red]Reto Cupos[/bold red])\n"
        "[bold yellow]a.[/bold yellow] 🥶 Dar de Baja Miembro de Clase\n"
        "[bold yellow]b.[/bold yellow] 🔍 Consultar Miembros por Clase\n"
        "[bold yellow]c.[/bold yellow] 🔍 Consultar Clases de un Miembro\n"
        "[dashed cyan]--------------------------------------------------[/dashed cyan]\n"
        "[bold red]0.[/bold red] 🚪 Salir de la Aplicación"
    )
    console.print(Panel(menu_texto, title="🏋️‍♂️ [bold magenta]SISTEMA GIMNASIO ADSO[/bold magenta] 🏋️‍♂️", border_style="magenta", expand=False))
    console.print("[bold yellow]Seleccione una opción: [/bold yellow]", end="")

def flujo_inscripcion():
    console.print("\n[bold yellow]📝 PROCESO DE INSCRIPCIÓN A CLASE[/bold yellow]")
    try:
        id_m_num = int(console.input("[green]Ingrese el número de ID del miembro (ej: 1): [/green]"))
        id_c_num = int(console.input("[green]Ingrese el número de ID de la clase (ej: 1): [/green]"))
    except ValueError:
        console.print("[red]⚠ Error: Los identificadores deben ser numéricos.[/red]")
        return

    str_id_miembro = f"miembro_{id_m_num}"
    str_id_clase = f"clase_{id_c_num}"

    # Cargar diccionarios usando las funciones nativas de tus módulos
    base_miembros = miembros.cargar_datos(RUTA_MIEMBROS)
    base_clases = clases.cargar_datos(clases.ruta)

    if str_id_miembro not in base_miembros:
        console.print(f"[red]❌ El miembro {str_id_miembro} no existe.[/red]")
        return
    if str_id_clase not in base_clases:
        console.print(f"[red]❌ La clase {str_id_clase} no existe.[/red]")
        return

    # Ejecución del validador de cupos (reto_final.py)
    if reto_final.validar_y_restar_cupo(base_clases, str_id_clase):
        exito_vinculo = inscripciones.vincular_miembros(base_miembros, base_clases, str_id_miembro, str_id_clase)
        
        if exito_vinculo:
            guardar_datos(clases.ruta, base_clases)
            console.print("[bold green]💾 Los cupos del gimnasio se han guardado con éxito.[/bold green]")
        else:
            reto_final.devolver_cupo_disponible(base_clases, str_id_clase)

def flujo_baja():
    console.print("\n[bold red]🥶 PROCESO DE DESVINCULACIÓN (DAR DE BAJA)[/bold red]")
    try:
        id_m_num = int(console.input("[green]Ingrese el número de ID del miembro (ej: 1): [/green]"))
        id_c_num = int(console.input("[green]Ingrese el número de ID de la clase (ej: 1): [/green]"))
    except ValueError:
        console.print("[red]⚠ Error: Los identificadores deben ser numéricos.[/red]")
        return

    str_id_miembro = f"miembro_{id_m_num}"
    str_id_clase = f"clase_{id_c_num}"

    base_clases = clases.cargar_datos(clases.ruta)

    if inscripciones.desvincular_miembro_de_clase(str_id_miembro, str_id_clase):
        reto_final.devolver_cupo_disponible(base_clases, str_id_clase)
        guardar_datos(clases.ruta, base_clases)
        console.print("[bold green]✅ Cupo reestablecido en la base de datos.[/bold green]")

def main():
    while True:
        mostrar_menu()
        
        # Aquí es donde 'readchar' se vuelve útil capturando la pulsación instantánea
        opcion = readchar.readkey().lower()
        console.print(f"[bold white]{opcion}[/bold white]\n") 

        if opcion == "1":
            base_m = miembros.cargar_datos(RUTA_MIEMBROS)
            miembros.ver_miembros(base_m)
            esperar_tecla()
        elif opcion == "2":
            base_m = miembros.cargar_datos(RUTA_MIEMBROS)
            miembros.crear_miembro(base_m)
            esperar_tecla()
        elif opcion == "3":
            base_m = miembros.cargar_datos(RUTA_MIEMBROS)
            miembros.actualizar_miembro(base_m)
            esperar_tecla()
        elif opcion == "4":
            base_m = miembros.cargar_datos(RUTA_MIEMBROS)
            miembros.eliminar_miembro(base_m)
            esperar_tecla()
        elif opcion == "5":
            clases.inspeccionar_clases()
            esperar_tecla()
        elif opcion == "6":
            clases.crear_clase()
            esperar_tecla()
        elif opcion == "7":
            clases.actualizar_clase()
            esperar_tecla()
        elif opcion == "8":
            clases.eliminar_clases()
            esperar_tecla()
        elif opcion == "9":
            flujo_inscripcion()
            esperar_tecla()
        elif opcion == "a":
            flujo_baja()
            esperar_tecla()
        elif opcion == "b":
            try:
                id_c = int(console.input("[green]Ingrese el número de la clase a consultar: [/green]"))
                base_m = miembros.cargar_datos(RUTA_MIEMBROS)
                inscripciones.mostrar_miembros_clase(base_m, id_c)
            except ValueError:
                console.print("[red]⚠ Entrada inválida.[/red]")
            esperar_tecla()
        elif opcion == "c":
            try:
                id_m = int(console.input("[green]Ingrese el número del miembro a consultar: [/green]"))
                base_c = clases.cargar_datos(clases.ruta)
                inscripciones.mostrar_clases_miembro(base_c, id_m)
            except ValueError:
                console.print("[red]⚠ Entrada inválida.[/red]")
            esperar_tecla()
        elif opcion == "0":
            console.print("\n[bold green]👋 ¡Sistema cerrado con éxito! Vuelve pronto.[/bold green]\n")
            break
        else:
            console.print("\n[bold red]⚠ Opción inválida. Intente de nuevo.[/bold red]")
            esperar_tecla()

if __name__ == "__main__":
    main()