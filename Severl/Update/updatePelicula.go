package update

import (
	interfacecine "Severl/interfacecine"
	"database/sql"
)

func UpdatePelicula(db *sql.DB, infoPeli interfacecine.Pelicula) error {
	sql := "UPDATE pelicula SET nombre = ?, img = ?, descri = ?, dura = ?, trailers = ?, genero_id = ? WHERE id = ?"
	_, err := db.Exec(sql, infoPeli.Nombre, infoPeli.Img, infoPeli.Descri, infoPeli.Dura, infoPeli.Trailer, infoPeli.Genero_id, infoPeli.Id)
	if err != nil {
		return err
	}
	return nil
}
