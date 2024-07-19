package delete

import "database/sql"

func DeletePelicula(db *sql.DB, id int) error {
	sql := "DELETE FROM pelicula WHERE id = ?"
	_, err := db.Exec(sql, id)
	if err != nil {
		return err
	}
	return nil
}

func DeleteEstrenos(db *sql.DB, idEstereno int) error {
	sql := "DELETE FROM estrenos WHERE id = ?"
	_, err := db.Exec(sql, idEstereno)
	if err != nil {
		return err
	}
	return nil
}

func DeleteSlider(db *sql.DB, idSlider int) error {
	sql := "DELETE FROM slider WHERE id = ?"
	_, err := db.Exec(sql, idSlider)
	if err != nil {
		return err
	}
	return nil
}
