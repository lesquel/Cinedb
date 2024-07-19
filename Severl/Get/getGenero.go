package get

import (
	"database/sql"
	"log"

	interfacecine "Severl/interfacecine"

	_ "github.com/go-sql-driver/mysql"
)

func GetGenero(db *sql.DB, id int) (interfacecine.Genero, error) {
	var datos interfacecine.Genero
	err := db.QueryRow("SELECT * FROM genero WHERE id=?", id).Scan(&datos.Id, &datos.Nombre)
	if err != nil {
		log.Println(err)
		return datos, err
	}
	return datos, nil
}
