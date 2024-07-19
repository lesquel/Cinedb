package update

import (
	interfacecine "Severl/interfacecine"
	"database/sql"
)

func UpdateGenero(db *sql.DB, genero interfacecine.Genero) error {
	idGenero := genero.Id
	nombre := genero.Nombre
	stmt, err := db.Prepare("UPDATE genero SET nombre = ? WHERE id = ?")
	if err != nil {
		return err
	}
	_, err = stmt.Exec(nombre, idGenero)
	if err != nil {
		return err
	}
	return nil
}
