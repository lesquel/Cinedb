package get

import (
	"Severl/interfacecine"
	"database/sql"

	_ "github.com/go-sql-driver/mysql"
)

func GetFunciones(db *sql.DB, idPeliculas int) ([]interfacecine.Funciones, error) {
	rows, err := db.Query("SELECT * FROM funciones WHERE id_peliculas = ?", idPeliculas)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var funciones []interfacecine.Funciones
	for rows.Next() {
		var f interfacecine.Funciones
		if err := rows.Scan(&f.Id, &f.Fecha, &f.IdSala, &f.IdPeliculas, &f.Sillas); err != nil {
			return nil, err
		}
		funciones = append(funciones, f)
	}
	return funciones, nil
}

func GetFuncionesAll(db *sql.DB) ([]interfacecine.Funciones, error) {
	rows, err := db.Query("SELECT * FROM funciones")
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var funciones []interfacecine.Funciones
	for rows.Next() {
		var f interfacecine.Funciones
		if err := rows.Scan(&f.Id, &f.Fecha, &f.IdSala, &f.IdPeliculas, &f.Sillas); err != nil {
			return nil, err
		}
		funciones = append(funciones, f)
	}
	return funciones, nil
}
