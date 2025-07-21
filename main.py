import streamlit as st
import sys
from pathlib import Path

# Añade la carpeta principal al path temporalmente
sys.path.append(str(Path(__file__).parent))

from ops.compra_call import calcular_compra_call
from ops.compra_put import calcular_compra_put
from ops.venta_call import calcular_venta_call
from ops.venta_put import calcular_venta_put



# Configuración de la página
st.set_page_config(page_title="Calculadora de Opciones", layout="centered")
st.title("📊 Calculadora de Opciones Financieras")

# Sidebar para selección de operación
with st.sidebar:
    st.header("Tipo de Operación")
    tipo_operacion = st.selectbox(
        "Selecciona",
        ["Compra CALL", "Venta CALL", "Compra PUT", "Venta PUT"]
    )
    
    # Inputs comunes (reutilizados para todas las operaciones)
    precio_strike = st.number_input("Precio de Strike ($)", min_value=0.01, value=100.0)
    prima = st.number_input("Prima ($)", min_value=0.01, value=5.0)
    cant_contratos = st.number_input("Cantidad de Contratos", min_value=1, value=1)
    rango = st.number_input("Rango de Análisis (puntos)", min_value=1, value=20)

# Lógica para llamar al script correcto
if st.button("Calcular"):
    if tipo_operacion == "Compra CALL":
        df, fig = calcular_compra_call(precio_strike, prima, cant_contratos, rango)
    elif tipo_operacion == "Venta CALL":
        df, fig = calcular_venta_call(precio_strike, prima, cant_contratos, rango)
    elif tipo_operacion == "Compra PUT":
        df, fig = calcular_compra_put(precio_strike, prima, cant_contratos, rango)
    elif tipo_operacion == "Venta PUT":
        df, fig = calcular_venta_put(precio_strike, prima, cant_contratos, rango)
    
    # Mostrar resultados
    st.subheader(f"🔹 Resultados: {tipo_operacion}")
    st.dataframe(df.style.format({"Precio Subyacente": "{:.2f}", "Resultado": "{:.2f}"}))
    
    # Mostrar gráfico
    st.pyplot(fig)