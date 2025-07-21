# ops/compra_call.py
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Evita problemas con el backend de matplotlib en algunos entornos
import matplotlib.pyplot as plt

def calcular_compra_call(precio_strike, prima, cant_contratos=1, rango=40):

    punto_equilibrio = precio_strike + prima
    precios = np.arange(punto_equilibrio - rango*10, punto_equilibrio + rango*8, rango)
    
    if punto_equilibrio not in precios:
        precios = np.append(precios, punto_equilibrio)
        precios = np.sort(precios)
    
    datos = []
    for precio_sub in precios:
        resultado = (max(0, precio_sub - precio_strike) - prima) * cant_contratos
        datos.append([precio_sub, resultado])
    
    df = pd.DataFrame(datos, columns=['Precio Sub', 'Resultado'])
    
    # Gráfico
    fig, ax = plt.subplots(figsize=(10, 6))

    # Línea horizontal para el punto de equilibrio
    ax.axhline(y=0, color='blue', linestyle='--')  
    ax.axhline(y=-(prima), color='r', linestyle='--', label='Pérdida máxima')  # Línea horizontal para la pérdida máxima
    
    # Texto de perdida máxima en el gráfico

    perdida_max = -prima * cant_contratos
    ax.text(
        (df['Precio Sub'].min() + df['Precio Sub'].max()) / 2,
        perdida_max - 1,
        f'Pérdida máxima: {perdida_max:.2f}',
        color='red',
        fontsize=12,
        ha='center',
        verticalalignment='top'
    )
    
    # Línea vertical para el punto de equilibrio  
    ax.axvline(x=punto_equilibrio, color='blue', linestyle='--', label='Punto de equilibrio')  
    
    # Texto del punto de equilibrio
    ax.text(
        punto_equilibrio,
        df['Resultado'].min() + 5,
        f'PE: {punto_equilibrio:.2f}',
        rotation=90,
        color='blue',
        fontsize=12,
        verticalalignment='bottom',
        ha='center'
    )

    # Línea principal del gráfico
    ax.plot(df['Precio Sub'], df['Resultado'], marker='o', color='black', label='Payoff Opción')  # Plotea el payoff de la opción

    # Personalización del gráfico
    ax.set_xticklabels (df['Precio Sub'], rotation=60, fontsize=12)  # Rotación de las etiquetas del eje X para mejor visualización
    
    # Eje Y: Utilizamos los resultados calculados en la tabla como ticks en el eje Y
    yticks = np.unique(df['Resultado'])  # Obtiene los valores únicos de los resultados para los ticks del eje Y
    ax.set_yticklabels(yticks, fontsize=12)  # Establece los valores del eje Y según los resultados

    ax.set_ylim(min(yticks) - 10, max(yticks) + 10)  # Establece los límites del eje Y con un pequeño margen

    # Etiquetas y leyenda
    ax.set_xlabel('Precio Subyacente', fontsize=14)  # Etiqueta para el eje X
    ax.set_ylabel('Ganancia / Pérdida', fontsize=14)  # Etiqueta para el eje Y
    ax.set_title('Resultado de una Compra de CALL', fontsize=16)  # Título del gráfico
    ax.grid(color='gray', linestyle='--', linewidth=0.5)  # Añade una cuadrícula ligera en el gráfico
    ax.legend(fontsize=12)  # Muestra la leyenda con una fuente de tamaño 12
    #ax.tight_layout(pad=2)  # Ajusta el espacio en el gráfico para evitar que las etiquetas se corten  
    ax.set_in_layout(True)  # Asegura que el gráfico se ajuste al layout de Streamlit

    
    return df, fig  # Devuelve DataFrame y gráfico