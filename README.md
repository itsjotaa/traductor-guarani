# Traductor Español-Guarani
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Un traductor de español a guarani desarrollado en Python, que incluye API web y funcionalidades de traduccion basicas.

## Caracteristicas

- Traduccion palabra por palabra
- API REST con Flask
- Diccionarios organizados por categorias
- Facil de extender y personalizar

## Instalación

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación desde código fuente
```bash

# Clonar el repositorio
git clone https://github.com/itsjotaa/traductor-guarani.git
cd traductor-guarani

# Instalar en modo desarrollo
pip install -e .
```
## Uso básico
### Como módulo python 
```python

 from translator.traductor import traducir

texto_espanol = "hola amigos"
texto_guarani = traducir(texto_espanol)
print(texto_guarani)  # "maitei angiru"
```
## API Web
```bash

# Iniciar el servidor
python examples/api_basica.py

# En otro terminal, probar la API
python examples/probar_api_interactivo.py
```
## En el navegador 
Visita: http://localhost:5000/translate?texto=hola amigos

## Estructura del proyecto 
```text

traductor-guarani/
├── translator/          # Paquete principal
│   ├── traductor.py    # Funcion principal de traduccion
│   ├── diccionario.py  # Vocabularios organizados
│   ├── reglas.py       # Reglas gramaticales (en desarrollo)
│   └── utils.py        # Utilidades
├── examples/           # Ejemplos de uso
│   ├── api_basica.py           # API web
│   ├── probar_traductor.py     # Prueba interactiva
│   └── probar_api_interactivo.py # Cliente API
├── tests/              # Tests unitarios
├── README.md           # Este archivo
├── LICENSE             # Licencia MIT
└── setup.py           # Configuracion de paquete
```

## Agregar nuevas palabras 
Edita translator/diccionario.py y anade entradas a los diccionarios:

```python

palabras = {
    'hola': 'maitei',
    'amigo': 'angiru',
    # ... anade mas palabras aqui
}
```

## Proximas caracteristicas 
- Reglas gramaticales avanzadas
- Conjugacion verbal automatica
- Soporte para dialectos regionales (Por verse)
- Interfaz web moderna (Por verse)
- App movil (Por verse)

## Contribuir
Las contribuciones son bienvenidas! Especialmente:

- Hablantes nativos de guarani para mejorar traducciones
- Desarrolladores para nuevas funcionalidades
- Documentacion y ejemplos

1. Haz fork del proyecto
2. Crea una rama para tu feature (git checkout -b feature/nueva-caracteristica)
3. Commit tus cambios (git commit -am 'Anadir nueva caracteristica')
4. Push a la rama (git push origin feature/nueva-caracteristica)
5. Abre un Pull Request

## Licencia
Este proyecto esta bajo la Licencia MIT - ver el archivo LICENSE para detalles.

## Autor 
itsjotaa @itsjotaa

# Si te gusta el proyecto dale una estrella en GitHub! ^^