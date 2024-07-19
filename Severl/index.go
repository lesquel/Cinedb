package main

import (
	"log"
	"net/http"
	"path/filepath"

	// Ajusta la ruta completa según la estructura de tu proyecto

	conex "Severl/Conex"
	"Severl/controladoresa/comentario"
	funciones "Severl/controladoresa/funciones"
	peliculas "Severl/controladoresa/peliculas"
	salas "Severl/controladoresa/salas"
	user "Severl/controladoresa/user"

	_ "github.com/go-sql-driver/mysql"
)

func main() {

	db := conex.GetConexion()
	defer db.Close()

	mux := http.NewServeMux()
	assetsDir := filepath.Join(".", "assets")
	fs := http.FileServer(http.Dir(assetsDir))
	// Configurar el manejador para servir archivos estáticos desde la carpeta 'assets'
	mux.Handle("/assets/", http.StripPrefix("/assets/", fs))

	// http://localhost:8080/getSalas?idSalas=1
	mux.HandleFunc("/getSalas", salas.HandleGetSalas(db))
	// http://localhost:8080/getSalasAll
	mux.HandleFunc("/getSalasAll", salas.HandleGetSalasAll(db))
	// http://localhost:8080/UpdateSillas?id=1&sillas=[]
	mux.HandleFunc("/UpdateSillas", funciones.HandleUpdateSillas(db))
	// http://localhost:8080/getFunciones?idPelicula=1
	mux.HandleFunc("/getFunciones", funciones.HandleGetFunciones(db))
	// http://localhost:8080/getFuncionesAll
	mux.HandleFunc("/getFuncionesAll", funciones.HandleGetFuncionesAll(db))
	// http://localhost:8080/getPeliculas?page=1&limit=5
	mux.HandleFunc("/getPeliculas", peliculas.HandleGetPeliculas(db))
	// http://localhost:8080/getPeliculasAll
	mux.HandleFunc("/getPeliculasAll", peliculas.HandleGetPeliculasAll(db))
	// http://localhost:8080/getPeliculasByGenero?id=1
	mux.HandleFunc("/getPeliculasByGenero", peliculas.HandleGetPeliculasByGenero(db))
	// http://localhost:8080/getPeliculasByNombre?nombre=1
	mux.HandleFunc("/getPeliculasByNombre", peliculas.HandleGetPeliculasByNombre(db))
	// http://localhost:8080/getPeliculaId?id=1
	mux.HandleFunc("/getPeliculaId", peliculas.HandleGetPeliculaId(db))
	// http://localhost:8080/getUsuario?nombre=1&contra=1
	mux.HandleFunc("/getUsuario", user.HandleGetUsuario(db))
	// http://localhost:8080/getUsuarioId?id=1
	mux.HandleFunc("/getUsuarioId", user.HandleGetUsuarioId(db))
	// http://localhost:8080/getGenero?id=1
	mux.HandleFunc("/getGenero", peliculas.HandleGetGenero(db))
	// http://localhost:8080/getAllGenero
	mux.HandleFunc("/getAllGenero", peliculas.HandleGetAllGenero(db))
	// http://localhost:8080/getComentario?idPelicula=1
	mux.HandleFunc("/getComentario", comentario.HandleGetComentario(db))
	// http://localhost:8080/getEstrenos?id=1
	mux.HandleFunc("/getEstrenos", peliculas.HandleGetEstrenos(db))
	// http://localhost:8080/getEstrenosAll
	mux.HandleFunc("/getEstrenosAll", peliculas.HandleGetEstrenosAll(db))
	// http://localhost:8080/getEstrenosPagination?page=1&limit=5
	mux.HandleFunc("/getEstrenosPagination", peliculas.HandleGetEstrenosPagination(db))
	// http://localhost:8080/getSlider?id=1
	mux.HandleFunc("/getSlider", peliculas.HandleGetSlider(db))
	// http://localhost:8080/getSliderAll
	mux.HandleFunc("/getSliderAll", peliculas.HandleGetSliderAll(db))

	// http://localhost:8080/insertComentario?idPelicula=1&comentario=1
	mux.HandleFunc("/insertComentario", comentario.HandleInsertComentario(db))
	// http://localhost:8080/introPelicula?nombre=1&img=1&descri=1&dura=1&trailers=1&genero_id=1
	mux.HandleFunc("/insertPelicula", peliculas.HandleIntroPelicula(db))
	// http://localhost:8080/introUsuario?nombre=1&contra=1&img=1&name=1&correo=1&admin=1
	mux.HandleFunc("/introUsuario", user.HandleIntroUsuario(db))
	// http://localhost:8080/introGenero?nombre=1
	mux.HandleFunc("/introGenero", peliculas.HandleIntroGenero(db))
	// http://localhost:8080/introSala?nombre=1&fillas=1&columnas=1
	mux.HandleFunc("/introSala", salas.HandleInsertSalas(db))
	// http://localhost:8080/introFunciones?fecha=1&idSala=1&idPeliculas=1&sillas=1
	mux.HandleFunc("/introFunciones", funciones.HandleIntroFunciones(db))
	// http://localhost:8080/introEstrenos?idPelicula=1
	mux.HandleFunc("/introEstrenos", peliculas.HandleIntroEstrenos(db))
	// http://localhost:8080/introSlider?idPelicula=1
	mux.HandleFunc("/introSlider", peliculas.HandleIntroSlider(db))

	// introFunciones

	// http://localhost:8080/updatePelicula?id=1&nombre=1&img=1&descri=1&dura=1&trailers=1&genero_id=1
	mux.HandleFunc("/updatePelicula", peliculas.HandleUpdatePelicula(db))
	// http://localhost:8080/updateUsuario?id=1&nombre=1&contra=1&edad=1&img=1&name=1&correo=1&admin=0&edad=1
	mux.HandleFunc("/updateUsuario", user.HandleUpdateUsuario(db))
	// http://localhost:8080/updateGenero?id=1&nombre=1
	mux.HandleFunc("/updateGenero", peliculas.HandleUpdateGenero(db))
	// http://localhost:8080/updateSala?id=1&nombre=1&fillas=1&columnas=1
	mux.HandleFunc("/updateSala", salas.HandleUpdateSalas(db))
	// http://localhost:8080/updateFunciones?id=1&idSala=1&idPeliculas=1&fecha=1
	mux.HandleFunc("/updateFunciones", funciones.HandleUpdateFunciones(db))

	// http://localhost:8080/deletePelicula?id=1
	mux.HandleFunc("/deletePelicula", peliculas.HandleDeletePelicula(db))
	// http://localhost:8080/deleteUsuario?id=1
	mux.HandleFunc("/deleteUsuario", user.HandleDeleteUsuario(db))
	// http://localhost:8080/deleteGenero?id=1
	mux.HandleFunc("/deleteGenero", peliculas.HandleDeleteGenero(db))
	// http://localhost:8080/deleteSala?id=1
	mux.HandleFunc("/deleteSala", salas.HandleDeleteSalas(db))
	// http://localhost:8080/deleteFunciones?id=1
	mux.HandleFunc("/deleteFunciones", funciones.HandleDeleteFunciones(db))
	// http://localhost:8080/deleteEstrenos?id=1
	mux.HandleFunc("/deleteEstrenos", peliculas.HandleDeleteEstrenos(db))
	// http://localhost:8080/deleteSlider?id=1
	mux.HandleFunc("/deleteSlider", peliculas.HandleDeleteSlider(db))

	log.Println("Server is running on port 8080...")
	if err := http.ListenAndServe(":8080", mux); err != nil {
		log.Fatalf("Server failed to start: %v", err)
	}
}
