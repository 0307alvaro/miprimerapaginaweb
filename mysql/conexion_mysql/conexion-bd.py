import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",    # Solo usa 'localhost' (sin el puerto)
    user="root",         # Tu usuario de MySQL
    password="alvaro321",# Tu contraseña de MySQL
    database="escuela"   # Nombre de la base de datos
)


# Verificar si la conexión fue exitosa
if conexion.is_connected():
    print("Conexión exitosa a la base de datos")

# Crear un cursor para interactuar con la base de datos
cursor = conexion.cursor()

# Ejecutar una consulta de ejemplo (por ejemplo, seleccionar todos los registros de la tabla 'estudiantes')
cursor.execute("SELECT * FROM estudiantes")

# Obtener los resultados de la consulta
resultados = cursor.fetchall()

# Mostrar los resultados
for fila in resultados:
    print(fila)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
