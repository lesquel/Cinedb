package conex

import (
	"database/sql"
	"log"
	"os"
)

// Database Connection
var db *sql.DB

func GetConexion() *sql.DB {
	if db != nil {
		return db
	}
	var err error
	dsn := os.Getenv("DB_DSN")
	if dsn == "" {
		dsn = "root:@tcp(localhost)/cine" // Default DSN
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
