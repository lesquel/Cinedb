def Cambiar_Guardar(b, r, c, matriz):
    """
    Cambia el estado de una posición específica en una matriz entre 'L', 'S' y 'R'.

    Args:
    - b: Valor que indica el estado actual de la celda (no se utiliza explícitamente en la función).
    - r (int): Índice de fila en la matriz.
    - c (int): Índice de columna en la matriz.
    - matriz (list): Matriz representada como una lista de listas.

    Returns:
    - list: La matriz modificada después de cambiar el estado en la posición (r, c).
    """
    if matriz[r][c] == 'L':
        matriz[r][c] = 'S'
    elif matriz[r][c] == 'S':
        matriz[r][c] = 'L'
    elif matriz[r][c] == 'R':
        matriz[r][c] = 'S'
    
    return matriz
