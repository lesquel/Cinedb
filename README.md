# Intercine

## Requisitos de Python

- Python 3.10
- Tkinter
- [Customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- Requests
- Jinja2
- urllib3
- ThreadPoolExecutor
- webbrowser
- json
- BytesIO
- PIL

## Requisitos de Go

- [Go](https://go.dev/doc/install)
- [Driver MySQL](https://github.com/go-sql-driver/mysql)
- database/sql
- net/http
- encoding/json

## Configuración de la base de datos

1. Crear una base de datos en MySQL
2. Exporta los datos y la estructura de la base de datos de la aplicación a la carpeta `Severl/assets/cine (1).sql`

## Configuración del servidor de Go (Conexión a la base de datos)

1. En el archivo `Severl/Conex/conex.go`, cambiar la constante `dsn` por la conexión a la base de datos
2. En el archivo `Severl/Conex/conex.go`, cambiar la constante `IpDeLaBaseDeDatos` por la IP de la base de datos
3. En el archivo `Severl/Conex/conex.go`, cambiar la constante `NombreDeLaBaseDeDatos` por el nombre de la base de datos
4. En el archivo `Severl/Conex/conex.go`, cambiar la constante `UsuarioDeLaBaseDeDatos` por el nombre de usuario de la base de datos
5. En el archivo `Severl/Conex/conex.go`, cambiar la constante `ContraseñaDeLaBaseDeDatos` por la contraseña de la base de datos

```
const IpDeLaBaseDeDatos = "localhost"
const NombreDeLaBaseDeDatos = "cine"
const UsuarioDeLaBaseDeDatos = "root"
const ContraseñaDeLaBaseDeDatos = ""
...
dsn = UsuarioDeLaBaseDeDatos + ":" + ContraseñaDeLaBaseDeDatos + "@tcp(" + IpDeLaBaseDeDatos + ")/" + NombreDeLaBaseDeDatos // Default DSN
```


## Instalación

1. Instalar las dependencias de Python
2. Instalar las dependencias de Go

## Ejecución

1. Ejecutar el servidor de Go en el puerto 8080 con el comando, en la carpeta Severl: `go run .`
2. Ejecutar la aplicación de Python con el comando `python view/main.py`