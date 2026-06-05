
# Traemos la herramienta para pintar la pantalla con textos de colores
from rich.console import Console
# Traemos los dos botones que fabricamos para abrir y guardar los archivos del computador
from modules.data import cargar_datos, guardar_datos
# Traemos las reglas del juego final para controlar si hay o no espacio en los salones
import modules.reto_final as reto_final
from rich.panel import Panel
from rich.table import Table

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
    Submenú encargado de gestionar las inscripciones de los miembros
    a las clases del gimnasio.

    El menú permanece activo dentro de un ciclo infinito hasta que
    el usuario seleccione la opción 0 para regresar al menú principal.
    """
    while True:
        # Limpia completamente la consola antes de volver a dibujar el menú.
        # Esto evita que se acumulen pantallas una debajo de otra.

        console.clear()
        
        # -----------------------------------------------------------------
        # CREACIÓN DEL TÍTULO
        # -----------------------------------------------------------------

        # Panel.fit() crea un cuadro cuyo tamaño se ajusta al contenido.
        # border_style define el color del borde.
        titulo = Panel.fit(
            "[bold magenta]📝 GESTIÓN DE INSCRIPCIONES Y CUPOS[/bold magenta]",
            border_style="magenta"
        )

        # Muestra el panel en pantalla.
        console.print(titulo)

        # -----------------------------------------------------------------
        # CREACIÓN DE LA TABLA DE OPCIONES
        # -----------------------------------------------------------------

        # Creamos una tabla con encabezados visibles.
        # header_style define el color y estilo de los encabezados.

        tabla = Table(show_header=True, header_style="bold cyan")
        
        # Primera columna:
        # justify="center" centra el texto.
        # width=10 establece un ancho fijo.
        tabla.add_column("Opción", justify="center", width=10)

        # Segunda columna:
        # Contendrá la descripción de cada acción.
        tabla.add_column("Descripción", width=50)

        # Agregamos cada fila del menú.
        tabla.add_row("1", "Inscribir Miembro en Clase")
        tabla.add_row("2", "Dar de Baja Miembro de Clase")
        tabla.add_row("3", "Consultar Miembros por Clase")
        tabla.add_row("4", "Consultar Clases de un Miembro")
        tabla.add_row("0", "Volver al Menú Principal")

        # Imprime la tabla completa.
        console.print(tabla)

        # -----------------------------------------------------------------
        # CAPTURA DE LA OPCIÓN DEL USUARIO
        # -----------------------------------------------------------------

        # Solicita al usuario que seleccione una opción.
        # strip() elimina espacios al inicio y final.
        opcion = console.input(
            "\n[bold yellow]Seleccione una opción:[/bold yellow] "
        ).strip()

        # -----------------------------------------------------------------
        # CONTROL DE OPCIONES
        # -----------------------------------------------------------------

        # Opción 1:
        # Llama al proceso encargado de inscribir miembros.
        if opcion == "1":
            flujo_inscripcion()

        # Opción 2:
        # Llama al proceso encargado de dar de baja miembros.
        elif opcion == "2":
            flujo_baja()

        # Opción 3:
        # Aquí irá la lógica para consultar los miembros
        # inscritos en una clase específica.
        elif opcion == "3":
            try:
                # Pide el número de la clase (por ejemplo: 1)
                id_c_num = console.input("[green]Ingrese el número de la clase a consultar (ej: 1): [/green]").strip()
                if not id_c_num.isdigit():
                    raise ValueError
                
                # Abre la lista de personas registradas en el gimnasio
                base_m = cargar_datos(Ruta_Miembros)
                # Llama a la función que los dibuja en la pantalla
                mostrar_miembros_clase(base_m, id_c_num)
            except ValueError:
                # Si el usuario escribe letras en vez de un número, muestra este aviso para que no se apague el programa
                console.print("[red]⚠ Entrada inválida. Ingrese solo el número de ID.[/red]")

        # Si escribe 4, intenta mostrar a qué clases asiste una persona específica
        elif opcion == "4":
            try:
                # Pide el número de la persona (por ejemplo: 1)
                id_m_num = console.input("[green]Ingrese el número del miembro a consultar (ej: 1): [/green]").strip()
                if not id_m_num.isdigit():
                    raise ValueError
                
                # Abre la lista de clases disponibles
                base_c = cargar_datos(Ruta_Clases)
                # Llama a la función que las dibuja en la pantalla
                mostrar_clases_miembro(base_c, id_m_num)
            except ValueError:
                # Si escribe letras en vez de números, frena el error y avisa
                console.print("[red]⚠ Entrada inválida. Ingrese solo el número de ID.[/red]")
        # Opción 0:
        # Rompe el ciclo while y regresa al menú principal.
        elif opcion == "0":
            break
        
        # Si el usuario escribe cualquier otra cosa.
        else:
            console.print(          # Muestra un mensaje de error en color rojo.
                "\n[bold red]⚠ Opción inválida.[/bold red]"
            )
# =====================================================================
#  FLUJOS INTERNOS DE CONTROL
# =====================================================================
def flujo_inscripcion():
    # Muestra un letrero amarillo avisando que inicia la inscripción
    console.print("\n[bold yellow]📝 PROCESO DE INSCRIPCIÓN A CLASE[/bold yellow]")
    
    # Pide los identificadores evitando que falle si digitan letras, validando con .isdigit()
    id_m_num = console.input("[green]Ingrese el número de ID del miembro (ej: 1): [/green]").strip()
    id_c_num = console.input("[green]Ingrese el número de ID de la clase (ej: 1): [/green]").strip()
    
    if not id_m_num.isdigit() or not id_c_num.isdigit():
        # Si el usuario digita mal y pone letras, detiene el proceso con este aviso
        console.print("[red]⚠ Error: Los identificadores deben ser numéricos.[/red]")
        return 

    # Formatos por defecto combinados con texto
    str_id_miembro = f"miembro_{id_m_num}"
    str_id_clase = f"clase_{id_c_num}"

    # Va al disco duro y trae los papeles actualizados de los miembros y de las clases
    base_miembros = cargar_datos(Ruta_Miembros)
    base_clases = cargar_datos(Ruta_Clases)

    # --- 🛠️ BUSCADOR INTELIGENTE Y MULTI-TIPO PARA MIEMBROS ---
    llave_miembro_real = None
    if str_id_miembro in base_miembros:
        llave_miembro_real = str_id_miembro          # Formato "miembro_1"
    elif id_m_num in base_miembros:
        llave_miembro_real = id_m_num                # Formato Texto "1"
    elif int(id_m_num) in base_miembros:
        llave_miembro_real = int(id_m_num)           # Formato Entero 1

    # --- 🛠️ BUSCADOR INTELIGENTE Y MULTI-TIPO PARA CLASES ---
    llave_clase_real = None
    if str_id_clase in base_clases:
        llave_clase_real = str_id_clase              # Formato "clase_1"
    elif id_c_num in base_clases:
        llave_clase_real = id_c_num                  # Formato Texto "1"
    elif int(id_c_num) in base_clases:
        llave_clase_real = int(id_c_num)             # Formato Entero 1

    # Si no se encontró el miembro usando ninguna de las tres formas, cancela
    if llave_miembro_real is None:
        console.print(f"[red]❌ El miembro '{id_m_num}' no existe en el sistema.[/red]")
        return
        
    # Si no se encontró la clase usando ninguna de las tres formas, cancela
    if llave_clase_real is None:
        console.print(f"[red]❌ La clase '{id_c_num}' no existe en el sistema.[/red]")
        # Imprime las llaves actuales en consola para ayudarte a diagnosticar visualmente si es necesario
        console.print(f"[yellow]💡 Llaves detectadas en tu JSON de clases: {list(base_clases.keys())}[/yellow]")
        return

    # Llama al otro archivo usando la llave real encontrada (str o int) para comprobar cupos
    if reto_final.validar_y_restar_cupo(base_clases, llave_clase_real):
        # Si había espacio, intenta hacer la unión oficial usando las llaves validadas
        exito_vinculo = vincular_miembros(base_miembros, base_clases, llave_miembro_real, llave_clase_real)
        
        # Si la unión se logró sin problemas...
        if exito_vinculo:
            # Guarda en el computador la lista de clases con el cupo restado
            guardar_datos(Ruta_Clases, base_clases)
            console.print("[bold green]💾 Los cupos del gimnasio se han guardado con éxito.[/bold green]")
        else:
            # Si el miembro ya estaba inscrito, devolvemos la silla usando la llave exacta
            reto_final.devolver_cupo_disponible(base_clases, llave_clase_real)
            
    # Agregamos una pausa para que main.py no limpie la pantalla de golpe
    console.input("\n[bold white]Presione [Enter] para continuar...[/bold white]")

def flujo_baja():
    # Muestra un letrero rojo avisando que inicia el retiro
    console.print("\n[bold red]🥶 PROCESO DE DESVINCULACIÓN (DAR DE BAJA)[/bold red]")
    
    # Pide los números del alumno y de la clase que va a abandonar limpiamente
    id_m_num = console.input("[green]Ingrese el número de ID del miembro (ej: 1): [/green]").strip()
    id_c_num = console.input("[green]Ingrese el número de ID de la clase (ej: 1): [/green]").strip()
    
    if not id_m_num.isdigit() or not id_c_num.isdigit():
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
        console.print("[yellow]El miembro ya está inscrito en esta clase.[/yellow]")
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
    
    # Preparamos los dos formatos posibles en los que pudo haberse guardado ("1" o "clase_1")
    id_puro = str(id_clase_num).strip()
    str_id_clase = f"clase_{id_puro}".lower()
    
    console.print(f"\n[bold cyan] Miembros inscritos en CLASE {id_puro}:[/bold cyan]")

    encontrados = False # Un interruptor para saber si encontramos al menos a una persona
    
    # Empieza a revisar todos los registros de inscripciones
    for datos in inscripciones.values():
        val_json = str(datos["id_clase"]).strip().lower()
        
        # Validamos contra ambos formatos posibles para no fallar nunca
        if val_json == str_id_clase or val_json == id_puro:
            m_id = datos["id_miembro"] # Saca el código del alumno (ej: "miembro_1" o "1")
            m_id_puro = m_id.replace("miembro_", "") # Saca el número limpio por si acaso
            
            # Busca en el archivo del gimnasio cómo se llama ese código real probando todas las llaves posibles
            nombre_m = "Desconocido"
            if m_id in gimnasio_dict:
                nombre_m = gimnasio_dict[m_id]["nombre"]
            elif m_id_puro in gimnasio_dict:
                nombre_m = gimnasio_dict[m_id_puro]["nombre"]
                
            # Muestra el nombre en la pantalla con un puntito de lista
            console.print(f"  - {m_id}: [bold]{nombre_m}[/bold]")
            encontrados = True # Enciende el interruptor porque sí encontramos a alguien

    # Si al final de revisar todo, el interruptor siguió apagado, avisa que el salón está vacío
    if not encontrados:
        console.print("[yellow] ⚠ No hay miembros registrados o inscritos en esta clase. [/yellow]")
        
    # 🚨 PAUSA CRÍTICA: Detiene la pantalla para que el console.clear() de main.py no borre el resultado
    console.input("\n[bold white]Presione [Enter] para volver al menú de inscripciones...[/bold white]")


def mostrar_clases_miembro(clases_dict, id_miembro_num):
    # Abre el archivo de inscripciones del computador
    inscripciones = cargar_datos(Ruta_Json)
    
    # Preparamos los dos formatos posibles en los que pudo haberse guardado ("1" o "miembro_1")
    id_puro = str(id_miembro_num).strip()
    str_id_miembro = f"miembro_{id_puro}".lower()
    
    console.print(f"\n[bold cyan] Clases asignadas al MIEMBRO {id_puro}:[/bold cyan]")
    
    encontrados = False # Otro interruptor para saber si la persona tiene clases o no
    
    # Revisa cada una de las inscripciones del gimnasio
    for datos in inscripciones.values():
        val_json = str(datos["id_miembro"]).strip().lower()
        
        # Si la inscripción le pertenece al alumno que estamos consultando...
        if val_json == str_id_miembro or val_json == id_puro:
            c_id = datos["id_clase"] # Saca el código de la clase (ej: "clase_1" o "1")
            c_id_puro = c_id.replace("clase_", "")
            
            # Va a los papeles de clases y saca la información de esa clase.
            info_c = {}
            if c_id in clases_dict:
                info_c = clases_dict[c_id]
            elif c_id_puro in clases_dict:
                info_c = clases_dict[c_id_puro]
                
            # Extrae el nombre real de la clase
            nombre_c = info_c.get("nombre_clase", "Desconocida")
            
            # Pinta en la pantalla el código y el nombre de la actividad
            console.print(f"  - {c_id}: [bold]{nombre_c}[/bold]")
            encontrados = True # Activa el interruptor porque encontramos al menos una clase
            
    # Si terminó la lista y el alumno no tenía nada registrado, muestra este mensaje amarillo
    if not encontrados:
        console.print("[yellow] ⚠ Este miembro no tiene clases asignadas.[/yellow]")
        
    # 🚨 PAUSA CRÍTICA: Detiene la pantalla para que el console.clear() de main.py no borre el resultado
    console.input("\n[bold white]Presione [Enter] para volver al menú de inscripciones...[/bold white]")