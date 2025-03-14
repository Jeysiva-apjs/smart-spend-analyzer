import pandas as pd
import joblib
import os 

# Get the absolute path of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Correct path
model_path = os.path.join(BASE_DIR, "model.joblib")
vector_path = os.path.join(BASE_DIR, "count_vectorizer.joblib")

# Load the model
model = joblib.load(model_path)
count_vectorizer = joblib.load(vector_path)

import os
print("Current working directory:", os.getcwd())


def categorise_expense(notes_input):
    data = count_vectorizer.transform([notes_input])
    category = model.predict(data)
    return str(category[0])

