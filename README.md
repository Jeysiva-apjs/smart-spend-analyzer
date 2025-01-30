# Expense Analyzer

**Expense Analyzer** is a full-stack app for managing and tracking expenses. It lets you add, update, and categorize expenses while providing analytics to visualize spending by date range or month.

# Demo and live app

- Live App:- [https://spend-analyzer.streamlit.app/](https://jeysiva-apjs-spend-analyzer-clientapp-gwtlpz.streamlit.app/)

![1](https://github.com/user-attachments/assets/95aed0a8-d6fe-4c9c-8124-d96be2903fbb)
![2 1](https://github.com/user-attachments/assets/b8704525-b66e-44ea-9787-8ebf64eac358)


## Built With

- Python
- FastAPI
- Streamlit
- MySQL DataBase
- Data Visualisation using pandas, matplotlib and seaborn.

## Features

- **Add and Update Expenses**: Easily add and change your expenses by date and category.
- **Analyze by Date Range**: View your expenses for a selected time period.
- **Monthly Analysis**: See how much you spend each month and track trends.

## Project Structure

The project has the following folders:

- **frontend/**: Contains the code for the Streamlit app, where you interact with the tool.
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
