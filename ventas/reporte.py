import pandas as pd
df = pd.read_excel("venta.xlsx")
ventas_filtradas = df[df["monto"] > 1000]
ventas_filtradas.to_excel("ventas_filtradas.xlsx", index=False)
