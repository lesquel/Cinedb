package funciones

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

func HandleGetFunciones(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		idPelicula, _ := strconv.Atoi(r.URL.Query().Get("idPelicula"))
		datos, err := get.GetFunciones(db, idPelicula)
		if err != nil {
			http.Error(w, "Failed to get funciones", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleUpdateSillas(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		sillas := r.URL.Query().Get("sillas")
		id, _ := strconv.Atoi(r.URL.Query().Get("id"))

		if err := update.UpdateSillas(db, id, sillas); err != nil {
			http.Error(w, "Failed to update sillas", http.StatusInternalServerError)
			return
		}
		response := interfacecine.Respuesta{Estabien: 1}
		json.NewEncoder(w).Encode(response)
	}
}

func HandleDeleteFunciones(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		id, _ := strconv.Atoi(r.URL.Query().Get("id"))

		if err := delete.DeleteFunciones(db, id); err != nil {
			http.Error(w, "Failed to delete funciones", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}

func HandleUpdateFunciones(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		var infoFunciones interfacecine.Funciones
		infoFunciones.Id, _ = strconv.Atoi(r.URL.Query().Get("id"))
		infoFunciones.Fecha = r.URL.Query().Get("fecha")
		infoFunciones.IdSala, _ = strconv.Atoi(r.URL.Query().Get("idSala"))
		infoFunciones.IdPeliculas, _ = strconv.Atoi(r.URL.Query().Get("idPeliculas"))
		if err := update.UpdateFunciones(db, infoFunciones); err != nil {
			http.Error(w, "Failed to update funciones", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}

func HandleIntroFunciones(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		var infoFunciones interfacecine.Funciones
		infoFunciones.Fecha = r.URL.Query().Get("fecha")
		infoFunciones.IdSala, _ = strconv.Atoi(r.URL.Query().Get("idSala"))
		infoFunciones.IdPeliculas, _ = strconv.Atoi(r.URL.Query().Get("idPeliculas"))
		infoFunciones.Sillas = r.URL.Query().Get("sillas")
		if err := intro.IntroFunciones(db, infoFunciones); err != nil {
			http.Error(w, "Failed to insert funciones", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}

func HandleGetFuncionesAll(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		datos, err := get.GetFuncionesAll(db)
		if err != nil {
			http.Error(w, "Failed to get funciones", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}
