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

col1, col2 = st.columns(2)
with col1:
    pass
    #st.image('resources/dashb1.jpg', width=200)
with col2:
    st.title(':rainbow-background[EDA & Dashboard]')

@st.cache_data()
def load_concat_data():
    concat_df = pd.read_csv('Data/df_churn.csv')
    return concat_df

concat_df = load_concat_data()

if st.checkbox('Show data'):
    st.subheader('Telco churn data')
    st.write(concat_df)

#@st.cache_data()
def eda_dashboard():
    
    st.subheader(' :rainbow[Univariate Analysis]')
    col1, col2, col3 = st.columns(3)

    with col1:
        fig = px.histogram(concat_df, x='tenure', nbins=100, title='Distribution of Tenure', color_discrete_sequence=['springgreen', 'lemonchiffon'])
        st.plotly_chart(fig)
    
        catp1 = px.box(concat_df, x= 'tenure', title='Boxplot of Tenure', color_discrete_sequence=['springgreen', 'lemonchiffon'])
        st.plotly_chart(catp1)

    with col2:    
        fig1 = px.histogram(concat_df, x='MonthlyCharges', nbins=100, title='Distribution of Monthly Charges', color_discrete_sequence=['royalblue', 'lemonchiffon'])
        st.plotly_chart(fig1)

        figc1 = px.box(concat_df, x='MonthlyCharges', title='Boxplot of Monthly Charges', color_discrete_sequence=['royalblue', 'lemonchiffon'])
        st.plotly_chart(figc1)   
    
    with col3:
    
        fig2 = px.histogram(concat_df, x='TotalCharges', nbins=100, title='Distribution of Total Charges', color_discrete_sequence=['magenta', 'lemonchiffon'])
        st.plotly_chart(fig2)
    
        catp1 = px.box(concat_df, x= 'TotalCharges', title='Boxplot of Total Charges', color_discrete_sequence=['magenta', 'lemonchiffon'])
        st.plotly_chart(catp1) 
    
    col1, col2 = st.columns(2)
    with col1:
        fignum = px.histogram(concat_df.select_dtypes(include=np.number), barmode='overlay', title='Number of Churned Customers')
        st.plotly_chart(fignum)
        
    with col2:
        figcat = px.box(concat_df.select_dtypes(include=np.number), title='Number of Churned Customers')
        st.plotly_chart(figcat)
    
    st.subheader(' :rainbow[Bivariate Analysis]')
    sns.set(style="ticks")
    pairplot = sns.pairplot(concat_df, hue='Churn', height=1.5, aspect=2)
    plt.subplots_adjust(top=0.9)
    plt.suptitle('Customer Churn Pairplot', fontsize=20)

    for ax in pairplot.axes.flatten():
        for label in ax.get_xticklabels():
            label.set_rotation(45)
        for label in ax.get_yticklabels():
            label.set_rotation(45)
    st.pyplot(pairplot)
    
    col4, col5, col6 = st.columns(3)
    with col4:
        fig4 = px.histogram(concat_df, x='Churn', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Number of Churned Customers')
        st.plotly_chart(fig4)
    
    with col5:    
        fig5 = px.histogram(concat_df, x='Contract', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Type of Contract and Customer Churn')
        st.plotly_chart(fig5)

    with col6:    
        fig6 = px.histogram(concat_df, x='PaymentMethod', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Type of Payment Method and Customer Churn')
        st.plotly_chart(fig6)
        
    col7, col8, col9 =st.columns(3)
    with col7:
        fig7 = px.histogram(concat_df, x='gender', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Gender and Customer Churn')
        st.plotly_chart(fig7)
    with col8:
        fig8 = px.histogram(concat_df, x='SeniorCitizen', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Senior Citizen and Customer Churn')
        st.plotly_chart(fig8)
    with col9:
        fig9 = px.histogram(concat_df, x='Partner', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Customers with Partner and Churn')
        st.plotly_chart(fig9)
        
    col10, col11, col12 = st.columns(3)
    with col10:
        fig10 = px.histogram(concat_df, x='InternetService', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Internet Service and Customer Churn')
        st.plotly_chart(fig10)
    with col11:
        fig11 = px.histogram(concat_df, x='OnlineSecurity', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Online Security and Customer Churn')
        st.plotly_chart(fig11)
    with col12:
        fig12 = px.histogram(concat_df, x='OnlineBackup', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Online Backup and Customer Churn')
        st.plotly_chart(fig12)
        
    col13, col14, col15 = st.columns(3)
    with col13:
        fig13 = px.histogram(concat_df, x='DeviceProtection', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Device Protection and Customer Churn')
        st.plotly_chart(fig13)
    with col14:
        fig14 = px.histogram(concat_df, x='TechSupport', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Tech Support and Customer Churn')
        st.plotly_chart(fig14)
    with col15:
        fig15 = px.histogram(concat_df, x='StreamingTV', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Streaming TV and Customer Churn')
        st.plotly_chart(fig15)
        
    col16, col17 = st.columns(2)
    with col16:
        fig16 = px.histogram(concat_df, x='StreamingMovies', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Streaming Movies and Churned Customers')
        st.plotly_chart(fig16)
    with col17:
        fig17 = px.histogram(concat_df, x='PaperlessBilling', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Paperless Billing and Churned Customers')
        st.plotly_chart(fig17)
        
    col18, col19, col20 = st.columns(3)
    with col18:
        fig19 = px.histogram(concat_df, x='tenure', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Tenure and Churned Customers')
        st.plotly_chart(fig19)
    with col19:
        fig20 = px.histogram(concat_df, x='MonthlyCharges', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Monthly Charges and Churned Customers')
        st.plotly_chart(fig20)
    with col20:
        fig21 = px.histogram(concat_df, x='TotalCharges', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Total Charges and Churned Customers')
        st.plotly_chart(fig21)
    
    col21, col22, col23 =st.columns(3)
    with col21:    
        catplot1 = px.box(concat_df, x='gender', y= 'tenure', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='How long it took Customers to Churn')
        st.plotly_chart(catplot1)

    with col22:
        catplot2 = px.box(concat_df, x='Contract', y= 'tenure', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Which Contract type did Customers Churned')
        st.plotly_chart(catplot2)
        
    with col23:
        cat1 = px.bar(concat_df, x='SeniorCitizen', y= 'tenure', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Did Senior Citizens Churn')
        st.plotly_chart(cat1)
        
    col24, col25= st.columns(2)
    with col24:
        kpi1 = px.bar(concat_df, x='Dependents', y= 'tenure', color='Churn', color_discrete_map={'Yes':'turquoise', 'No':'slateblue'}, title='Customers with Dependents and Churn')
        st.plotly_chart(kpi1)
    with col25:
        kp2 = sns.catplot(data=concat_df, x='gender', y='tenure', hue='Churn', kind='bar', col='PaymentMethod', aspect=.7, palette=['blue', 'red'])
    st.pyplot(kp2)

        
#@st.cache_data()
def kpi_dashboard():    
    st.subheader(':rainbow[Key Performance Indicators]')
    
    st.markdown(
        f"""
        <div style= "background-color: purple; border-radius: 10px; width: 60%; margin-top: 20px;" >
            <h3 style="margin-left: 30px">Quick Stats About Dataset</h3>
            <hr>
            <h5 style="margin-left: 30px"> Churn Rate: {(concat_df['Churn'].value_counts(normalize = True).get('Yes', 0)* 100):.2f}%.</h5>
            </hr>
            <h5 style="margin-left: 30px"> Average Monthly Charges: ${concat_df['MonthlyCharges'].mean():.2f}</h5>
            </hr>
            <h5 style="margin-left: 30px"> Count of Churned Customers : {concat_df['Churn'].value_counts().get('Yes')}</h5>
            </hr>
            <h5 style="margin-left: 30px"> Count of Retained Customers : {concat_df['Churn'].value_counts().get('No')}</h5>
            </hr>
            <h5 style="margin-left: 30px"> Data Size: {concat_df.size}</h5>
        </div>
        """,
        unsafe_allow_html=True
        )

            
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


            