import streamlit as st
import os
import pandas as pd

# Set the page configuration
st.set_page_config(
    page_title='History Page',
    page_icon='🗓',
    layout='wide'
)



def historic_prediction():
    csv_path = 'Data/history.csv'
    csv_exists = os.path.exists(csv_path)

    if csv_exists:
        history = pd.read_csv(csv_path)
        st.dataframe(history)

if __name__ == "__main__":
    st.title(":rainbow[Prediction History]")
    historic_prediction()
