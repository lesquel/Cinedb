def agregar_datos(entries, campos, refrescar_tabla, datos, table_frame):
    """
    Agrega un nuevo dato a la lista de datos, actualiza la tabla y limpia los campos de entrada.

    Args:
    - entries: Diccionario de campos de entrada donde las claves son nombres de campos y los valores son objetos de entrada.
    - campos: Lista de nombres de campos que se deben agregar al nuevo dato.
    - refrescar_tabla: Función para refrescar la tabla con los datos actualizados.
    - datos: Lista que contiene todos los datos actuales que se muestran en la tabla.
    - table_frame: Marco de la tabla donde se muestra la información.

    Returns:
    - None
    """
    import customtkinter as ctk

    # Crear un nuevo dato a partir de los valores actuales en los campos de entrada
    nuevo_dato = {campo: entries[campo].get() for campo in campos}

    # Agregar el nuevo dato a la lista de datos
    datos.append(nuevo_dato)

    # Imprimir el nuevo dato agregado (opcional, para propósitos de depuración)
    print(f"Nuevo dato agregado: {nuevo_dato}")

    # Limpiar los campos de entrada después de agregar el dato
    for campo in campos:
        entries[campo].delete(0, ctk.END)

    # Actualizar la tabla para mostrar el nuevo dato
    refrescar_tabla(table_frame, datos, campos, entries)
