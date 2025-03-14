# Smart Spend Analyzer

It is a full-stack app for tracking expenses with ML-powered categorization. It allows adding, updating, and analyzing expenses with visualizations by date or month. 

# Demo and live app 
https://jeysiva-apjs-ssa.streamlit.app/

## Features

- **ML-Powered Categorization**: Automatically classify expenses based on user input into categories such as Utilities, Food &      Groceries, Transportation, Health & Wellness, Entertainment and Others.
- **Add and Update Expenses**: Easily add and modify expenses by date and category.
- **Analyze by Date Range**: View your expenses for a selected time period.
- **Monthly Analysis**: See how much you spend each month and track trends.

## Built With

- Python
- FastAPI
- Streamlit
- MySQL DataBase
- Data Visualisation using pandas, matplotlib and seaborn.
- Scikit-learn (Naïve Bayes Multinomial algorithm)


## Project Structure

The project has the following folders:

- **frontend/**: Contains the code for the Streamlit app and ML model.
- **backend/**: Contains the code for the FastAPI server, which handles the data and requests.
- **tests/**: Contains test files to check if everything is working properly.
- **requirements.txt**: Lists all the Python libraries needed to run the project.
- **README.md**: This file, which explains the project and how to use it.

## Getting Started

Follow these steps to set up the **Expense Analyzer** on your system.


### Installation

1. **Clone the project repository:**
   ```bash
   git clone https://github.com/Jeysiva-apjs/spend-analyzer.git
   cd expense-analyzer

2. **Install dependencies:**  
   ```commandline
    pip install -r requirements.txt
   ```

3. **Run the FastAPI server:** 
   ```commandline
    cd backend
    uvicorn main:app --reload
   ```
4. **Run the Streamlit app:**:   
   ```commandline
    cd frontend
    streamlit run app.py
   ```
