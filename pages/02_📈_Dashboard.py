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

def eda_dashboard():
    
    st.subheader(' Univariate Analysis')
    col1, col2, col3 = st.columns(3)


    with col1:
        fig = px.histogram(concat_df, x='tenure', nbins=100, title='Distribution of Tenure')
        st.plotly_chart(fig)
    
        catp1 = sns.catplot(concat_df, y= 'tenure', kind='box', height=3, aspect=2 )
        plt.show()
        st.pyplot(catp1)
   
    with col2:    
        fig1 = px.histogram(concat_df, x='MonthlyCharges', nbins=100, title='Distribution of Monthly Charges')
        st.plotly_chart(fig1)
    
        catp1 = sns.catplot(concat_df, y= 'MonthlyCharges', kind='box', height=3, aspect=2 )
        plt.show()
        st.pyplot(catp1)   
    
    

    with col3:
    
        fig2 = px.histogram(concat_df, x='TotalCharges', nbins=100, title='Distribution of Total Charges')
        st.plotly_chart(fig2)
    
        catp1 = sns.catplot(concat_df, y= 'TotalCharges', kind='box', height=3, aspect=2 )
        plt.show()
        st.pyplot(catp1) 
    
def kpi_dashboard():    
    st.subheader('Bivariate Analysis')    
    col1, col2, col3 = st.columns(3)
    with col1:
        fig4 = px.histogram(concat_df, x='Churn', color='Churn', color_discrete_map={'Yes':'red', 'No':'blue'}, title='Number of Churned Customers')
        st.plotly_chart(fig4)
    
    with col2:    
        fig5 = px.histogram(concat_df, x='Contract', color='Churn', color_discrete_map={'Yes':'red', 'No':'blue'}, title='Number of Churned Customers')
        st.plotly_chart(fig5)

    with col3:    
        fig6 = px.histogram(concat_df, x='PaymentMethod', color='Churn', color_discrete_map={'Yes':'red', 'No':'blue'}, title='Number of Churned Customers')
        st.plotly_chart(fig5)


col7, col8, col9 =st.columns(3)
with col7:    
    catplot1 = sns.catplot(concat_df, x='gender', y= 'tenure', hue='Churn', kind='violin', palette=['blue', 'red'], height=3, aspect=2 )
    st.subheader('How long Female and Male stay with Telco before Churning')
    plt.show()
    st.pyplot(catplot1)

with col8:
    catplot2 = sns.catplot(concat_df, x='Contract', y= 'tenure', hue='Churn', kind='box', aspect=1, palette=['blue', 'red'])
    plt.title('How long does it take each contract type before Churning')
    plt.show()
    st.pyplot(catplot2)
    
    
    
if __name__ == '__main__':
    st.title('Dashboard')
    
    col1, col2 = st.columns(2)
    with col1:
        pass
    with col2:
        st.selectbox('Select Dashboard', options=['EDA', 'KPI'], key='selected_dashboard')
    if st.session_state['selected_dashboard'] == 'EDA':
        eda_dashboard()
    elif st.session_state['selected_dashboard'] == 'KPI':
        kpi_dashboard()
