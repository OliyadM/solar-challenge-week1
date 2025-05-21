import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_boxplot(df, column, country):
    fig, ax = plt.subplots()
    sns.boxplot(y=df[column], ax=ax)
    ax.set_title(f'{column} for {country}')
    return fig