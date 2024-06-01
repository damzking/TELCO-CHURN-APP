import streamlit as st

st.set_page_config(
    page_title = 'Home Page',
    page_icon = '💒',
    layout = 'wide'
)

st.title("Telco Customer Churn Prediction App")
name = st.text_input("Customer Name")  
st.write(f'Hello {name}!')

Gender = st.selectbox("Select your Gender:", ["Male", "Female"])
SeniorCitizen = st.selectbox("Select SeniorCitizen:", ["Yes", "No"])
Partner = st.selectbox("Select Partner", ["Yes", "No"])
Dependents = st.selectbox("Select Dependents", ["Yes", "No"])
Tenure = st.number_input("Enter Tenure", key="Tenure_input")
PhoneService = st.selectbox("Select PhoneService", ["Yes", "No"])
MultipleLines = st.selectbox("Select MultipleLines", ["Yes", "No"])
InternetService = st.selectbox("Select InternetService", ['DSL', 'Fiber optic', 'No'])
OnlineSecurity= st.selectbox("Select OnlineSecurity", ["Yes", "No"])
OnlineBackup = st.selectbox("Select OnlineBackup", ["Yes", "No"])
DeviceProtection =st.selectbox("Select DeviceProtection", ["Yes", "No"])
TechSupport = st.selectbox("Select TechSupport", ["Yes", "No"])
StreamingTV = st.selectbox("Select StreamingTV", ["Yes", "No"])
StreamingMovies = st.selectbox("Select StreamingMovies", ["Yes", "No"])
Contract = st.selectbox("Select Contract", ['Month-to-month', 'One year', 'Two year'])
PaperlessBilling = st.selectbox("Select PaperlessBilling", ["Yes", "No"])
PaymentMethod= st.selectbox("Select PaymentMethod", ['Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check'])
MonthlyCharges= st.number_input("Enter MonthlyCharges", key="MonthlyCharges_input")

# Create a function to calculate total charges
def calculate_total_charges(tenure, monthly_charges):
    total_charges = tenure * monthly_charges
    return total_charges

TotalCharges = st.write("Total Charges", calculate_total_charges(Tenure, MonthlyCharges))


if st.button("Predict"):
    st.text("The Customer churn rate is classified to be : '{''}'.")