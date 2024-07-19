package get

import (
	"database/sql"

	"Severl/interfacecine"

	_ "github.com/go-sql-driver/mysql"
)

func GetUsuario(db *sql.DB, nombre string, contra string) (interfacecine.Usuario, error) {
	rows, err := db.Query("SELECT * FROM user WHERE nombre = ? AND contra = ?", nombre, contra)
	if err != nil {
		return interfacecine.Usuario{}, err
	}
	defer rows.Close()
	// Log para verificar si se encontraron filas
	if !rows.Next() {
		return interfacecine.Usuario{}, sql.ErrNoRows
	}
	var usuario interfacecine.Usuario
	// Escanear los resultados
	if err := rows.Scan(&usuario.Id, &usuario.Nombre, &usuario.Contra, &usuario.Img, &usuario.Edad, &usuario.Name, &usuario.Correo, &usuario.Admin); err != nil {
		return interfacecine.Usuario{}, err
	}

	return usuario, nil
}

func GetUsuarioId(db *sql.DB, id int) (interfacecine.Usuario, error) {
	rows, err := db.Query("SELECT * FROM user WHERE id = ?", id)
	if err != nil {
		return interfacecine.Usuario{}, err
	}
	defer rows.Close()

	// Log para verificar si se encontraron filas
	if !rows.Next() {
		return interfacecine.Usuario{}, sql.ErrNoRows
	}

	var usuario interfacecine.Usuario
	if err := rows.Scan(&usuario.Id, &usuario.Nombre, &usuario.Contra, &usuario.Img, &usuario.Edad, &usuario.Name, &usuario.Correo, &usuario.Admin); err != nil {
		return interfacecine.Usuario{}, err
	}
	return usuario, nil
}
