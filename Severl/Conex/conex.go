package conex

import (
	"database/sql"
	"log"
	"os"
)

// Database Connection
var db *sql.DB

const IpDeLaBaseDeDatos = "localhost"
const NombreDeLaBaseDeDatos = "cine"
const UsuarioDeLaBaseDeDatos = "root"
const ContraseñaDeLaBaseDeDatos = ""

func GetConexion() *sql.DB {
	if db != nil {
		return db
	}
	var err error
	dsn := os.Getenv("DB_DSN")
	if dsn == "" {
		dsn = UsuarioDeLaBaseDeDatos + ":" + ContraseñaDeLaBaseDeDatos + "@tcp(" + IpDeLaBaseDeDatos + ")/" + NombreDeLaBaseDeDatos // Default DSN
	}
	db, err = sql.Open("mysql", dsn)
	if err != nil {
		log.Fatalf("Failed to open database connection: %v", err)
	}
	if err = db.Ping(); err != nil {
		log.Fatalf("Failed to ping database: %v", err)
	}
	return db
}
