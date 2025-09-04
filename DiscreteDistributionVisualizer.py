import streamlit as st

from Poisson_func import plot_poisson
from Binomial_func import plot_binomial
from Hypergeometric_func import plot_hypergeometric

st.title("Discrete Distribution Visualizer")
dist = st.selectbox("Choose a distribution:", ["Poisson", "Binomial", "Hypergeometric"])

if dist == "Poisson":
    st.title("Poisson Distribution Visualizer")
    lmbda = st.slider("Lambda (λ)", 0.1, 10.0, 5.0, 0.1)
    fig = plot_poisson(lmbda)
    st.pyplot(fig)
    
elif dist == "Binomial":
    st.title("Binomial Distribution Visualizer")
    n = st.slider("Number of trials (n)", 1, 50, 10, 1)
    p = st.slider("Probability of success (p)", 0.01, 1.0, 0.5, 0.01)
    fig = plot_binomial(n, p)
    st.pyplot(fig)

elif dist == "Hypergeometric":
    st.title("Hypergeometric Distribution Visualizer")
    N = st.slider("Population size (N)", 5, 100, 20, 1)
    K = st.slider("Number of successes in population (K)", 1, N, 10, 1)
    n = st.slider("Sample size (n)", 1, N, 5, 1)
    fig = plot_hypergeometric(N, K, n)
    st.pyplot(fig)
