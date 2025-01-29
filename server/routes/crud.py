import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import APIRouter, HTTPException
from datetime import date
from typing import List
from pydantic import BaseModel
import database.db_helper as db_helper

router = APIRouter()

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date

@router.get("/expenses", response_model=List[Expense])
def get_all_expenses():
    expenses = db_helper.fetch_all_records()
    return expenses

@router.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses_by_date(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    return expenses

@router.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
    
    return {"message": "expenses updated successfully!"}

@router.post("/analytics")
def get_analytics_data(date_range: DateRange):

    summary = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)

    if not summary or (date_range.start_date > date_range.end_date):
        return {}
    
    total = sum([row['total'] for row in summary])
    summary_by_category = {}

    for row in summary:
        percentage = (row['total']/total) * 100
        summary_by_category[row['category']] = {
            "total": row['total'],
            "percentage": percentage
        }
    
    return summary_by_category

@router.get("/analytics_month")
def get_analytics_by_month():
    summary = db_helper.fetch_expense_summary_month()

    if not summary:
        raise HTTPException(status_code=404, detail="Not able to get the summary.")
    
    summary_by_month = {}

    for row in summary:
        summary_by_month[row['month_year']] = row['total']
    
    return summary_by_month
   

