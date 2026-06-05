# 🏋️‍♂️ reservations_GYM_2

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Storage-JSON-orange?style=for-the-badge&logo=json&logoColor=white" alt="Storage JSON">
  <img src="https://img.shields.io/badge/UI-Rich--Library-purple?style=for-the-badge" alt="Rich Library">
</p>

---

## 📝 Descripción

> Se quiere crear una aplicación para administrar los miembros de un gimnasio **Crud Completo**, las clases que se ofrecen y las inscripciones de los miembros a estas clases.

---

## 📐 Entidades y Relaciones

A continuación se detallan las entidades principales del sistema y sus atributos:

| Entidad | Atributos / Estructura |
| :--- | :--- |
| **1. Miembros** | `id_miembro`, `nombre`, `tipo_suscripcion` *(ej. "Mensual", "Anual")* |
| **2. Clases** | `id_clase`, `nombre_clase`, `instructor`, `horario`, `cupo_maximo` |
| **3. Inscripciones** | Cada inscripción será un objeto que vincula un `id_miembro` con un `id_clase` |

---

## ⚡ Funcionalidades Clave

* ✨ **CRUD completo** para Miembros y Clases.
* 📌 **Inscribir un miembro** en una clase *(y validar que haya cupo disponible)*.
* ❌ **Dar de baja** a un miembro de una clase.
* 🔍 **Mostrar la lista** de miembros inscritos en una clase específica.
* 📋 **Mostrar todas las clases** en las que está inscrito un miembro.

---

## 💎 Estándares de Calidad

* 🐙 **Git y GitHub:** El proyecto debe estar en un único repositorio de GitHub. Se evaluará el uso de *commits atómicos* y con mensajes claros.
* 📦 **EntornoVirtual con venv:** El proyecto debe ser gestionado con **VENV**.
* 🧩 **Modularidad (Funciones):** Toda la lógica debe estar encapsulada en funciones con una única responsabilidad *(Principio de Responsabilidad Única)*. Debe haber funciones para cargar datos, guardar datos, mostrar menús, y para cada una de las operaciones CRUD.
* 🛡️ **Manejo de Errores:** La aplicación debe ser robusta. Utilicen bloques `try-except` para validar las entradas del usuario *(ej. que un número sea realmente un número)* y para manejar errores de archivos *(ej. FileNotFoundError)*.
* 💾 **Archivo JSON:** Cada proyecto debe utilizar archivo **JSON**. Un archivo `.json` donde guarda los datos.
* 🔄 **CRUD Completo:** La aplicación debe implementar un CRUD completo *(Crear, Leer, Actualizar, Eliminar)* para las entidades principales.
* 🔗 **Lógica Relacional:** Se debe implementar lógica para crear y leer las entidades relacionales.
* 🎨 **rich es obligatorio:** Todos los menús, tablas de datos, mensajes de éxito y error deben ser presentados de forma profesional utilizando la librería **rich**. *¡Hagan que su aplicación sea agradable de usar!*
* 🔎 **Búsqueda y Filtrado:** La aplicación debe ofrecer funcionalidades de búsqueda que permitan al usuario encontrar información.

---

## ⚠️ IMPORTANTE

### Rutas o mensajes de los commits a cualquier funcionalidad nueva o cambios en la funcionalidad:

* `Fix` $\rightarrow$ Se coloca en el mensaje del commit *fix* si se arreglo o se modifico alguna funcionalidad. 
    > **EJM:** `fix: se arreglo funcionalidad eliminar_cliente.`
* `Add` $\rightarrow$ Si se agrego una funcionalidad nueva.
    > **EJM:** `Add: se agrego funcionalidad eliminar_cliente.`
* `library` $\rightarrow$ Si agregaron alguna libreria y donde la utilizaron **ESPECIFICAR EN QUE LINEA DE CODIGO ESTAN** utilizando la libreria.
    > **EJM:** `library: se agrego la liberia match en la linea 32.`
* `modified` $\rightarrow$ Para cambios pequeños de estrutura de codigo.
* `fox` $\rightarrow$ cambios grandes como varias funciones y especificar que funciones.

---
