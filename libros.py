import sqlite3

def iniciar_conexion():
    con = sqlite3.connect('biblioteca.db')
    return con

def crear_tabla_biblioteca(con):
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS coleccion (
            identificador INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            escritor TEXT NOT NULL,
            publicacion INTEGER NOT NULL
        )
    ''')
    con.commit()

con = iniciar_conexion()
crear_tabla_biblioteca(con)

def insertar_libro(con, nombre, escritor, publicacion):
    cur = con.cursor()
    cur.execute('INSERT INTO coleccion (nombre, escritor, publicacion) VALUES (?, ?, ?)', (nombre, escritor, publicacion))
    con.commit()

def encontrar_libro(con, nombre):
    cur = con.cursor()
    cur.execute('SELECT * FROM coleccion WHERE nombre LIKE ?', ('%' + nombre + '%',))
    libros = cur.fetchall()
    for libro in libros:
        print(f'ID: {libro[0]}, Nombre: {libro[1]}, Escritor: {libro[2]}, Publicación: {libro[3]}')

def borrar_libro(con, id_libro):
    cur = con.cursor()
    cur.execute('DELETE FROM coleccion WHERE identificador = ?', (id_libro,))
    con.commit()

def menu_principal():
    con = iniciar_conexion()
    crear_tabla_biblioteca(con)
    
    while True:
        print("\nGestor de Biblioteca")
        print("1. Añadir libro")
        print("2. Buscar libro")
        print("3. Eliminar libro")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre del libro: ")
            escritor = input("Escritor del libro: ")
            publicacion = int(input("Año de publicación: "))
            insertar_libro(con, nombre, escritor, publicacion)
        elif opcion == '2':
            nombre = input("Nombre del libro a buscar: ")
            encontrar_libro(con, nombre)
        elif opcion == '3':
            id_libro = int(input("ID del libro a eliminar: "))
            borrar_libro(con, id_libro)
        elif opcion == '4':
            con.close()
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == '__main__':
    menu_principal()
