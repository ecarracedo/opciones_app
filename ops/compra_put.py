# ops/compra_put.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calcular_compra_put(precio_strike, prima, cant_contratos=1, rango=40):
    punto_equilibrio = precio_strike - prima
    precios = np.arange(punto_equilibrio - rango*8, punto_equilibrio + rango*10, rango)
    
    if punto_equilibrio not in precios:
        precios = np.append(precios, punto_equilibrio)
        precios = np.sort(precios)
    
    datos = []
    for precio_sub in precios:
        resultado = (max(0, precio_strike - precio_sub) - prima) * cant_contratos
        datos.append([precio_sub, resultado])
    
    df = pd.DataFrame(datos, columns=['Precio Subyacente', 'Resultado'])
    
    # Gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Precio Subyacente'], df['Resultado'], marker='o', color='black')
    ax.axhline(0, color='black', linestyle='--')
    ax.axvline(punto_equilibrio, color='red', linestyle='--', label=f'Punto de equilibrio: {punto_equilibrio}')
    ax.set_title('Estrategia Compra de Put')
    ax.set_xlabel('Precio Subyacente')
    ax.set_ylabel('Ganancia/Pérdida')
    ax.legend()
    ax.grid(True)
    
    return df, fig