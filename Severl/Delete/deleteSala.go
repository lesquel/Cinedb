package delete

import "database/sql"

func DeleteSala(db *sql.DB, id int) error {
	stmt, err := db.Prepare("DELETE FROM salas WHERE id=?")
	if err != nil {
		return err
	}
	defer stmt.Close()
	_, err = stmt.Exec(id)
	if err != nil {
		return err
	}

	return nil
}
