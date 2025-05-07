import pandas as pd
productos = pd.read_excel("productos.xlsx")
productos["precio_descuento"] = productos.apply(
    lambda row: row["precio"] * 0.9 if row["stock"] < 50 else row["precio"],
    axis=1
)
productos.to_excel("productos_actualizados.xlsx", index=False)
