package interfacecine

type EstrenoAndSlider struct {
	Id         int `json:"id"`
	IdPelicula int `json:"id_pelicula"`
}

// Struct Definitions
type Salas struct {
	Id       int    `json:"id"`
	Nombre   string `json:"nombre"`
	Fillas   int    `json:"fillas"`
	Columnas int    `json:"columnas"`
}

type Funciones struct {
	Id          int    `json:"id"`
	Fecha       string `json:"fecha"`
	IdSala      int    `json:"idSala"`
	IdPeliculas int    `json:"idPeliculas"`
	Sillas      string `json:"sillas"`
}
type Peliculas []Pelicula // Peliculas es un slice de Peliula

type Pelicula struct {
	Id        int    `json:"id"`
	Nombre    string `json:"nombre"`
	Img       string `json:"img"`
	Descri    string `json:"descri"`
	Dura      string `json:"dura"`
	Trailer   string `json:"trailer"`
	Genero_id int    `json:"genero"`
}
type Usuario struct {
	Id     int    `json:"id"`
	Nombre string `json:"nombre"`
	Contra string `json:"contra"`
	Img    string `json:"img"`
	Edad   int    `json:"edad"`
	Name   string `json:"name"`
	Correo string `json:"correo"`
	Admin  bool   `json:"admin"`
}
type Respuesta struct {
	Estabien int `json:"estabien"`
}
type Genero struct {
	Id     int    `json:"id"`
	Nombre string `json:"nombre"`
}
type Comentario struct {
	Id          int    `json:"id"`
	Comentario  string `json:"comentario"`
	Id_usuario  int    `json:"id_usuario"`
	Id_pelicula int    `json:"id_pelicula"`
}
