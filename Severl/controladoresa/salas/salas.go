package salas

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

func HandleGetSalas(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		idSalas, _ := strconv.Atoi(r.URL.Query().Get("idSalas"))
		datos, err := get.GetSala(db, idSalas)
		if err != nil {
			http.Error(w, "Failed to get salas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleGetSalasAll(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		datos, err := get.GetSalasAll(db)
		if err != nil {
			http.Error(w, "Failed to get salas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleInsertSalas(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		var infoSala interfacecine.Salas
		infoSala.Nombre = r.URL.Query().Get("nombre")
		infoSala.Fillas, _ = strconv.Atoi(r.URL.Query().Get("fillas"))
		infoSala.Columnas, _ = strconv.Atoi(r.URL.Query().Get("columnas"))

		err := intro.IntroSalas(db, infoSala)
		if err != nil {
			http.Error(w, "Failed to insert salas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}

func HandleDeleteSalas(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		id, _ := strconv.Atoi(r.URL.Query().Get("id"))
		err := delete.DeleteSala(db, id)
		if err != nil {
			http.Error(w, "Failed to delete salas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}

func HandleUpdateSalas(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		id, _ := strconv.Atoi(r.URL.Query().Get("id"))
		nombre := r.URL.Query().Get("nombre")
		fillas, _ := strconv.Atoi(r.URL.Query().Get("fillas"))
		columnas, _ := strconv.Atoi(r.URL.Query().Get("columnas"))
		err := update.UpdateSala(db, id, nombre, fillas, columnas)
		if err != nil {
			http.Error(w, "Failed to update salas", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}
