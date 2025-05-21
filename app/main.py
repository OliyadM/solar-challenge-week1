import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

st.title("Solar Data Dashboard - MoonLight Energy Solutions")

@st.cache_data
def load_data(country):
    try:
        # Get the absolute path to the data directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        data_file = os.path.join(parent_dir, 'data', f'{country}_clean.csv')
        return pd.read_csv(data_file)
    except FileNotFoundError:
        st.error(f"Data file for {country} not found!")
        return None

# Country selection
country = st.selectbox("Select Country", ["Benin", "Sierra Leone", "Togo"])
df = load_data(country.lower())
if df is not None:
    # GHI Boxplot
    st.subheader(f"GHI Distribution for {country}")
    fig, ax = plt.subplots()
    sns.boxplot(y=df['GHI'], ax=ax)
    ax.set_title(f"GHI for {country}")
    st.pyplot(fig)

    # Cross-Country Summary
    st.subheader("Cross-Country Comparison")
    summary_stats = pd.read_csv('../data/summary_stats.csv')
    st.table(summary_stats)