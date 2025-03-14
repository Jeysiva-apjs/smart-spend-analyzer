import streamlit as st
from add_update import add_tab
from add_update import update_tab
from analytics_category import analytics_category_tab
from analytics_month import analytics_month_tab
from datetime import datetime


# Page Title with Centered Styling
st.markdown("<h1 class='title'>Smart Spend Analyzer</h1>", unsafe_allow_html=True)

# Tabs for Navigation
tab1, tab2, tab3 = st.tabs(["📌 Add/Update", "📊 Analyse by Category", "📆 Analyse by Month"])

# Tab 1: Add/Update Expense
with tab1:
    st.markdown("<div class='date-container'>📅 <h3>Select a Date</h3></div>", unsafe_allow_html=True)
    
    selected_date = st.date_input("", datetime.today().date(), label_visibility="collapsed")

    # Call Functions for Adding and Updating Expense
    add_tab(selected_date)
    update_tab(selected_date)

# Tab 2: Analytics by Category
with tab2:
    analytics_category_tab()

# Tab 3: Analytics by Month
with tab3:
    analytics_month_tab()
    