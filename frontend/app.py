import streamlit as st
from add_update import add_tab
from add_update import update_tab
from analytics_category import analytics_category_tab
from analytics_month import analytics_month_tab
from datetime import datetime


st.title("Smart Spend Analyzer")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analyse by Category", "Analyse by Month"])

with tab1:
    st.markdown("<h3 style='color: #4CAF50; font-weight: bold;'>📅 Select a Date</h3>", unsafe_allow_html=True)
    selected_date = st.date_input("", datetime.today().date(), label_visibility="collapsed")
    add_tab(selected_date)
    update_tab(selected_date)


with tab2:
    analytics_category_tab()

with tab3:
    analytics_month_tab()
    