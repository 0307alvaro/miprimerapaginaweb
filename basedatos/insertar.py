import mysql.connector

# Establecer conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="alvaro321",
    database="escuela"
)
cursor = conexion.cursor()

sql = "INSERT INTO estudiante (nombre, edad, correo, direccion, telefono) VALUES (%s, %s, %s, %s, %s)"
valores = [
    ("Juanito", 21, "juanitof@gmail.com", "asoc 1234", "921536987"),
    ("Juanes", 21, "juanes@gmail.com", "asoc 12345", "921536987"),
    ("pedrito", 21, "pedrito@gmail.com", "asoc 12346", "921536987"),
    ("perezozo", 21, "perezozo@gmail.com", "asoc 12347", "921536987"),
    ("paul", 21, "paul@gmail.com", "asoc 12348", "921536987"),
    ("pol", 21, "pol@gmail.com", "asoc 12349", "921536987"),
    ("gavi", 21, "gavi@gmail.com", "asoc 123410", "921536987"),
    ("morales", 21, "morales@gmail.com", "asoc 123411", "921536987")
]
cursor.executemany(sql, valores)
conexion.commit()  # Guardar cambios
sql = "INSERT INTO estudiante (nombre, edad, correo, direccion, telefono) VALUES (%s, %s, %s, %s, %s)"
valores = [
    ("Maria", 23, "maria@gmail.com", "asoc 12dsa34", "921536987"),
    ("Mariana", 21, "mariana@gmail.com", "asoc 12dasd345", "921536987"),
    ("Mario", 21, "mario@gmail.com", "asoc 1234fedf6", "921536987"),
]
cursor.executemany(sql, valores)
conexion.commit()

print(cursor.rowcount, "registros insertados.")

cursor.close()
conexion.close()
