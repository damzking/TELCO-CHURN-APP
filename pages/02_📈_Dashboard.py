import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px

st.set_page_config(
    page_title = 'Dashboard Page',
    page_icon = '📊',
    layout = 'wide'
)

st.title('EDA & Dashboard')

@st.cache_data
def load_concat_data():
    concat_df = pd.read_csv('Data/df_churn.csv')
    return concat_df

concat_df = load_concat_data()
st.write(concat_df)

#st.bar_chart(concat_df, y='tenure', x='gender', width=50, height=300)

df = px.concat_df.tips()
fig = px.histogram(df, x='tenure', nbins=20)
fig.show()
