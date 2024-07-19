package update

import (
	interfacecine "Severl/interfacecine"
	"database/sql"
)

func UpdateUser(db *sql.DB, infoUser interfacecine.Usuario) error {
	sql := "UPDATE user SET nombre = ?, contra = ?, edad = ?, img = ?, name = ?, correo = ? WHERE id = ?"
	_, err := db.Exec(sql, infoUser.Nombre, infoUser.Contra, infoUser.Edad, infoUser.Img, infoUser.Name, infoUser.Correo, infoUser.Id)
	if err != nil {
		return err
	}
	return nil
}
