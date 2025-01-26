import config
from backend.database import db_helper

def test_fetch_expenses_for_date():
    expenses = db_helper.fetch_expenses_for_date("2024-12-22")
    
    assert len(expenses) == 2

def test_fetch_expenses_for_date_with_data():
    expenses = db_helper.fetch_expenses_for_date("2025-01-01")

    assert expenses[0]['amount'] == 120.5
    assert expenses[0]['category'] == 'Utilities'
    assert expenses[0]['notes'] == 'Electricity bill for January'

def test_fetch_expenses_for_date_invalid():
    expenses = db_helper.fetch_expenses_for_date("1998-12-22")

    assert len(expenses) == 0

def test_fetch_expense_summary_valid_range():
    summary = db_helper.fetch_expense_summary("2024-12-01", "2024-12-31")
    print(summary)
    assert summary[0]['category'] == 'Utilities'
    assert summary[0]['total'] == 2901.25
    assert summary[1]['category'] == 'Food & Groceries'
    assert summary[1]['total'] == 4551.25
    assert summary[2]['category'] == 'Transportation'
    assert summary[2]['total'] == 3850
    assert summary[3]['category'] == 'Health & Wellness'
    assert summary[3]['total'] == 2150
    assert summary[4]['category'] == 'Entertainment & Leisure'
    assert summary[4]['total'] == 4250
    assert summary[5]['category'] == 'Others'
    assert summary[5]['total'] == 1950

def test_fetch_expense_summary_invalid_range():
    summary = db_helper.fetch_expense_summary("1998-08-01", "1998-08-01")
    assert len(summary) == 0


