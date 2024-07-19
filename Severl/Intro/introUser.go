package intro

import (
	interfacecine "Severl/interfacecine"
	"database/sql"
)

func IntroUser(db *sql.DB, infoUser interfacecine.Usuario) error {
	infoUser.Admin = false
	sql := `INSERT INTO user (nombre, contra, img, edad, name, correo, admin) VALUES (?, ?, ?, ?, ?, ?, ?)`
	stmt, err := db.Prepare(sql)
	if err != nil {
		return err
	}
	_, err = stmt.Exec(infoUser.Nombre, infoUser.Contra, infoUser.Img, infoUser.Edad, infoUser.Name, infoUser.Correo, infoUser.Admin)
	if err != nil {
		return err
	}
	return nil
}
