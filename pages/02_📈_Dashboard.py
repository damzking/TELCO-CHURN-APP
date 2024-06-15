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
    st.markdown('### Exploratory Data Analysis')
    st.markdown('#### Univariate Analysis')
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
        
        
    st.subheader('Bivariate Analysis')    
    col4, col5, col6 = st.columns(3)
    with col4:
        fig4 = px.histogram(concat_df, x='Churn', color='Churn', color_discrete_map={'Yes':'red', 'No':'blue'}, title='Number of Churned Customers')
        st.plotly_chart(fig4)
        
    with col5:    
        fig5 = px.histogram(concat_df, x='Contract', color='Churn', color_discrete_map={'Yes':'red', 'No':'blue'}, title='Number of Churned Customers')
        st.plotly_chart(fig5)

    with col6:    
        fig6 = px.histogram(concat_df, x='PaymentMethod', color='Churn', color_discrete_map={'Yes':'red', 'No':'blue'}, title='Number of Churned Customers')
        st.plotly_chart(fig5)


    col7, col8 =st.columns(2)
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


def kpi_dashboard():
    st.markdown('### Key Performance Indicators')
    
    st.markdown(
        f"""
        <div style= "background-color: #ADD8E6; border-radius: 10px; width: 80%; margin-top: 20px;" >
            <h3 style="margin-left: 30px">Quick Stats About Dataset</h3>
            <hr>
            <h5 style="margin-left: 30px"> Churn Rate: {(concat_df['Churn'].value_counts(normalize = True).get('Yes', 0)* 100):.2f}%.</h5>
            </hr>
            <h5 style="margin-left: 30px"> Average Monthly Charges: ${concat_df['MonthlyCharges'].mean():.2f}</h5>
            </hr>
            <h5 style="margin-left: 30px"> Count of Customers: {concat_df.shape[0]}</h5>
            </hr>
            <h5 style="margin-left: 30px"> Data Size: {concat_df.size}</h5>
        </div>
        """,
        unsafe_allow_html=True
        )


if __name__ == '__main__':
        col1, col2 = st.columns(2)
        with col1:
            pass
        with col2:
            st.selectbox('Select the type of Dashboard', options= ['EDA', 'KPI'], key = 'selected_dashboard_type')
        
        if st.session_state.selected_dashboard_type == 'EDA':
            eda_dashboard()
        else:
            kpi_dashboard()


            