# ops/compra_call.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calcular_compra_call(precio_strike, prima, cant_contratos=1, rango=40):
    # --- (Mantén tu lógica actual aquí) --- #
    punto_equilibrio = precio_strike + prima
    precios = np.arange(punto_equilibrio - rango*10, punto_equilibrio + rango*8, rango)
    
    if punto_equilibrio not in precios:
        precios = np.append(precios, punto_equilibrio)
        precios = np.sort(precios)
    
    datos = []
    for precio_sub in precios:
        resultado = (max(0, precio_sub - precio_strike) - prima) * cant_contratos
        datos.append([precio_sub, resultado])
    
    df = pd.DataFrame(datos, columns=['Precio Subyacente', 'Resultado'])
    
    # Gráfico (opcional: devuelve el fig de matplotlib)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Precio Subyacente'], df['Resultado'], marker='o', color='black')
    # ... (personaliza el gráfico como en tu código)
    
    return df, fig  # Devuelve DataFrame y gráfico