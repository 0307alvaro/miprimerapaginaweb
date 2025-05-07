import mysql.connector


conexion = mysql.connector.connect(
    host="localhost",  
    user="root", 
    password="alvaro321", 
    database="tienda"  
)


cursor = conexion.cursor()


consulta = """
SELECT v.id_venta, v.id_cliente 
FROM venta v 
LEFT JOIN clientes c ON v.id_cliente = c.id_cliente
WHERE c.id_cliente IS NULL;
"""

cursor.execute(consulta)


resultados = cursor.fetchall()


if not resultados:
    print("No se encontraron ventas sin cliente asociado.")
else:

    for fila in resultados:
        print(f"id_venta: {fila[0]}, id_cliente: {fila[1]}")


cursor.close()
conexion.close()
