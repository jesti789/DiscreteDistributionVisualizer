import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom

#st.title("Hypergeometric Distribution Visualizer")
#N = st.slider("Population size (N)", 5, 100, 20, 1)
#K = st.slider("Number of successes in population (K)", 1, N, 10, 1)
#n = st.slider("Sample size (n)", 1, N, 5, 1)

def plot_hypergeometric(N, K, n):
    x_values = np.arange(max(0, n - (N - K)), min(n, K) + 1)
    y_values = hypergeom.pmf(x_values, N, K, n)

    fig, (ax, ax_table) = plt.subplots(ncols=2, figsize=(10, 5), gridspec_kw={'width_ratios': [2, 1]})

    ax.bar(x_values, y_values, alpha=0.75, color='blue', edgecolor='black')
    ax.set_xlabel('X values')
    ax.set_ylabel('Probability')
    ax.set_title(f'Hypergeometric Distribution (N={N}, K={K}, n={n})')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    table_data = [[f"{int(x)}", f"{y:.8f}"] for x, y in zip(x_values, y_values)]
    ax_table.axis("off")
    table = ax_table.table(cellText=table_data, colLabels=["X", "P(X)"], loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)

    return fig

#fig = plot_hypergeometric(N, K, n)
#st.pyplot(fig)
