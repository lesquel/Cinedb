package delete

import "database/sql"

func DeleteGenero(db *sql.DB, idGenero int) error {
	stmt, err := db.Prepare("DELETE FROM genero WHERE id = ?")
	if err != nil {
		return err
	}
	_, err = stmt.Exec(idGenero)
	if err != nil {
		return err
	}
	return nil
}
