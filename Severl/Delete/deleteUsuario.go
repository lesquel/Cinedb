package delete

import "database/sql"

func DeleteUsuario(db *sql.DB, id int) error {
	sql := "DELETE FROM usuario WHERE id = ?"
	_, err := db.Exec(sql, id)
	if err != nil {
		return err
	}
	return nil
}
