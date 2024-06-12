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

if st.checkbox('Show data'):
    st.subheader('Telco churn data')
    st.write(concat_df)

col1, col2, col3 = st.columns(3)

with col1:
    #st.subheader('Number of Churned Customers')
    #fig = px.histogram(concat_df, x='Churn', color='Churn', color_discrete_map={'Yes':'red', 'No':'blue'}, title='Number of Churned Customers')
    fig = px.histogram(concat_df, x='tenure', nbins=100, title='Distribution of Tenure')
    st.plotly_chart(fig)
with col2:    
    fig1 = px.histogram(concat_df, x='MonthlyCharges', nbins=100, title='Distribution of Monthly Charges')
    st.plotly_chart(fig1)   
    
    

with col3:
    
    fig2 = px.histogram(concat_df, x='TotalCharges', nbins=100, title='Distribution of Total Charges')
    st.plotly_chart(fig2)
    
    sns.set(style="ticks")
    pairplot = sns.pairplot(concat_df, hue='Churn', height=1.2, aspect=2)
    plt.subplots_adjust(top=0.9)
    plt.suptitle('Customer Churn Pairplot', fontsize=20)

    for ax in pairplot.axes.flatten():
        for label in ax.get_xticklabels():
            label.set_rotation(25)
        for label in ax.get_yticklabels():
            label.set_rotation(25)
    st.pyplot(pairplot)
    
col4, col5 = st.columns(2)
with col4:
    fig4 = px.histogram(concat_df, x='Churn', color='Churn', color_discrete_map={'Yes':'red', 'No':'blue'}, title='Number of Churned Customers')
    st.plotly_chart(fig4)
    
    fig5 = px.histogram(concat_df, x='Contract', color='Churn', color_discrete_map={'Yes':'red', 'No':'blue'}, title='Number of Churned Customers')
    st.plotly_chart(fig5)
    
    fig6 = px.histogram(concat_df, x='PaymentMethod', color='Churn', color_discrete_map={'Yes':'red', 'No':'blue'}, title='Number of Churned Customers')
    st.plotly_chart(fig5)

with col5:    
    catplot1 = sns.catplot(concat_df, x='gender', y= 'tenure', hue='Churn', kind='violin', palette=['blue', 'red'], height=3, aspect=2 )
    st.subheader('How long Female and Male stay with Telco before Churning')
    plt.show()
    st.pyplot(catplot1)

    catplot2 = sns.catplot(concat_df, x='Contract', y= 'tenure', hue='Churn', kind='box', aspect=1, palette=['blue', 'red'])
    plt.title('How long does it take each contract type before Churning')
    plt.show()
    st.pyplot(catplot2)