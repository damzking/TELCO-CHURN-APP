import streamlit as st
import os
import pandas as pd

st.set_page_config(
    page_title = 'History Page',
    page_icon = '🗓',
    layout = 'wide'
)

col1, col2 = st.columns(2)
with col1:
    st.image('resources/imageshist.jfif', width=200)
with col2:
    st.header(':rainbow-background[Historic Predictions]')
    
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

def display_historic_predictions():
    st.subheader(":violet[Displaying historic predictions]")
    csv_path = './data/history.csv'
    csv_exists = os.path.isfile(csv_path)

    if csv_exists:
        history = pd.read_csv(csv_path)
        
        st.dataframe(history)
        
if __name__ == '__main__':
    display_historic_predictions()