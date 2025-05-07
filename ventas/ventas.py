import pandas as pd

data_ventas = {
    "cliente": ["Juan", "María", "Pedro", "Rosa"],
    "monto": [950, 1200, 1800, 750]
}
df_ventas = pd.DataFrame(data_ventas)
df_ventas.to_excel("venta.xlsx", index=False)