import pandas as pd
from fpdf import FPDF

usuarios = [
    {"Nombre": "Ana", "Edad": 22, "Correo": "ana@gmail.com"},
    {"Nombre": "luis", "Edad": 30, "Correo": "luis@gmail.com"},
    {"Nombre": "Pedro", "Edad": 25, "Correo": "pedro@gmail.com"},
    {"Nombre": "Maria", "Edad": 28, "Correo": "mari@gmail.com"},
    {"Nombre": "Raul", "Edad": 26, "Correo": "raul@gmail.com"},
    {"Nombre": "Elena", "Edad": 32, "Correo": "elena@gmail.com"},
    {"Nombre": "Javier", "Edad": 27, "Correo": "javier@gmail.com"},
    {"Nombre": "Clara", "Edad": 34, "Correo": "clara@gmail.com"},
]

# Crear Excel
df = pd.DataFrame(usuarios)
df.to_excel("usuarios.xlsx", index=False)

# Crear PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Reporte de usuarios", ln=True, align='C')
pdf.ln(10)

# Encabezados
pdf.set_font("Arial", size=8)
pdf.cell(60, 10, "Nombre", 1)
pdf.cell(30, 10, "Edad", 1)
pdf.cell(100, 10, "Correo", 1)
pdf.ln()

# Filas
pdf.set_font("Arial", size=10)
for u in usuarios:
    pdf.cell(60, 10, u["Nombre"], 1)
    pdf.cell(30, 10, str(u["Edad"]), 1)
    pdf.cell(100, 10, u["Correo"], 1)
    pdf.ln()

# Guardar PDF
pdf.output("Usuarios.pdf")



















reporte.py