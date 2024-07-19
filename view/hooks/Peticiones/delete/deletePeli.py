import requests
from tkinter import messagebox


def eliminar_pelicula(pelicula, main_frame, ventana, infoUser):
    """
    Elimina una película de la base de datos y actualiza la tabla de películas en la interfaz gráfica.

    Args:
    - pelicula: Información de la película que se va a eliminar.
    - main_frame: Marco principal de la aplicación donde se muestra la tabla de películas.
    - ventana: Ventana principal de la aplicación.
    - infoUser: Información del usuario actual.

    Returns:
    - JSON: Respuesta de la solicitud HTTP DELETE si la eliminación fue exitosa, None si no se realizó.

    Notes:
    - Muestra un mensaje de confirmación antes de proceder con la eliminación.
    - Realiza una solicitud HTTP DELETE para eliminar la película por su ID.
    - Si la eliminación es exitosa (código de estado 200), muestra un mensaje de éxito y actualiza la tabla de películas.
    - Maneja errores mostrando un mensaje en la consola si la eliminación no se pudo completar.
    """
    from components.tablaCrud.tablaPelicula import TablaPelicula
    # Mostrar un mensaje de confirmación para la eliminación
    confirmar = messagebox.askyesno("Eliminar", "¿Estás seguro de eliminar la película?")
    
    if confirmar:
        # Construir la URL para la solicitud DELETE
        url = f"http://localhost:8080/deletePelicula?id={pelicula['id']}"
        
        # Realizar la solicitud DELETE para eliminar la película
        response = requests.delete(url)
        
        # Verificar el código de estado de la respuesta
        if response.status_code == 200:
            # Mostrar mensaje de éxito y actualizar la tabla de películas
            messagebox.showinfo("Eliminar", "La película se ha eliminado correctamente")
            TablaPelicula(main_frame=main_frame, infoUser=infoUser, ventana=ventana)
            return response.json()  # Devolver la respuesta en formato JSON
        else:
            # Manejar caso de error en la respuesta
            print(f"Error: {response.status_code} - {response.text}")
            return None
    else:
        return None  # No se confirma la eliminación, retornar None
