package get

import (
	interfacecine "Severl/interfacecine"
	"database/sql"

	_ "github.com/go-sql-driver/mysql"
)

func GetPeliculasPagination(db *sql.DB, page int, limit int) (interfacecine.Peliculas, error) { // Cambia el retorno a un slice de Pelicula
	// Calcular el offset a partir de la página y el límite
	offset := (page - 1) * limit
	rows, err := db.Query("SELECT * FROM pelicula LIMIT ? OFFSET ?", limit, offset) // Incluye trailer y genero_id en la consulta
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	var peliculas interfacecine.Peliculas // Cambia a un slice de Pelicula
	for rows.Next() {
		var p interfacecine.Pelicula // Cambia a Pelicula
		if err := rows.Scan(&p.Id, &p.Nombre, &p.Img, &p.Descri, &p.Dura, &p.Trailer, &p.Genero_id); err != nil {
			return nil, err
		}
		peliculas = append(peliculas, p)
	}
	return peliculas, nil
}

func GetPeliculaId(db *sql.DB, id int) (interfacecine.Pelicula, error) {
	sql := "SELECT * FROM pelicula WHERE id = ?"
	rss, err := db.Query(sql, id)
	var pelicula interfacecine.Pelicula
	if err != nil {
		return pelicula, err
	}
	defer rss.Close()
	for rss.Next() {
		if err := rss.Scan(&pelicula.Id, &pelicula.Nombre, &pelicula.Img, &pelicula.Descri, &pelicula.Dura, &pelicula.Trailer, &pelicula.Genero_id); err != nil {
			return pelicula, err
		}
	}
	return pelicula, err
}
func GetPeliculasAll(db *sql.DB) (interfacecine.Peliculas, error) {
	rows, err := db.Query("SELECT id, nombre FROM pelicula") // Incluye trailer y genero_id en la consulta
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	var peliculas interfacecine.Peliculas // Cambia a un slice de Pelicula
	for rows.Next() {
		var p interfacecine.Pelicula // Cambia a Pelicula
		if err := rows.Scan(&p.Id, &p.Nombre); err != nil {
			return nil, err
		}
		peliculas = append(peliculas, p)
	}
	return peliculas, nil
}

func GetPeliculasByGenero(db *sql.DB, idGenero int) (interfacecine.Peliculas, error) {
	sql := "SELECT * FROM pelicula WHERE genero_id = ?"
	rss, err := db.Query(sql, idGenero)
	if err != nil {
		return nil, err
	}
	defer rss.Close()
	var peliculas interfacecine.Peliculas // Cambia a un slice de Pelicula
	for rss.Next() {
		var p interfacecine.Pelicula // Cambia a Pelicula
		if err := rss.Scan(&p.Id, &p.Nombre, &p.Img, &p.Descri, &p.Dura, &p.Trailer, &p.Genero_id); err != nil {
			return nil, err
		}
		peliculas = append(peliculas, p)
	}
	return peliculas, nil
}

func GetPeliculasByNombre(db *sql.DB, nombre string) (interfacecine.Peliculas, error) {
	sql := "SELECT id, nombre, img, descri, dura, trailers, genero_id FROM pelicula WHERE LOWER(nombre) LIKE LOWER(?)"
	nombre = "%" + nombre + "%"
	rss, err := db.Query(sql, nombre)
	if err != nil {
		return nil, err
	}
	defer rss.Close()
	var peliculas interfacecine.Peliculas // Cambia a un slice de Pelicula
	for rss.Next() {
		var p interfacecine.Pelicula // Cambia a Pelicula
		if err := rss.Scan(&p.Id, &p.Nombre, &p.Img, &p.Descri, &p.Dura, &p.Trailer, &p.Genero_id); err != nil {
			return nil, err
		}
		peliculas = append(peliculas, p)
	}
	return peliculas, nil
}

func GetEstrenos(db *sql.DB, idEstreno int) (interfacecine.EstrenoAndSlider, error) {
	sql := "SELECT * FROM estrenos WHERE id = ?"
	rss, err := db.Query(sql, idEstreno)
	if err != nil {
		return interfacecine.EstrenoAndSlider{}, err
	}
	defer rss.Close()
	var estrenos interfacecine.EstrenoAndSlider
	for rss.Next() {
		if err := rss.Scan(&estrenos.Id, &estrenos.IdPelicula); err != nil {
			return interfacecine.EstrenoAndSlider{}, err
		}
	}
	return estrenos, nil
}

func GetEstrenosAll(db *sql.DB) ([]interfacecine.EstrenoAndSlider, error) {
	sql := "SELECT * FROM estrenos"
	rss, err := db.Query(sql)
	if err != nil {
		return []interfacecine.EstrenoAndSlider{}, err
	}
	defer rss.Close()
	var estrenos []interfacecine.EstrenoAndSlider
	for rss.Next() {
		var e interfacecine.EstrenoAndSlider
		if err := rss.Scan(&e.Id, &e.IdPelicula); err != nil {
			return []interfacecine.EstrenoAndSlider{}, err
		}
		estrenos = append(estrenos, e)
	}
	return estrenos, nil
}

func GetEstrenosPagination(db *sql.DB, page int, limit int) ([]interfacecine.EstrenoAndSlider, error) {
	// Calcular el offset a partir de la página y el límite
	offset := (page - 1) * limit
	rows, err := db.Query("SELECT * FROM estrenos LIMIT ? OFFSET ?", limit, offset)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	var estrenos []interfacecine.EstrenoAndSlider
	for rows.Next() {
		var e interfacecine.EstrenoAndSlider
		if err := rows.Scan(&e.Id, &e.IdPelicula); err != nil {
			return nil, err
		}
		estrenos = append(estrenos, e)
	}
	return estrenos, nil
}

func GetSlider(db *sql.DB, idSlider int) (interfacecine.EstrenoAndSlider, error) {
	sql := "SELECT * FROM slider WHERE id = ?"
	rss, err := db.Query(sql, idSlider)
	if err != nil {
		return interfacecine.EstrenoAndSlider{}, err
	}
	defer rss.Close()
	var slider interfacecine.EstrenoAndSlider
	for rss.Next() {
		if err := rss.Scan(&slider.Id, &slider.IdPelicula); err != nil {
			return interfacecine.EstrenoAndSlider{}, err
		}
	}
	if slider.Id == 0 {
		return interfacecine.EstrenoAndSlider{}, nil
	}
	return slider, nil
}

func GetSliderAll(db *sql.DB) ([]interfacecine.EstrenoAndSlider, error) {
	sql := "SELECT * FROM slider"
	rss, err := db.Query(sql)
	if err != nil {
		return []interfacecine.EstrenoAndSlider{}, err
	}
	defer rss.Close()
	var slider []interfacecine.EstrenoAndSlider
	for rss.Next() {
		var s interfacecine.EstrenoAndSlider
		if err := rss.Scan(&s.Id, &s.IdPelicula); err != nil {
			return []interfacecine.EstrenoAndSlider{}, err
		}
		slider = append(slider, s)
	}
	return slider, nil
}
