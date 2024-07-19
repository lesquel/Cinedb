package update

import (
	"database/sql"

	_ "github.com/go-sql-driver/mysql"
)

func UpdateSillas(db *sql.DB, id int, sillas string) error {
	stmt, err := db.Prepare("UPDATE funciones SET sillas = ? WHERE id = ?")
	if err != nil {
		return err
	}
	defer stmt.Close()
	_, err = stmt.Exec(sillas, id)
	return err
}
