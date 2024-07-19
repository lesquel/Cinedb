import webbrowser

def AbrirTrailer(trailer_url):
    """
    Abre el enlace del tráiler en el navegador por defecto del sistema.

    Args:
    - trailer_url (str): URL del tráiler a abrir en el navegador.

    Returns:
    - None
    """
    # Abrir el enlace del tráiler en el navegador por defecto
    webbrowser.open(trailer_url)
