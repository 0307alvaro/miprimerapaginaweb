import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",        # Servidor MySQL
    user="root",             # Usuario de MySQL
    password="alvaro321",# Contraseña de MySQL
    database="escuela"       # Nombre de la base de datos
)

if conexion.is_connected():
    print("Conexión exitosa a la base de datos")

# Cerrar la conexión
conexion.close()


