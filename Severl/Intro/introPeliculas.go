package intro

import (
	interfacecine "Severl/interfacecine"
	"database/sql"
)

func IntroPeliculas(db *sql.DB, infoPeli interfacecine.Pelicula) error {
	sql := "INSERT INTO pelicula (nombre, img, descri, dura, trailers, genero_id) VALUES (?, ?, ?, ?, ?, ?)"
	_, err := db.Exec(sql, infoPeli.Nombre, infoPeli.Img, infoPeli.Descri, infoPeli.Dura, infoPeli.Trailer, infoPeli.Genero_id)
	if err != nil {
		return err
	}
	return nil
}

func IntroEstrenos(db *sql.DB, infoEstrenos interfacecine.EstrenoAndSlider) error {
	sql := "INSERT INTO estrenos (id_pelicula) VALUES (?)"
	_, err := db.Exec(sql, infoEstrenos.IdPelicula)
	if err != nil {
		return err
	}
	return nil
}

func IntroSlider(db *sql.DB, infoSlider interfacecine.EstrenoAndSlider) error {
	sql := "INSERT INTO slider (id_pelicula) VALUES (?)"
	_, err := db.Exec(sql, infoSlider.IdPelicula)
	if err != nil {
		return err
	}
	return nil
}
