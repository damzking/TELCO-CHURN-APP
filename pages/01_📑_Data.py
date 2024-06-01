import streamlit as st
import pyodbc
import pandas as pd


st.set_page_config(
    page_title = 'Home Page',
    page_icon = '💒',
    layout = 'wide'
)

st.title("Telco Customer Churn Prediction Database 🔋")

# Create a connection to database
# Query database

def init_connection():
    pyodbc.connect(
        "driver='{SQL SERVER}' SERVER = ",
        + st.secrets['server']
        + ";database"
        + st.secrets['database']
        + ";uid="
        + st.secrets['username']
        + ";pwd="
        + st.secrets['password']
    )

