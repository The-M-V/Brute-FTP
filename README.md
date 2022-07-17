# FTP BRUTE

> ***FTP BRUTE*** es una herramienta creada en Python3 para hacer ataques de fuerza bruta hacia el servicio FTP.

## Instalación
```bash
# Clonar el repositorio
git clone https://github.com/The-M-V/Brute-FTP

# Movernos al directorio
cd Brute-FTP/
```
## Uso
- **-i**
	- Especifica una IP.
		- `python3 ftp-brute.py -i 127.0.0.1`
	
- **-u**
	- Usuario a hacer fuerza bruta.
		- `python3 ftp-brute.py -i 127.0.0.1 -u prueba`
	
- **-v**
	- Activar o desactivar la verbosidad.
		- `python3 ftp-brute.py -i 127.0.0.1 -u prueba -v yes`
        
- **-w**
	- Diccionario de contraseñas.
		- `python3 ftp-brute.py -i 127.0.0.1 -u prueba -v yes`

- **-U**
	- Diccionario de usuarios.
		- `python3 ftp-brute.py -i 127.0.0.1 -U users.txt`
    
## ¿Dónde funciona?
|    OS   |   Tested   |
|:-------:|:----------:|
| Linux   |      ✔️     |
| Windows | Not Tested     |
| Mac     | Not Tested |

