package intro

import (
	"database/sql"
)

func IntroGenero(db *sql.DB, nombre string) error {
	stmt, err := db.Prepare("INSERT INTO genero (nombre) VALUES (?)")
	if err != nil {
		return err
	}
	_, err = stmt.Exec(nombre)
	if err != nil {
		return err
	}
	return nil
}
