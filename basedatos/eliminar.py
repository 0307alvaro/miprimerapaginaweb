import mysql.connector

# Establecer conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="alvaro321",
    database="escuela"
)
cursor = conexion.cursor()

sql = "DELETE FROM estudiante WHERE nombre = %s"
valores = ("Maria",)
cursor.execute(sql, valores)
conexion.commit()  # Guardar cambios

print(cursor.rowcount, "registros eliminado.")

cursor.close()
conexion.close()