from concurrent.futures import ThreadPoolExecutor

def ModelRequest(func, *args):
    """
    Ejecuta una función de manera asíncrona utilizando un ThreadPoolExecutor.

    Args:
    - func: Función a ejecutar de manera asíncrona.
    - *args: Argumentos de la función `func`.

    Returns:
    - El resultado de la función `func` después de haberse ejecutado.
    """
    with ThreadPoolExecutor() as executor:
        # Ejecutar la función `func` con los argumentos `args` en el ThreadPoolExecutor
        future = executor.submit(func, *args)
        # Obtener el resultado de la ejecución de la función
        result = future.result()
        return result
