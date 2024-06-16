import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier
from catboost import CatBoostClassifier
from xgboost import XGBClassifier
import os
import datetime



st.set_page_config(
    page_title='Predict Page',
    page_icon='🔍',
    layout='wide'
)





st.title('Predict Telco Customer Churn')


st.cache_resource()
def load_XGBoost_pipeline():
    pipeline = joblib.load('./models/XGBoost_pipeline.joblib')
    return pipeline


st.cache_resource()
def load_Cat_Boost_pipeline():
    pipeline = joblib.load('./models/CatBoost_pipeline.joblib')
    return pipeline


st.cache_resource()
def GB_pipeline():
    pipeline = joblib.load('./models/GBC_pipeline.joblib')
    return pipeline


st.cache_resource()
def load_custom_imputer():
    return joblib.load('./models/custom_imputer.joblib')


st.cache_resource(show_spinner= 'Model Loading....')
def select_model():
    col1, col2 = st.columns(2)
    
    with col1:
        st.selectbox('Select Model', options=['XGBoost', 'Gradient Boosting', 'Category Boosting'], key='selected_model')

    with col2:
        pass
    
    if st.session_state['selected_model'] == 'XGBoost':
        pipeline = load_XGBoost_pipeline()
        
    elif st.session_state['selected_model'] == 'Category Boosting':
        pipeline = load_Cat_Boost_pipeline()
    else:
        pipeline = GB_pipeline()
    
    encoder = joblib.load('./models/encoder.joblib')
    
    return pipeline, encoder


def make_prediction(pipeline, encoder):
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
    data = [[gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges]]
    columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges']
    df = pd.DataFrame(data, columns=columns)
    pred = pipeline.predict(df)
    pred_int = int(pred[0])
    prediction = encoder.inverse_transform([pred_int])[0]
    probability = pipeline.predict_proba(df)[0]

    st.session_state['prediction'] = prediction
    st.session_state['probability'] = probability
    
    # Save results
    final_probability = round(probability[pred_int], 2)
    df['prediction'] = prediction
    df['probability'] = final_probability
    
    df['model_used'] = st.session_state['selected_model']

    history_file_path = './models/history.csv'
    df.to_csv(history_file_path, mode='a', header=not os.path.exists(history_file_path), index=False)

    
    
    return prediction , probability


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
            st.selectbox('Customer gender', options =['Male', 'Female'], key='gender', placeholder='Select Gender')
            st.selectbox('Is Customer a SeniorCitizen', options =['Yes', 'No'], key='SeniorCitizen')
            st.selectbox('Does Customer have a partner?', options =['Yes', 'No'], key='Partner')
            st.selectbox('Does Customer have Dependents?', options =['Yes', 'No'], key='Dependents')
            st.number_input('tenure', key='tenure', min_value=0, step=1)
            st.selectbox('Does Telco provide Phone Service', options =['Yes', 'No'], key='PhoneService')
            st.selectbox('Does Customer have Multiple Lines', options =['Yes', 'No'], key='MultipleLines')
            st.selectbox('Which type of Internet Service', options =['DSL', 'Fiber optic'], key='InternetService')
            st.selectbox('Does Telco provide Online Security', options =['Yes', 'No'], key='OnlineSecurity')
            st.selectbox('Does Telco provide Online Backup', options =['Yes', 'No'], key='OnlineBackup', )
        with col2:
            st.write('### ....')  
            st.selectbox('Does Telco provide Device Protection', options =['Yes', 'No'], key='DeviceProtection')
            st.selectbox('Does Telco provide Tech Support', options =['Yes', 'No'], key='TechSupport')
            st.selectbox('Does Telco provide Streaming TV', options =['Yes', 'No'], key='StreamingTV')
            st.selectbox('Does Telco provide Streaming Movies', options =['Yes', 'No'], key='StreamingMovies')
            st.selectbox('Which type of Contract', options =['Month-to-month', 'One year', 'Two year'], key='Contract')
            st.selectbox('Paperless Billing', options =['Yes', 'No'], key='PaperlessBilling')
            st.selectbox('Payment Method', options =['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], key='PaymentMethod')
            st.number_input('Monthly Charges', key='MonthlyCharges')
            st.number_input('Total Charges', key='TotalCharges')
        st.form_submit_button('Predict', on_click=make_prediction, kwargs=dict(pipeline=pipeline, encoder=encoder)) # st.form_submit_button('submit', on_click=make_prediction, kwargs=dict(pipeline=pipeline, encoder=encoder))

if __name__ == '__main__':
    
    display_form()
    if not st.session_state['prediction']:
        st.write('### Prediction show here')
    else:
        st.write(f'### Prediction: :red[{st.session_state["prediction"][0]}]')
        st.write(f'### Churned: :red[{st.session_state["prediction"][0] == "Yes"}]')
        st.write(f'### Probability: :green[{st.session_state["probability"][0]}]')
        
        
    
st.write(st.session_state)
