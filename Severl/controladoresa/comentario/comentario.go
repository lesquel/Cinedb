package comentario

import (
	get "Severl/Get"
	intro "Severl/Intro"
	"database/sql"
	"encoding/json"
	"net/http"
	"strconv"
)

func HandleGetComentario(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		id, _ := strconv.Atoi(r.URL.Query().Get("idPelicula"))
		datos, err := get.GetComentario(db, id)
		if err != nil {
			http.Error(w, "Failed to get comentario", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleInsertComentario(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		comentario := r.URL.Query().Get("comentario")
		id_pelicula, _ := strconv.Atoi(r.URL.Query().Get("idPelicula"))
		id_usuario, _ := strconv.Atoi(r.URL.Query().Get("idUsuario"))
		err := intro.IntroComentario(db, comentario, id_pelicula, id_usuario)
		if err != nil {
			http.Error(w, "Failed to insert comentario", http.StatusInternalServerError)
			return
		}
		w.WriteHeader(http.StatusOK)
	}
}
