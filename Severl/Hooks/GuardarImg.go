package hooks

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"strings"
	"time"
)

// DownloadFile descarga un archivo desde una URL o una ruta local y lo guarda en una carpeta específica del proyecto.
// Retorna la URL completa donde se guardó el archivo.
func DownloadFile(source string) (string, error) {
	var url string
	var fileName string

	// Determinar si la fuente es una URL o una ruta local
	if strings.HasPrefix(source, "http://") || strings.HasPrefix(source, "https://") {
		url = source
		fileName = generateUniqueFileName(url)
	} else {
		// Es una ruta local
		localFilePath := source
		fileName = filepath.Base(localFilePath)
		if _, err := os.Stat(localFilePath); os.IsNotExist(err) {
			return "", fmt.Errorf("local file does not exist: %v", err)
		}
	}

	destFolder := "./assets" // Carpeta de destino dentro del proyecto

	// Crear la carpeta de destino si no existe
	if _, err := os.Stat(destFolder); os.IsNotExist(err) {
		err := os.Mkdir(destFolder, os.ModePerm)
		if err != nil {
			return "", fmt.Errorf("failed to create directory: %v", err)
		}
	}

	// Crear el archivo en la carpeta de destino
	destPath := filepath.Join(destFolder, fileName)
	out, err := os.Create(destPath)
	if err != nil {
		return "", fmt.Errorf("failed to create file: %v", err)
	}
	defer out.Close()

	// Si la fuente es una URL, descargar el archivo
	if url != "" {
		// Descargar el archivo desde la URL
		resp, err := http.Get(url)
		if err != nil {
			return "", fmt.Errorf("failed to fetch URL: %v", err)
		}
		defer resp.Body.Close()

		if resp.StatusCode != http.StatusOK {
			return "", fmt.Errorf("unexpected status code: %d", resp.StatusCode)
		}

		// Copiar el cuerpo de la respuesta HTTP al archivo de salida
		_, err = io.Copy(out, resp.Body)
		if err != nil {
			return "", fmt.Errorf("failed to copy body: %v", err)
		}
	} else {
		// Si la fuente es una ruta local, copiar el archivo local al destino
		in, err := os.Open(source)
		if err != nil {
			return "", fmt.Errorf("failed to open local file: %v", err)
		}
		defer in.Close()

		// Copiar el contenido del archivo local al archivo de salida
		_, err = io.Copy(out, in)
		if err != nil {
			return "", fmt.Errorf("failed to copy local file content: %v", err)
		}
	}

	// Construir y retornar la URL completa donde se guardó el archivo
	fullURL := fmt.Sprintf("http://localhost:8080/assets/%s", fileName)
	return fullURL, nil
}

// generateUniqueFileName genera un nombre de archivo único basado en la URL y la fecha actual.
func generateUniqueFileName(source string) string {
	var fileName string
	if strings.HasPrefix(source, "http://") || strings.HasPrefix(source, "https://") {
		// Si la fuente es una URL, obtener el nombre de archivo de la URL
		fileName = filepath.Base(source)
	} else {
		// Si la fuente es una ruta local, usar el nombre base del archivo
		fileName = filepath.Base(source)
	}

	// Generar un nombre único basado en la fecha y hora actual
	now := time.Now().Format("20060102150405") // Formato: yyyymmddhhmmss
	uniqueFileName := fmt.Sprintf("%s_%s", now, fileName)

	return uniqueFileName
}
