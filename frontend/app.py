import streamlit as st
from add_update import add_tab
from add_update import update_tab
from analytics_category import analytics_category_tab
from analytics_month import analytics_month_tab
from datetime import datetime


# Apply custom styling to center content
st.markdown("""
    <style>
        .main {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        div.block-container {
            max-width: 700px;
        }
        .stTabs [role="tablist"] {
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("\U0001F4B8 Smart Spend Analyzer")

# Tabs
tab1, tab2, tab3 = st.tabs(["➕ Add/Update", "📊 Analyse by Category", "📆 Analyse by Month"])

with tab1:
    selected_date = st.date_input("Enter Date", datetime.date(2025, 1, 1), label_visibility="collapsed")
    add_tab(selected_date)
    update_tab(selected_date)

with tab2:
    analytics_category_tab()

with tab3:
    analytics_month_tab()
    