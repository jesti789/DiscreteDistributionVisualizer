import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

#st.title("Binomial Distribution Visualizer")
#n = st.slider("Number of trials (n)", 1, 50, 10, 1)
#p = st.slider("Probability of success (p)", 0.01, 1.0, 0.5, 0.01)

def plot_binomial(n, p):
    x_values = np.arange(0, n + 1)
    y_values = binom.pmf(x_values, n, p)
    fig, (ax, ax_table) = plt.subplots(ncols=2, figsize=(10, 5), gridspec_kw={'width_ratios': [2, 1]})

    ax.bar(x_values, y_values, alpha=0.75, color='blue', edgecolor='black')
    ax.set_xlabel('X values')
    ax.set_ylabel('Probability')
    ax.set_title(f'Binomial Distribution (n={n}, p={p:.2f})')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    table_data = [[f"{int(x)}", f"{y:.8f}"] for x, y in zip(x_values, y_values)]
    ax_table.axis("off")
    table = ax_table.table(cellText=table_data, colLabels=["X", "P(X)"], loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)

    return fig

#fig = plot_binomial(n, p)
#st.pyplot(fig)
