import streamlit as st
import requests
import time
from expense_categorizer.categorizer_helper import categorise_expense

API_URL = "https://spend-analyzer-git-main-jey-projects.vercel.app"

def add_tab(selected_date):
    with st.form(key="expense_add_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Notes")

        amount = 0.0
        notes = ""

        col1, col2 = st.columns(2)
        with col1:
            amount_input = st.number_input(label="Amount", min_value=0.0, step=1.0, value=amount, label_visibility="collapsed")
        with col2:
            notes_input = st.text_input(label="Notes", value=notes, label_visibility="collapsed")

        expense = {
            'amount': amount_input,
            'category': categorise_expense(notes_input),
            'notes': notes_input
        }

        submit_button = st.form_submit_button(label='Add Expense')

        print(expense)

        if submit_button:
            response = requests.post(f"{API_URL}/expenses/add/{selected_date}", json=expense)

            if response.status_code == 200:
                st.success("Expense added successfully!")
                time.sleep(2)
                st.rerun()
            else:
                st.error("Failed to add expense.")


def update_tab(selected_date):
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    existing_expenses = []
    if response.status_code == 200:
        existing_expenses = response.json()
    
    if len(existing_expenses) == 0:
        return
    

    categories = ["Utilities", "Food & Groceries", "Transportation", "Health & Wellness", "Entertainment", "Others"]


    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")
        


        expenses = []
        for i in range(0, len(existing_expenses)):
            amount = existing_expenses[i]['amount']
            category = existing_expenses[i]["category"]
            notes = existing_expenses[i]["notes"]

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(label="Amount", min_value=0.0, step=1.0, value=amount, key=f"amount_{i}",
                                               label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="Category", options=categories, index=categories.index(category),
                                              key=f"category_{i}", label_visibility="collapsed")
            with col3:
                notes_input = st.text_input(label="Notes", value=notes, key=f"notes_{i}", label_visibility="collapsed")

            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })

        submit_button = st.form_submit_button(label="Update Expenses")

        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]

            response = requests.post(f"{API_URL}/expenses/update/{selected_date}", json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expenses updated successfully!")
                time.sleep(2)
                st.rerun()
            else:
                st.error("Failed to update expenses.")