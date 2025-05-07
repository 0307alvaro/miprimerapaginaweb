import streamlit as st
import pandas as pd

data={'mes':['Enero', 'Febrebro', 'Marzo', 'Eneero', 'Febrebro', 'Marzo'],
      'producto': ['A', 'A', 'A', 'B', 'B', 'B'],
      'monto': [200,340,500,180,320,460]
      }

df=pd.DataFrame(data)
st.title("Reporte de Ventas")
mes=st.selectbox("Selecciona un mes", df['mes'].unique())
filtro=df[df['mes']==mes]

st.write(filtro)
st.bar_chart(filtro[['producto', 'monto']].set_indesx('producto'))

