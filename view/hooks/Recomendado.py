def Recomendado(matriz):
    """
    Recomienda un asiento en la matriz de asientos.

    Args:
    - matriz: Matriz que representa la disposición de asientos ('L' para libre, 'R' para reservado).

    Returns:
    - Matriz con un asiento recomendado marcado como 'R'.
    """
    # Dimensiones de la matriz
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Calcular las columnas centrales
    centro_izquierda = (columnas // 2) - 1
    centro_derecha = columnas // 2

    # Lista de columnas para recorrer, empezando por el centro y moviéndose hacia los extremos
    columnas_ordenadas = list(range(centro_derecha, columnas)) + list(range(centro_izquierda, -1, -1))
    
    # Buscar 'R' en las columnas centrales y recomendar el primer asiento 'R' encontrado
    for i in range(filas):
        for j in columnas_ordenadas:
            if matriz[i][j] == 'R':
                return matriz  # Si encuentra 'R', devuelve la matriz sin cambios
    
    # Si no se encontró 'R' en las columnas centrales, buscar 'L' desde abajo hacia arriba
    for i in range(filas-1, -1, -1):
        for j in columnas_ordenadas:
            if matriz[i][j] == 'L':
                matriz[i][j] = 'R'
                return matriz  # Marcar la primera 'L' encontrada como 'R' y salir
    
    # Si no se encontraron 'L' ni 'R', devuelve la matriz original
    return matriz
