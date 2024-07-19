def obtener_id_genero(seleccion):
    """
    Obtiene el ID del género a partir de la selección en el menú desplegable.

    Parameters:
    - seleccion (str): La cadena seleccionada en el menú desplegable, que incluye el nombre del género y su ID entre paréntesis.

    Returns:
    - int: El ID del género.

    Raises:
    - ValueError: Si la selección está vacía o no se puede obtener el ID del género.
    """
    if not seleccion:
        raise ValueError("La selección está vacía.")
    
    try:
        id_str = seleccion.split("(")[-1].strip(")")
        return int(id_str)
    except (IndexError, ValueError) as e:
        raise ValueError(f"Error al obtener el ID del género de '{seleccion}': {e}")

def GeneroEntry(parent, campos, entries, valorPordefecto=None):
    """
    Crea un campo de entrada para seleccionar un género usando un menú desplegable.

    Parameters:
    - parent (ctk.CTkFrame): El contenedor principal donde se ubicará el campo de entrada.
    - campos (list): Lista de campos existentes, utilizada para determinar la fila en la que se ubicará el nuevo campo.
    - entries (dict): Diccionario para almacenar la referencia del menú desplegable.
    - valorPordefecto (str, optional): Valor por defecto para el menú desplegable.

    Returns:
    - genero_var (ctk.StringVar): Variable que contiene la selección del menú desplegable.
    - genero_menu (ctk.CTkOptionMenu): El widget del menú desplegable.
    - entries (dict): El diccionario actualizado con la referencia del menú desplegable.
    """
    import customtkinter as ctk
    from hooks.Peticiones.getGenero import getAllGeneros
    generos = getAllGeneros()

    # Crear la variable del menú desplegable y la etiqueta
    genero_var = ctk.StringVar()
    ctk.CTkLabel(parent, text="Género:").grid(row=len(campos), column=0, padx=10, pady=5, sticky="nsew")
    
    # Crear el menú desplegable con los nombres y IDs de los géneros
    genero_menu = ctk.CTkOptionMenu(parent, values=[f"{g['nombre']} ({g['id']})" for g in generos], variable=genero_var)
    genero_menu.grid(row=len(campos), column=1, padx=10, pady=5, sticky="nsew")
    
    # Establecer el valor por defecto si se proporciona
    if valorPordefecto:
        genero_var.set(valorPordefecto)
    
    # Almacenar la referencia del menú desplegable en el diccionario entries
    entries["genero"] = genero_var
    
    return genero_var, genero_menu, entries
