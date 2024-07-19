package update

import (
	"database/sql"
)

func UpdateSala(db *sql.DB, id int, nombre string, fillas int, columnas int) error {
	stmt, err := db.Prepare("UPDATE salas SET nombre=?, fillas=?, columnas=? WHERE id=?")
	if err != nil {
		return err
	}
	defer stmt.Close()
	_, err = stmt.Exec(nombre, fillas, columnas, id)
	if err != nil {
		return err
	}

	return nil
}
