import streamlit as st
import pandas as pd

# Crear datos 
data = {
    'mes': ['Enero', 'Febrero', 'Marzo', 'Enero', 'Febrero', 'Marzo'],
    'producto': ['A', 'A', 'A', 'B', 'B', 'B'],
    'monto': [200, 340, 500, 180, 320, 460]
}
df = pd.DataFrame(data)

st.title("Reporte de Ventas")

# Selección de mes
mes = st.selectbox("Selecciona un mes", df['mes'].unique())

# Filtrado de datos
filtro = df[df['mes'] == mes]

# Mostrar datos y gráfico
st.write(filtro)
st.bar_chart(filtro[['producto', 'monto']].set_index('producto'))


