package intro

import (
	interfacecine "Severl/interfacecine"
	"database/sql"
)

func IntroFunciones(db *sql.DB, infoFunciones interfacecine.Funciones) error {
	// Inserta una nueva entrada en la tabla comentarios
	stmt, err := db.Prepare("INSERT INTO funciones (fecha, id_salas, id_peliculas, sillas) VALUES (?, ?, ?, ?)")
	if err != nil {
		return err
	}
	defer stmt.Close()
	_, err = stmt.Exec(infoFunciones.Fecha, infoFunciones.IdSala, infoFunciones.IdPeliculas, infoFunciones.Sillas)
	if err != nil {
		return err
	}
	return nil
}
