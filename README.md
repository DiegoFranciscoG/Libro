# Gestor de Biblioteca

Este proyecto es una aplicación sencilla para gestionar una colección de libros utilizando SQLite como base de datos. Permite añadir, buscar y eliminar libros de la base de datos a través de una interfaz de línea de comandos.

## Características

- **Añadir libro:** Permite añadir un nuevo libro a la base de datos con los datos del nombre, escritor y año de publicación.
- **Buscar libro:** Permite buscar libros en la base de datos por su nombre, mostrando los resultados coincidentes.
- **Eliminar libro:** Permite eliminar un libro de la base de datos por su identificador único.
- **Interfaz de usuario sencilla:** Una interfaz de línea de comandos fácil de usar para interactuar con la base de datos.

## Requisitos

- Python 3.x
- SQLite3 (incluido en Python estándar)

## Instrucciones de Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tuusuario/gestor-de-biblioteca.git
   ```
2. **Navegar al directorio del proyecto:**
   ```bash
   cd gestor-de-biblioteca
   ```

## Uso

1. Ejecuta el script principal:
   ```bash
   python biblioteca.py
   ```
2. Sigue las instrucciones en pantalla para añadir, buscar o eliminar libros de la base de datos.

## Estructura del Proyecto

- **biblioteca.py:** El archivo principal que contiene toda la lógica del programa.
- **README.md:** Este archivo, con las instrucciones y detalles del proyecto.

## Ejemplo de Uso

Al ejecutar el programa, verás el siguiente menú:

```
Gestor de Biblioteca
1. Añadir libro
2. Buscar libro
3. Eliminar libro
4. Salir
```

### Añadir un Libro

Selecciona la opción `1` y sigue las indicaciones para añadir un nuevo libro:

```
Nombre del libro: Cien Años de Soledad
Escritor del libro: Gabriel García Márquez
Año de publicación: 1967
```

### Buscar un Libro

Selecciona la opción `2` y proporciona el nombre (o parte del nombre) del libro que deseas buscar:

```
Nombre del libro a buscar: Soledad
```

El programa mostrará los libros que coinciden con la búsqueda.

### Eliminar un Libro

Selecciona la opción `3` y proporciona el ID del libro que deseas eliminar:

```
ID del libro a eliminar: 1
```

### Salir

Selecciona la opción `4` para cerrar el programa.
