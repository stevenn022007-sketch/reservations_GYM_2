# reservations_GYM_2

# Reservations_GYM

Descripción: Se quiere crear una aplicación para administrar los miembros de un
gimnasio Crud Completo, las clases que se ofrecen y las inscripciones de los miembros a
estas clases.

Entidades y Relaciones:
1. Miembros: id_miembro, nombre, tipo_suscripcion (ej. "Mensual",
"Anual").
2. Clases: id_clase, nombre_clase, instructor, horario,
cupo_maximo.
3. Inscripciones: Cada inscripción será un objeto que vincula
un id_miembro con un id_clase.

Funcionalidades Clave:
-- CRUD completo para Miembros y Clases.

-- Inscribir un miembro en una clase (y validar que haya cupo
disponible).

-- Dar de baja a un miembro de una clase.

-- Mostrarla lista de miembros inscritos en una clase específica.

-- Mostrar todas las clases en las que está inscrito un miembro.

ESTÁNDARES DE CALIDAD:
-- Git y GitHub: El proyecto debe estar en un único repositorio de GitHub. Se
evaluará el uso de commits atómicos y con mensajes claros.

-- EntornoVirtual con venv:El proyecto debe ser gestionado con VENV.

-- Modularidad (Funciones): Toda la lógica debe estar encapsulada en
funciones con una única responsabilidad (Principio de Responsabilidad
Única). Debe haber funciones para cargar datos, guardar datos, mostrar menús,
y para cada una de las operaciones CRUD.

-- Manejo de Errores: La aplicación debe ser robusta. Utilicen bloques try-except
para validar las entradas del usuario (ej. que un número sea realmente un número)
y para manejar errores de archivos (ej. FileNotFoundError).

-- Cada proyecto debe utilizar archivo JSON. Un archivo .json donde guarda
los datos.

-- La aplicación debe implementar un CRUD completo (Crear, Leer, Actualizar,
Eliminar) para las entidades principales.

-- Se debe implementar lógica para crear y leerlas entidades relacionales.

-- rich es obligatorio: Todos los menús, tablas de datos, mensajes de éxito y error
deben ser presentados de forma profesional utilizando la librería rich. ¡Hagan que
su aplicación sea agradable de usar!

-- Búsqueda y Filtrado: La aplicación debe ofrecer funcionalidades de búsqueda que
permitan al usuario encontrar información

IMPORTANTE: 
Rutas o mensajes de los commits a cualquier funcionalidad nueva o cambios en la funcionalidad:

Fix -> Se coloca en el mensaje del commit fix si se arreglo o se modifico alguna funcionalidad. EJM: fix: se arreglo funcionalidad eliminar_cliente.

Add -> Si se agrego una funcionalidad nueva EJM: Add: se agrego funcionalidad eliminar_cliente.

library -> Si agregaron alguna libreria y donde la utilizaron ESPECIFICAR EN QUE LINEA DE CODIGO ESTAN utilizando la libreria EJM: library: se agrego la liberia match en la linea 32.

modified -> Para cambios pequeños de estrutura de codigo
