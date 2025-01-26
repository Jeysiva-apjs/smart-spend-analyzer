import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


API_URL = "http://localhost:8000"


def analytics_category_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2025, 1, 1))

    with col2:
        end_date = st.date_input("End Date", datetime(2025, 1, 5))

    chart_type = st.selectbox(
        "Choose Chart Type",
        options=["Pie Chart", "Bar Chart"],
        index=0,  # Default selection
    )
    st.write("")
    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/", json=payload)
        response = response.json()

        data = {
            "Category": list(response.keys()),
            "Total": [response[category]["total"] for category in response],
            "Percentage": [response[category]["percentage"] for category in response]
        }

        df = pd.DataFrame(data)
        # st.title("Expense Breakdown By Category")

        # palette = sns.color_palette("pastel", len(df))


        # # Plotting with matplotlib
        # fig, ax = plt.subplots(figsize=(8, 4)) 
        # ax.bar(df["Category"], df["Percentage"], color=palette)
        # ax.set_xlabel("Category", fontsize=14)
        # ax.set_ylabel("Percentage", fontsize=14)
        # plt.xticks(rotation=0, fontsize=7)  # Rotate x-axis labels at 45 degrees


        # Streamlit App
        st.title("Expense Breakdown By Category")

        # Define a color palette
        palette = sns.color_palette("pastel", len(df))

        # Plotting with matplotlib
        if chart_type == "Bar Chart":
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.bar(df["Category"], df["Percentage"], color=palette)
            ax.set_xlabel("Category", fontsize=14)
            ax.set_ylabel("Percentage", fontsize=14)
            plt.xticks(rotation=0, fontsize=7)
            st.pyplot(fig)  # Display the bar chart
        elif chart_type == "Pie Chart":
            fig, ax = plt.subplots(figsize=(4, 4))
            wedges, texts, autotexts = ax.pie(
                df["Percentage"],
                labels=None,  # Remove labels from the pie chart
                autopct="%1.1f%%",
                colors=palette,
                startangle=90
            )
            for autotext in autotexts:
                autotext.set_fontsize(5)  # Adjust the number to your desired font size

            # Add a legend for the categories
            ax.legend(
                wedges, 
                df["Category"],
                title="Categories",
                loc="center left", 
                bbox_to_anchor=(1, 0, 0.5, 1)
            )

            st.pyplot(fig)
        
        st.table(df)