package get

import (
	"database/sql"

	"Severl/interfacecine"

	_ "github.com/go-sql-driver/mysql"
)

func GetSala(db *sql.DB, id int) (interfacecine.Salas, error) {
	var sala interfacecine.Salas
	sql := "SELECT * FROM salas WHERE id=?"
	err := db.QueryRow(sql, id).Scan(&sala.Id, &sala.Nombre, &sala.Fillas, &sala.Columnas)
	if err != nil {
		return sala, err
	}
	return sala, nil
}

func GetSalasAll(db *sql.DB) ([]interfacecine.Salas, error) {
	sql := "SELECT * FROM salas"
	rows, err := db.Query(sql)
	if err != nil {
		return []interfacecine.Salas{}, err
	}
	var salas []interfacecine.Salas
	for rows.Next() {
		var sala interfacecine.Salas
		if err := rows.Scan(&sala.Id, &sala.Nombre, &sala.Fillas, &sala.Columnas); err != nil {
			return []interfacecine.Salas{}, err
		}
		salas = append(salas, sala)
	}
	return salas, nil
}
