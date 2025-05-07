import os
carpeta = "."  # Puedes cambiar a tu ruta específica si deseas
archivo_origen = os.path.join(carpeta, "productos.xlsx")
archivo_destino = os.path.join(carpeta, "productorenombrado.xlsx")

if os.path.exists(archivo_origen):
    os.rename(archivo_origen, archivo_destino)
    print("✅ Archivo renombrado correctamente.")
else:
    print("⚠️ El archivo 'productos.xlsx' no se encontró.")