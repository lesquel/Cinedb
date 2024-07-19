package user

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

func HandleGetUsuario(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		nombre := r.URL.Query().Get("nombre")
		contra := r.URL.Query().Get("contra")
		datos, err := get.GetUsuario(db, nombre, contra)
		if err != nil {
			http.Error(w, "Failed to get usuario", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleGetUsuarioId(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		id, _ := strconv.Atoi(r.URL.Query().Get("id"))
		datos, err := get.GetUsuarioId(db, id)
		if err != nil {
			http.Error(w, "Failed to get usuario", http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(datos)
	}
}

func HandleIntroUsuario(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		var infoUser interfacecine.Usuario
		infoUser.Nombre = r.URL.Query().Get("nombre")
		infoUser.Contra = r.URL.Query().Get("contra")
		infoUser.Edad, _ = strconv.Atoi(r.URL.Query().Get("edad"))
		infoUser.Name = r.URL.Query().Get("name")
		infoUser.Correo = r.URL.Query().Get("correo")
		infoUser.Admin, _ = strconv.ParseBool(r.URL.Query().Get("admin"))
		infoUser.Img, _ = hooks.DownloadFile(r.URL.Query().Get("img"))
		err := intro.IntroUser(db, infoUser)
		if err != nil {
			http.Error(w, "Failed to insert user", http.StatusInternalServerError)
			return
		}
		// Responder con éxito
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}

func HandleUpdateUsuario(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		var infoUser interfacecine.Usuario
		infoUser.Id, _ = strconv.Atoi(r.URL.Query().Get("id"))
		infoUser.Nombre = r.URL.Query().Get("nombre")
		infoUser.Contra = r.URL.Query().Get("contra")
		infoUser.Edad, _ = strconv.Atoi(r.URL.Query().Get("edad"))
		infoUser.Img, _ = hooks.DownloadFile(r.URL.Query().Get("img"))
		infoUser.Name = r.URL.Query().Get("name")
		infoUser.Correo = r.URL.Query().Get("correo")
		infoUser.Admin, _ = strconv.ParseBool(r.URL.Query().Get("admin"))
		err := update.UpdateUser(db, infoUser)
		if err != nil {
			http.Error(w, "Failed to update user", http.StatusInternalServerError)
			return
		}
		// Responder con éxito
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}
func HandleDeleteUsuario(db *sql.DB) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		hooks.SetCORSHeaders(w)
		id, _ := strconv.Atoi(r.URL.Query().Get("id"))
		err := delete.DeleteUsuario(db, id)
		if err != nil {
			http.Error(w, "Failed to delete user", http.StatusInternalServerError)
			return
		}
		// Responder con éxito
		json.NewEncoder(w).Encode(interfacecine.Respuesta{Estabien: 1})
	}
}
