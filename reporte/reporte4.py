#Ejemplo 3: Gráfico Interactivo con Plotly (Jupyter Notebook o script)

import pandas as pd
import plotly.express as px

# Datos simulados
df = pd.DataFrame({
    'producto': ['A', 'B', 'C'],
    'ventas': [100, 200, 150]
})

# Gráfico de pastel
fig = px.pie(df, names='producto', values='ventas', title='<b>Ventas por Producto</b>')
fig.update_layout(title={'x': 0.5})
fig.show()

            
#jecutar con: python reporte4.py


