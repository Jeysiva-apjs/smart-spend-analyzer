import streamlit as st
from add_update import add_update_tab
from analytics_category import analytics_category_tab
from analytics_month import analytics_month_tab

st.title("Spend Analyzer")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analyse by Category", "Analyse by Month"])

with tab1:
    add_update_tab()

with tab2:
    analytics_category_tab()

with tab3:
    analytics_month_tab()
    