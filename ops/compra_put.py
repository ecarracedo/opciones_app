# ops/compra_put.py
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Evita problemas con el backend de matplotlib en algunos entornos
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

    # Línea de pérdida máxima
    perdida_max = -prima * cant_contratos
    ax.axhline(y=perdida_max, color='r', linestyle='--', label='Pérdida máxima')
    
    # Texto de pérdida máxima
    ax.text(
        (df['Precio Subyacente'].min() + df['Precio Subyacente'].max()) / 2,
        perdida_max - 1,
        f'Pérdida máxima: {perdida_max:.2f}',
        color='red',
        fontsize=12,
        ha='center',
        verticalalignment='top'
    )

    # Línea del punto de equilibrio
    ax.axvline(x=punto_equilibrio, color='blue', linestyle='--', label='Punto de equilibrio')

    # Texto del punto de equilibrio
    ax.text(
        punto_equilibrio,
        (df['Resultado'].min() + df['Resultado'].max()) / 2,
        f'PE: {punto_equilibrio:.2f}',
        rotation=90,
        color='blue',
        fontsize=12,
        ha='center',
        va='center',
        bbox=dict(facecolor='white', alpha=0.6, edgecolor='none')
    )
    # Payoff
    ax.plot(df['Precio Subyacente'], df['Resultado'], marker='o', color='black', label='Payoff Opción')

    # Ejes y estilo
    ax.set_title('Resultado de una Compra de PUT', fontsize=16)
    ax.set_xlabel('Precio Subyacente', fontsize=14)
    ax.set_ylabel('Ganancia / Pérdida', fontsize=14)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    ax.legend(fontsize=12)
    ax.set_in_layout(True)

    return df, fig
