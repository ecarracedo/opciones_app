# ops/venta_put.py
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def calcular_venta_put(precio_strike, prima, cant_contratos=1, rango=40):
    punto_equilibrio = precio_strike - prima
    precios = np.arange(punto_equilibrio - rango*8, punto_equilibrio + rango*10, rango)

    if punto_equilibrio not in precios:
        precios = np.append(precios, punto_equilibrio)
        precios = np.sort(precios)

    datos = []
    for precio_sub in precios:
        resultado = (prima - max(0, precio_strike - precio_sub)) * cant_contratos
        datos.append([precio_sub, resultado])

    df = pd.DataFrame(datos, columns=['Precio Subyacente', 'Resultado'])

    fig, ax = plt.subplots(figsize=(10, 6))

    # Línea de ganancia máxima
    ganancia_max = prima * cant_contratos
    ax.axhline(y=ganancia_max, color='g', linestyle='--', label='Ganancia máxima')

    # Texto de ganancia máxima
    ax.text(
        (df['Precio Subyacente'].min() + df['Precio Subyacente'].max()) / 2,
        ganancia_max + 1,
        f'Ganancia máxima: {ganancia_max:.2f}',
        color='green',
        fontsize=12,
        ha='center',
        va='bottom'
    )

    # Línea del punto de equilibrio
    ax.axvline(x=punto_equilibrio, color='blue', linestyle='--', label='Punto de equilibrio')

    # Texto rotado del punto de equilibrio (alineado sin desplazar gráfico)
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

    # Línea de payoff
    ax.plot(df['Precio Subyacente'], df['Resultado'], marker='o', color='black', label='Payoff Opción')

    # Estética general
    ax.set_title('Resultado de una Venta de PUT', fontsize=16)
    ax.set_xlabel('Precio Subyacente', fontsize=14)
    ax.set_ylabel('Ganancia / Pérdida', fontsize=14)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    ax.legend(fontsize=12)
    ax.set_in_layout(True)

    return df, fig
