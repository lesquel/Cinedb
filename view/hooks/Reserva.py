from components.Tiket import Tiket

def Reservar(frame, info, id, sillas, idUsuario, funcion, sala):
    """
    Handles the reservation process and displays the ticket.

    Args:
    - frame (tkinter.Frame): The parent frame where the ticket will be displayed.
    - info (dict): Information about the movie.
    - id (int): Identifier for the reservation.
    - sillas (list): Matrix representing the seats.
    - idUsuario (int): User identifier for the reservation.
    - funcion (dict): Details of the function or screening.
    - sala (dict): Details of the cinema hall or room.

    Returns:
    - None
    """
    # Importing Tiket from components.Tiket
    Tiket(parent=frame, matriz=sillas, idUsuario=idUsuario, infoPelicula=info, funcion=funcion, sala=sala)
