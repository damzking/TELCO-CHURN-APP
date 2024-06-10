import streamlit as st
import joblib
import pandas as pd
import numpy as np
from catboost import CatBoostClassifier
from xgboost import XGBClassifier
from custom_imputer import CustomImputer
from imblearn.over_sampling import SMOTE

st.set_page_config(
    page_title='Predict Page',
    page_icon='🔍',
    layout='wide'
)

st.title('Telco Customer Churn Prediction 🔍')

@st.cache_resource
def load_forest_pipeline():
    return joblib.load('./models/forest_pipeline.joblib')

@st.cache_resource
def load_svc_pipeline():
    return joblib.load('./models/svc_pipeline.joblib')

@st.cache_resource(show_spinner='Model is loading...')
def select_model():
    col1, col2 = st.columns(2)
    
    with col1:
        selected_model = st.selectbox('Select a model', options=['Random Forest', 'SVC'], key='selected_model')
    
    if selected_model == 'Random Forest':
        pipeline = load_forest_pipeline()
    else:
        pipeline = load_svc_pipeline()
    
    encoder = joblib.load('./models/encoder.joblib')
    
    return pipeline, encoder

pipeline, encoder = select_model()

st.write(f"Model '{st.session_state['selected_model']}' loaded successfully!")

def make_prediction(pipeline, encoder):
    customerID = st.session_state['customerID']
    gender = st.session_state['gender']
    SeniorCitizen = st.session_state['SeniorCitizen']
    Partner = st.session_state['Partner']
    Dependents = st.session_state['Dependents']
    tenure = st.session_state['tenure']
    PhoneService = st.session_state['PhoneService']
    MultipleLines = st.session_state['MultipleLines']
    InternetService = st.session_state['InternetService']
    OnlineSecurity = st.session_state['OnlineSecurity']
    OnlineBackup = st.session_state['OnlineBackup']
    DeviceProtection = st.session_state['DeviceProtection']
    TechSupport = st.session_state['TechSupport']
    StreamingTV = st.session_state['StreamingTV']
    StreamingMovies = st.session_state['StreamingMovies']
    Contract = st.session_state['Contract']
    PaperlessBilling = st.session_state['PaperlessBilling']
    PaymentMethod = st.session_state['PaymentMethod']
    MonthlyCharges = st.session_state['MonthlyCharges']
    TotalCharges = st.session_state['TotalCharges']

  

    data = [[customerID, gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges]]
    columns = ['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges']
    df = pd.DataFrame(data, columns=columns)
    pred = pipeline.predict(df)
    pred_int = int(pred[0])
    prediction = encoder.inverse_transform([pred_int])
    probability = pipeline.predict_proba(df)
    st.session_state['prediction'] = prediction
    st.session_state['probability'] = probability
    return prediction

if 'prediction' not in st.session_state:
    st.session_state['prediction'] = None
if 'probability' not in st.session_state:
    st.session_state['probability'] = None

def display_form():
    pipeline, encoder = select_model()
    with st.form('my_form'):
        col1, col2 = st.columns(2)
        with col1:
            st.write('### Select/Input parameters :info:')
            st.selectbox('Customer gender', options=['Male', 'Female'], key='gender', placeholder='Select Gender')
            st.selectbox('Is Customer a SeniorCitizen', options=['Yes', 'No'], key='SeniorCitizen')
            st.selectbox('Does Customer have a partner?', options=['Yes', 'No'], key='Partner')
            st.selectbox('Does Customer have Dependents?', options=['Yes', 'No'], key='Dependents')
            st.number_input('tenure', key='tenure', min_value=0, step=1)
            st.selectbox('Does Telco provide Phone Service', options=['Yes', 'No'], key='PhoneService')
            st.selectbox('Does Customer have Multiple Lines', options=['Yes', 'No'], key='MultipleLines')
            st.selectbox('Which type of Internet Service', options=['DSL', 'Fiber optic'], key='InternetService')
            st.selectbox('Does Telco provide Online Security', options=['Yes', 'No'], key='OnlineSecurity')
            st.selectbox('Does Telco provide Online Backup', options=['Yes', 'No'], key='OnlineBackup')
        with col2:
            st.write('### ....')  
            st.selectbox('Does Telco provide Device Protection', options=['Yes', 'No'], key='DeviceProtection')
            st.selectbox('Does Telco provide Tech Support', options=['Yes', 'No'], key='TechSupport')
            st.selectbox('Does Telco provide Streaming TV', options=['Yes', 'No'], key='StreamingTV')
            st.selectbox('Does Telco provide Streaming Movies', options=['Yes', 'No'], key='StreamingMovies')
            st.selectbox('Which type of Contract', options=['Month-to-month', 'One year', 'Two year'], key='Contract')
            st.selectbox('Paperless Billing', options=['Yes', 'No'], key='PaperlessBilling')
            st.selectbox('Payment Method', options=['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], key='PaymentMethod')
            st.number_input('Monthly Charges', key='MonthlyCharges')
            st.number_input('Total Charges', key='TotalCharges')
        st.form_submit_button('Predict', on_click=make_prediction, kwargs=dict(pipeline=pipeline, encoder=encoder))


if __name__ == '__main__':
    display_form()
    
    final_prediction = st.session_state['prediction']
    
    if final_prediction is None:
        st.write('### Prediction shows here')
        st.divider()
    else:
        st.write(final_prediction)
    
    st.write(st.session_state)
