from database.connection import get_db_cursor

def fetch_all_records():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * from expenses")
        expenses = cursor.fetchall()
        return expenses

def fetch_expenses_for_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses


def insert_expense(expense_date, amount, category, notes):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )


def delete_expenses_for_date(expense_date):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def fetch_expense_summary(start_date, end_date):
    with get_db_cursor() as cursor:
        cursor.execute('''
        SELECT category, ROUND(SUM(amount), 2) as total
        FROM expenses
        WHERE expense_date BETWEEN %s AND %s
        GROUP BY category''', (start_date, end_date))

        summary = cursor.fetchall()
        return summary

def fetch_expense_summary_month():

    with get_db_cursor() as cursor:
        cursor.execute('''
        SELECT 
            MONTH(expense_date) as month, 
            YEAR(expense_date) as year,
            CONCAT(SUBSTRING(MONTHNAME(expense_date), 1, 3), " ", YEAR(expense_date)) AS month_year,
            ROUND(SUM(amount), 2) as total
        FROM expenses
        GROUP BY year, month
        ORDER BY year, month''')

        summary = cursor.fetchall()
        return summary