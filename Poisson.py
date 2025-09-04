import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

#st.title("Poisson Distribution Visualizer")
#lmbda = st.slider("Lambda (λ)", 0.1, 10.0, 5.0, 0.1)

def plot_poisson(lmbda):
    max_x = int(poisson.ppf(0.999, lmbda))
    x_values = np.arange(0, max_x + 1)
    y_values = np.array(poisson.pmf(x_values, lmbda), dtype=np.float64)

    fig, (ax, ax_table) = plt.subplots(ncols=2, figsize=(10, 5), gridspec_kw={'width_ratios': [2, 1]})
    
    ax.bar(x_values, y_values, alpha=0.75, color='blue', edgecolor='black')
    ax.set_xlabel('X values')
    ax.set_ylabel('Probability')
    ax.set_title(f'Poisson Distribution (λ = {lmbda:.2f})')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    table_data = [[f"{int(x)}", f"{p:.4f}"] for x, p in zip(x_values, y_values)]
    ax_table.axis("off")
    table = ax_table.table(cellText=table_data, colLabels=["X", "P(X)"], loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)

    return fig

#fig = plot_poisson(lmbda)
#st.pyplot(fig)
