import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Datos simulados
df = pd.DataFrame({
    'mes': ['Enero', 'Enero', 'Febrero', 'Febrero'],
    'producto': ['A', 'B', 'A', 'B'],
    'monto': [100, 150, 200, 250]
})

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Dashboard de Ventas"),
    dcc.Dropdown(df['mes'].unique(), id='mes', value='Enero'),
    dcc.Graph(id='grafico')
])

@app.callback(
    Output('grafico', 'figure'),
    Input('mes', 'value')
)
def update(mes):
    filtro = df[df['mes'] == mes]
    return px.bar(filtro, x='producto', y='monto', title=f'Ventas en {mes}')

if __name__ == "__main__":
    app.run(debug=True)  

#jecutar con: python reporte3.py

