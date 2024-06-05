import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
st.set_page_config(
    page_title='Predict Page',
    page_icon='🔍',
    layout='wide'
)

st.title('Telco Customer Churn Prediction 🔍')

classifier_name = st.sidebar.selectbox(
    'Select Classifier',
    ('Gradient Boosting', 'Category_Boosting')
)

@st.cache_resource
def load_model(classifier_name):
    if classifier_name == 'Gradient Boosting':
        model = joblib.load('models\Gradient_Boosting_tunedb.joblib')  # Replace with the actual path
    elif classifier_name == 'Category_Boosting':
        model = joblib.load('models\Category_Boosting_tunedb.joblib')  # Replace with the actual path
    return model

import streamlit as st
import joblib
import pandas as pd

st.sidebar.title("Select Classifier")
classifier_name = st.sidebar.selectbox('', ('Gradient Boosting', 'Category Boosting'))

@st.cache_resource
def load_model(classifier_name):
    if classifier_name == 'Gradient Boosting':
        model = joblib.load('models\Gradient_Boosting_tunedb.joblib')  # Replace with the actual path
    elif classifier_name == 'Category_Boosting':
        model = joblib.load('models\Category_Boosting_tunedb.joblib')  # Replace with the actual path
    return model

@st.cache_data
def load_data():
    return pd.read_csv('data/df_churn.csv')

data = load_data()
st.write(data.head())  # Display the data for reference

model = load_model(classifier_name)
if model:
    st.write(f"Model '{classifier_name}' loaded successfully!")
else:
    st.error("Model loading failed.")

if classifier_name == 'Gradient Boosting':
    st.write(f"Selected Classifier: {classifier_name}")
    st.write("Training Gradient Boosting Model...")
    
    # Example: Instantiate and train Gradient Boosting model
    X = data.drop('Churn', axis=1)  # Replace 'target_column_name' with the actual target column name
    y = data['Churn']  # Replace 'target_column_name' with the actual target column name
    model = GradientBoostingClassifier()
    model.fit(X, y)

    # Make predictions
    predictions = model.predict(X)
    st.write(f"Predictions using {classifier_name}:")
    st.write(predictions)






