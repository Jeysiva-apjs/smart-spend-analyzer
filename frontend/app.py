import streamlit as st
from add_update import add_tab
from add_update import update_tab
from analytics_category import analytics_category_tab
from analytics_month import analytics_month_tab
from datetime import date


st.title("Spend Analyzer")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analyse by Category", "Analyse by Month"])

with tab1:
    col1, col2 = st.columns([1, 8])  # Adjust column width as needed
    with col1:
        st.markdown("<p style='margin-bottom:10px; font-size: 27px; font-weight: bold;'>Date:</p>", unsafe_allow_html=True)

    with col2:
        selected_date = st.date_input("Enter Date", date.today(), label_visibility="collapsed")

    st.subheader('Add New Expense')
    add_tab(selected_date)
    update_tab(selected_date)

with tab2:
    analytics_category_tab()

with tab3:
    analytics_month_tab()
    