package peliculas

import (
	"database/sql"
	"encoding/json"
	"net/http"
	"strconv"

	delete "Severl/Delete"
	get "Severl/Get"
	hooks "Severl/Hooks"
	intro "Severl/Intro"
	update "Severl/Update"
	interfacecine "Severl/interfacecine"
)

func HandleGetPeliculas(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		paguina, _ := strconv.Atoi(r.URL.Query().Get("page"))
		limit, _ := strconv.Atoi(r.URL.Query().Get("limit"))
		datos, err := get.GetPeliculasPagination(db, paguina, limit)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleGetPeliculasAll(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		datos, err := get.GetPeliculasAll(db)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleGetPeliculaId(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		id, _ := strconv.Atoi(r.URL.Query().Get("id"))
		datos, err := get.GetPeliculaId(db, id)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleGetPeliculasByGenero(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		id, _ := strconv.Atoi(r.URL.Query().Get("id"))
		datos, err := get.GetPeliculasByGenero(db, id)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleGetPeliculasByNombre(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		nombre := r.URL.Query().Get("nombre")
		datos, err := get.GetPeliculasByNombre(db, nombre)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleIntroGenero(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		// Obtener parámetros de la URL
		nombre := r.URL.Query().Get("nombre")

		// Insertar la película en la base de datos
		err := intro.IntroGenero(db, nombre)
		if err != nil {
			http.Error(w, "Failed to insert movie", http.StatusInternalServerError)
			return
		}
		// Responder con éxito
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}

func HandleGetGenero(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		id, _ := strconv.Atoi(r.URL.Query().Get("id"))
		datos, err := get.GetGenero(db, id)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleGetAllGenero(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		datos, err := get.GetAllGenero(db)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleUpdateGenero(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		var infoGenero interfacecine.Genero
		infoGenero.Id, _ = strconv.Atoi(r.URL.Query().Get("id"))
		infoGenero.Nombre = r.URL.Query().Get("nombre")
		err := update.UpdateGenero(db, infoGenero)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}

func HandleDeleteGenero(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		id, _ := strconv.Atoi(r.URL.Query().Get("id"))
		err := delete.DeleteGenero(db, id)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}

func HandleIntroPelicula(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)

		// Obtener parámetros de la URL
		nombre := r.URL.Query().Get("nombre")
		generoID, _ := strconv.Atoi(r.URL.Query().Get("genero_id"))
		dura := r.URL.Query().Get("dura")
		trailers := r.URL.Query().Get("trailers")
		descri := r.URL.Query().Get("descri")
		imgURL := r.URL.Query().Get("img")

		// Descargar la imagen y obtener la URL completa
		imgURL, err := hooks.DownloadFile(imgURL)
		if err != nil {
			http.Error(w, "Failed to download image", http.StatusInternalServerError)
			return
		}

		// Preparar la estructura de datos de la película
		infoPeli := interfacecine.Pelicula{
			Nombre:    nombre,
			Genero_id: generoID,
			Dura:      dura,
			Trailer:   trailers,
			Descri:    descri,
			Img:       imgURL, // Aquí asignamos la URL de la imagen descargada
		}

		// Insertar la película en la base de datos
		err = intro.IntroPeliculas(db, infoPeli)
		if err != nil {
			http.Error(w, "Failed to insert movie", http.StatusInternalServerError)
			return
		}

		// Responder con éxito
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}

func HandleUpdatePelicula(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		var infoPeli interfacecine.Pelicula
		infoPeli.Id, _ = strconv.Atoi(r.URL.Query().Get("id"))
		infoPeli.Nombre = r.URL.Query().Get("nombre")
		infoPeli.Img = r.URL.Query().Get("img")
		infoPeli.Descri = r.URL.Query().Get("descri")
		infoPeli.Dura = r.URL.Query().Get("dura")
		infoPeli.Trailer = r.URL.Query().Get("trailers")
		infoPeli.Genero_id, _ = strconv.Atoi(r.URL.Query().Get("genero_id"))
		err := update.UpdatePelicula(db, infoPeli)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}

func HandleDeletePelicula(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		id, _ := strconv.Atoi(r.URL.Query().Get("id"))
		err := delete.DeletePelicula(db, id)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}

func HandleGetEstrenos(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		id, _ := strconv.Atoi(r.URL.Query().Get("id"))
		datos, err := get.GetEstrenos(db, id)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleGetEstrenosPagination(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		paguina, _ := strconv.Atoi(r.URL.Query().Get("page"))
		limit, _ := strconv.Atoi(r.URL.Query().Get("limit"))
		datos, err := get.GetEstrenosPagination(db, paguina, limit)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleGetEstrenosAll(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		datos, err := get.GetEstrenosAll(db)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleGetSlider(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		id, _ := strconv.Atoi(r.URL.Query().Get("id"))
		datos, err := get.GetSlider(db, id)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleGetSliderAll(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		datos, err := get.GetSliderAll(db)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleIntroEstrenos(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		// Obtener parámetros de la URL

		var infEstreno interfacecine.EstrenoAndSlider
		infEstreno.IdPelicula, _ = strconv.Atoi(r.URL.Query().Get("idPelicula"))

		// Insertar la película en la base de datos
		err := intro.IntroEstrenos(db, infEstreno)
		if err != nil {
			http.Error(w, "Failed to insert movie", http.StatusInternalServerError)
			return
		}
		// Responder con éxito
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}

func HandleIntroSlider(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		// Obtener parámetros de la URL
		var infSlider interfacecine.EstrenoAndSlider
		infSlider.IdPelicula, _ = strconv.Atoi(r.URL.Query().Get("idPelicula"))

		// Insertar la película en la base de datos
		err := intro.IntroSlider(db, infSlider)
		if err != nil {
			http.Error(w, "Failed to insert movie", http.StatusInternalServerError)
			return
		}
		// Responder con éxito
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}

func HandleDeleteEstrenos(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		id, _ := strconv.Atoi(r.URL.Query().Get("id"))
		err := delete.DeleteEstrenos(db, id)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}

func HandleDeleteSlider(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		id, _ := strconv.Atoi(r.URL.Query().Get("id"))
		err := delete.DeleteSlider(db, id)
		if err != nil {
			http.Error(w, "Failed to get peliculas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}
