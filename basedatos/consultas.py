import mysql.connector

# Establecer conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="alvaro321",
    database="escuela"
)
cursor = conexion.cursor()

# Ejecutar consulta
cursor.execute("SELECT * FROM curso")

# Obtener resultados
resultados = cursor.fetchall()

# Mostrar resultados
for fila in resultados:
    print(fila)

# Cerrar conexión
cursor.close()

conexion.close()