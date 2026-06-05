# main.py
import sys
import os
from rich.console import Console
# Importamos todos los módulos centralizados de la carpeta modules
import modules.miembros as miembros
import modules.clases as clases
import modules.inscripciones as inscripciones

# Asegurar que Python reconozca la raíz del proyecto para las importaciones
directorio_raiz = os.path.dirname(os.path.abspath(__file__))
if directorio_raiz not in sys.path:
    sys.path.append(directorio_raiz)



console = Console()

def mostrar_menu():
    """Imprime las opciones del menú principal procesando los estilos de Rich."""
    console.print("\n[bold blue]============= 🏋️‍♂️ GESTIÓN DEL GIMNASIO =============[/bold blue]")
    console.print("[bold cyan]1.[/bold cyan] Gestión de Miembros (Submenú)")
    console.print("[bold cyan]2.[/bold cyan] Gestión de Clases (Submenú)")
    console.print("[bold cyan]3.[/bold cyan] Gestión de Inscripciones y Cupos (Submenú)") 
    console.print("[bold red]0.[/bold red] Salir del Sistema")

def main():
    while True:
        mostrar_menu()
        
        # console.input captura la opción limpia de espacios
        opcion = console.input("\n[bold yellow]Seleccione una opción: [/bold yellow]").strip()

        if opcion == "1":
            console.print("[green]🔄 Cargando módulo de miembros...[/green]")
            # Llamada al submenú interactivo de miembros.py
            miembros.menu_miembros()
            
        elif opcion == "2":
            console.print("[green]🔄 Cargando módulo de clases...[/green]")
            # Llamada al submenú interactivo de clases.py
            clases.menu_principal()
            
        elif opcion == "3":
            console.print("[green]🔄 Cargando módulo de inscripciones...[/green]")
            # Llamada al submenú interactivo de inscripciones.py
            inscripciones.menu_inscripciones()
            
        elif opcion == "0":
            console.print("\n[bold green]👋 ¡Gracias por usar el sistema del gimnasio! Hasta luego.[/bold green]\n")
            break
        else:
            console.print("[bold red]⚠ Opción inválida. Intente de nuevo.[/bold red]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]👋 Programa cerrado desde el teclado.[/bold red]\n")