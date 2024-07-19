package get

import (
	interfacecine "Severl/interfacecine"
	"database/sql"
)

func GetComentario(db *sql.DB, id int) ([]interfacecine.Comentario, error) {
	// se filtra el comentario por el id de la pelicula
	var comentario interfacecine.Comentario
	sql := "SELECT * FROM comentarios_peli WHERE id_pelicula=?"
	consul, err := db.Query(sql, id)
	if err != nil {
		return nil, err
	}

	var comentarios []interfacecine.Comentario
	for consul.Next() {
		err = consul.Scan(&comentario.Id, &comentario.Comentario, &comentario.Id_usuario, &comentario.Id_pelicula)
		if err != nil {
			return nil, err
		}
		comentarios = append(comentarios, comentario)
	}

	return comentarios, nil
}
