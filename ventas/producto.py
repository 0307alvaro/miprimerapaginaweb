import pandas as pd
data_productos = {
    "producto": ["Laptop", "Mouse", "Teclado", "Monitor", "USB", "Webcam"],
    "precio": [3000, 50, 100, 800, 20, 150],
    "stock": [30, 100, 45, 25, 70, 40]
}
df_productos = pd.DataFrame(data_productos)
df_productos.to_excel("productos.xlsx", index=False)
print("✅ Archivo productos.xlsx creado con éxito.")