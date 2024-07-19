package get

import (
	"Severl/interfacecine"
	"database/sql"
)

func GetAllGenero(db *sql.DB) ([]interfacecine.Genero, error) {
	sql := "SELECT * FROM genero"
	rows, err := db.Query(sql)
	if err != nil {
		return nil, err
	}
	var datos []interfacecine.Genero
	for rows.Next() {
		var infoGenero interfacecine.Genero
		err := rows.Scan(&infoGenero.Id, &infoGenero.Nombre)
		if err != nil {
			return nil, err
		}
		datos = append(datos, infoGenero)
	}
	return datos, nil
}
