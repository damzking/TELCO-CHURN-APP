import streamlit as st

st.set_page_config(
    page_title = 'Home Page',
    page_icon = '💒',
    layout = 'wide'
)

st.title("Telco Customer Churn Prediction App")
name = st.text_input("Customer Name")  
st.write(f'Hello {name}!')