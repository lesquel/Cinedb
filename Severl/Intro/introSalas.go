package intro

import (
	interfacecine "Severl/interfacecine"
	"database/sql"
)

func IntroSalas(db *sql.DB, infoSala interfacecine.Salas) error {
	sql := "INSERT INTO salas (nombre, fillas, columnas) VALUES (?, ?, ?)"
	stmt, err := db.Prepare(sql)
	if err != nil {
		return err
	}
	_, err = stmt.Exec(infoSala.Nombre, infoSala.Fillas, infoSala.Columnas)
	if err != nil {
		return err
	}
	return nil
}
