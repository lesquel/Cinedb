package update

import (
	interfacecine "Severl/interfacecine"
	"database/sql"
)

func UpdateFunciones(db *sql.DB, infoFunciones interfacecine.Funciones) error {
	// Actualiza la tabla comentarios
	stmt, err := db.Prepare("UPDATE funciones SET fecha = ?, id_salas = ?, id_peliculas = ? WHERE id = ?")
	if err != nil {
		return err
	}
	defer stmt.Close()
	_, err = stmt.Exec(infoFunciones.Fecha, infoFunciones.IdSala, infoFunciones.IdPeliculas, infoFunciones.Id)
	if err != nil {
		return err
	}
	return nil
}
