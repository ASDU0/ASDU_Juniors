import mysql.connector
from mysql.connector import Error

def conectar_mysql():
    try:
        conexion = mysql.connector.connect(
            host='localhost',       # o 127.0.0.1
            port=3307,              # cambia si usas otro puerto, ej. 3307
            user='root',
            password='',            # vacío si no tienes contraseña
            database='test'         # crea una base llamada "test" en phpMyAdmin
        )

        if conexion.is_connected():
            print("✅ Conectado a MySQL correctamente.")
            info = conexion.get_server_info()
            print("Versión del servidor:", info)

    except Error as e:
        print("❌ Error al conectar:", e)

    finally:
        if 'conexion' in locals() and conexion.is_connected():
            conexion.close()
            print("🔒 Conexión cerrada.")

if __name__ == "__main__":
    conectar_mysql()
