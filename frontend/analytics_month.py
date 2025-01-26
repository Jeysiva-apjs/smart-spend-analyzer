import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_URL = "https://spend-analyzer-git-main-jey-projects.vercel.app"

def analytics_month_tab():
    response = requests.get(f"{API_URL}/analytics_month")
    response = response.json()

    data = {
        "Month": list(response.keys()),
        "Total": list(response.values())
    }

    df = pd.DataFrame(data)
    df["Total"] = df["Total"].apply(lambda x: round(x, 2))

    # Streamlit App
    st.title("Expense Breakdown By Month")

    # Define a color palette
    palette = sns.color_palette("pastel", len(df))

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(df["Month"], df["Total"], color=palette)
    ax.set_xlabel("Month", fontsize=14)
    ax.set_ylabel("Expense", fontsize=14)
    plt.xticks(rotation=0, fontsize=7)

    st.pyplot(fig)

    # Add a total row and round the values to 2 decimal points
    total = round(df['Total'].sum(), 2)
    df.loc[len(df)] = ['Total', total]

    # Display the dataframe in Streamlit
    st.table(df)
