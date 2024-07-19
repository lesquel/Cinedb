package intro

import "database/sql"

func IntroComentario(db *sql.DB, comentario string, id_pelicula int, id_usuario int) error {
	sql := "INSERT INTO comentarios_peli (comentario, id_pelicula, id_usuario) VALUES (?, ?, ?)"
	_, err := db.Exec(sql, comentario, id_pelicula, id_usuario)
	if err != nil {
		return err
	}
	return nil
}
