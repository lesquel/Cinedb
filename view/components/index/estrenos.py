import customtkinter as ctk
from components.Text import Text
from components.Button import Button
from components.Img import Img
from EditPeli_Admin import EditAdmin
from Salas import Salas
from hooks.Peticiones.GetSliderAndEstreno import GetEstrenoPage
from hooks.Peticiones.GetPeli import GetPeliId

def Estrenos(parent, infoUser, ventana, page=1):
    from hooks.destuirTodo import destuirTodo
    destuirTodo(ventana=parent)

    def Ventana(infoPelicula, idUsuario):
        # Mostrar la sala de la película seleccionada
        frame2 = Salas(ventana=ventana, infoPelicula=infoPelicula, idUsuario=idUsuario)

    def VentanaAdmin(infoPelicula, infoUser):
        # Mostrar la ventana de edición para la película seleccionada
        frame2 = EditAdmin(ventana=ventana, infoUser=infoUser, infoPelicula=infoPelicula)

    # Obtener estrenos de la página actual
    estrenos = GetEstrenoPage(page=page, limit=4)

    def PintarEstrenos():
        # Si no hay estrenos, no se muestra nada
        fila = 1
        columna = 0
        if not estrenos:
            ctk.CTkLabel(parent, text="No hay más estrenos", font=("Arial", 24), corner_radius=20).grid(row=1, column=0, columnspan=3, padx=10, pady=10)
            return fila
        
        # Añadir título al frameEstrenos
        ctk.CTkLabel(parent, text="Todos los estrenos", font=("Arial", 24), corner_radius=20).grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Crear un marco para los estrenos
        frame = ctk.CTkFrame(parent, corner_radius=20)
        frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Iterar sobre los estrenos para crear widgets de visualización
        for estreno in estrenos:
            pelicula = GetPeliId(idPelicula=estreno["id_pelicula"])
            # Crear un marco para el estreno
            marco_estreno = ctk.CTkFrame(frame, corner_radius=10, border_width=2)
            marco_estreno.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")

            # Mostrar la imagen del estreno
            Img(marco_estreno, pelicula["img"])

            # Crear un marco para el nombre del estreno
            marco_nombre = ctk.CTkFrame(marco_estreno, fg_color="transparent") 
            marco_nombre.grid(row=1, column=0, pady=(0, 10))

            # Mostrar el nombre y duración del estreno
            Text(marco_nombre, texto=pelicula["nombre"], tamanio=16).grid(row=0, column=0, padx=10, pady=5, sticky="w")
            Text(marco_nombre, texto=f"Duración: {pelicula['dura']}H", tamanio=16).grid(row=1, column=0, padx=10, pady=5, sticky="w")

            # Botón para ver más detalles o editar el estreno
            if infoUser["admin"]:
                # Crear un botón para editar el estreno (solo para administradores)
                Button(marco_estreno, texto="Editar", tamanio=16, eventoClick=lambda infoPelicula=pelicula, infoUser=infoUser: VentanaAdmin(infoPelicula, infoUser)).grid(row=4, column=0, padx=10, pady=5)
            else:
                # Crear un botón para ver la sala del pel
                Button(marco_estreno, texto="Ver", tamanio=16, eventoClick=lambda infoPelicula=pelicula, idUsuario=infoUser["id"]: Ventana(infoPelicula, idUsuario)).grid(row=4, column=0, padx=10, pady=5)
        
            # Actualizar las posiciones de fila y columna
            columna += 1
            if columna >= 4:
                columna = 0
                fila += 1

        return fila
    
    fila = PintarEstrenos()

    # Crear botones de paginación si hay más páginas disponibles
    paginacion_frame = ctk.CTkFrame(parent)
    paginacion_frame.grid(row=fila+1, column=0, pady=10, sticky="nsew")

    # Verificar si hay más estrenos en la siguiente página
    hay_mas_estrenos = (GetEstrenoPage(page=page+1, limit=4))

    # Botón Anterior
    if page > 1:
        btn_anterior = Button(paginacion_frame, texto="Anterior", tamanio=16, eventoClick=lambda: Estrenos(parent, infoUser, ventana, page=page-1))
        btn_anterior.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Botón Siguiente
    if hay_mas_estrenos:
        btn_siguiente = Button(paginacion_frame, texto="Siguiente", tamanio=16, eventoClick=lambda: Estrenos(parent, infoUser, ventana, page=page+1))
        btn_siguiente.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
