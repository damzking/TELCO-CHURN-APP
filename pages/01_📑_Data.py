import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title='Data Page',
    page_icon='🗃',
    layout='wide'
)

with open('.streamlit/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

@st.cache_data
def load_data0():
    data0 = pd.read_csv('Data/telco_churn_sql.csv')
    return data0

@st.cache_data
def load_data():
    data = pd.read_csv('Data/telco_churn_git.csv')
    return data

@st.cache_data
def load_concat_data():
    concat_df = pd.read_csv('Data/df_churn.csv')
    return concat_df

# Function to get all columns from a specific table
st.cache_resource()
def get_all_column():
    data0 = pd.read_csv("Data/telco_churn_sql.csv")
    data = pd.read_csv('Data/telco_churn_git.csv')
    concat_df = pd.read_csv('Data/df_churn.csv')
    st.session_state['data0'], st.session_state['data'], st.session_state['concat_df'] = data0, data, concat_df

# Initialize the dataframe in session state if not already there
if 'data0' not in st.session_state and 'data' not in st.session_state and 'concat_df' not in st.session_state:
    get_all_column()
    
def select_data():
    st.subheader('Telco churn data Category')
    col1, col2 = st.columns(2)
    with col1:
        # Dropdown select box
        selection = st.selectbox('Select Columns of Data', options=['All columns', 'Numerical Columns', 'Categorical Columns'], on_change=get_all_column)
    with col2:
        pass
    # Filter the DataFrame based on the selection
    if selection == 'Numerical Columns':
        data0_to_display = st.session_state['data0'].select_dtypes(include=['number'])
        data_to_display = st.session_state['data'].select_dtypes(include=['number'])
        concat_df_to_display = st.session_state['concat_df'].select_dtypes(include=['number'])
    elif selection == 'Categorical Columns':
        data0_to_display = st.session_state['data0'].select_dtypes(include=['object', 'category'])
        data_to_display = st.session_state['data'].select_dtypes(include=['object', 'category'])
        concat_df_to_display = st.session_state['concat_df'].select_dtypes(include=['object', 'category'])    
    else:
        data0_to_display = st.session_state['data0']
        data_to_display = st.session_state['data']
        concat_df_to_display = st.session_state['concat_df']
    # Display the DataFrame
    
    if st.checkbox('Show data from SQL'):
        st.subheader(f'**{selection}**')
        st.write(data0_to_display)
    
    if st.checkbox('Show data from GitHub'):    
        st.subheader(f'**{selection}**')
        st.write(data_to_display)

    if st.checkbox('Show cleaned and merged data'):
        st.subheader(f'**{selection}**')
        st.write(concat_df_to_display)
        
    
def data_description():
    st.subheader('Descriptive statistics')
    
    col1, col2 = st.columns(2)
    with col1:
        select_df = st.selectbox('Select DataFrame', options=['All Columns', 'Numerical Columns', 'Categorical Columns'], on_change=get_all_column)
    with col2:
        pass
    if select_df == 'All Columns':
        github_df = st.session_state['data'].describe(include=['number', 'object', 'category']).T
        sql_df = st.session_state['data0'].describe(include=['number', 'object', 'category']).T
        merged_df = st.session_state['concat_df'].describe(include=['number', 'object', 'category']).T
    if select_df == 'Numerical Columns':
        github_df = st.session_state['data'].describe(include=['number']).T
        sql_df = st.session_state['data0'].describe(include=['number']).T
        merged_df = st.session_state['concat_df'].describe(include=['number']).T
    if select_df == 'Categorical Columns':
        github_df = st.session_state['data'].describe(include=['object', 'category']).T
        sql_df = st.session_state['data0'].describe(include=['object', 'category']).T
        merged_df = st.session_state['concat_df'].describe(include=['object', 'category']).T
    
    if st.checkbox('Show SQL data descriptive statistics'):
        st.subheader(f'**{select_df}**')
        st.write(sql_df)
    
    if st.checkbox('Show GitHub data descriptive statistics'):    
        st.subheader(f'**{select_df}**')
        st.write(github_df)

    if st.checkbox('Show cleaned & merged data descriptive statistics'):
        st.subheader(f'**{select_df}**')
        st.write(merged_df)
        
def data_dict():
    st.subheader('Data Dictionary')

    with st.expander('Click to see data dictionary'):
        st.write("""
 - **customerID**        - Uniquely identify each customer
 - **gender**            - whether a customer is a Male or Female
 - **SeniorCitizen**     - whether customer is >60 years or not (Yes or No)
 - **Partner**           - Whether customer have a partner or not (Yes or No)
 - **Dependents**        - Whether customer have a dependents or not (Yes or No)
 - **tenure**            - How many months customer has been on the network
 - **PhoneService**      - Whether the customer is satisfied with the phone services
 - **MultipleLines**     - Whether the customer is satisfied with the multiple lines service
 - **InternetService**   - Whether the customer is satisfied with the internet service
 - **OnlineSecurity**    - whether the customer is satisfied with the online security service
 - **OnlineBackup**      - Whether the customer is satisfied with the online backup service
 - **DeviceProtection**  - Whether the customer is satisfied with the device protection service
 - **TechSupport**       - Whether the customer is satisfied with the tech support service
 - **StreamingTV**       - Whether the customer is satisfied with the streaming TV service
 - **StreamingMovies**   - Whether the customer is satisfied with the streaming Movies service
 - **Contract**          - Whether the customer opted for month-to-month, one-year and two-years contract with the Telco
 - **PaperlessBilling**  - Whether the customer is satisfied with the Paperless Billing service
 - **PaymentMethod**     - Whether the customer opted for electronic, mailed check, bank transfer and credit card payment methods
 - **MonthlyCharges**    - Monthly customer charges
 - **TotalCharges**      - Yearly customer charges
 - **Churn**             - Whether a customer will stop using the Telco's network or not (Yes and No)
        """)
    
if st.session_state['authentication_status']:
    authenticator.logout(location='sidebar')
    col1, col2 = st.columns(2)
    with col1:
        st.image('resources/imagesdata.jfif', width=300)
    with col2:
        st.write('### :rainbow-background[Telco Customer Churn Data ]🗃')
        st.selectbox('Select DataFrame/Descriptive statistics', options=['Data', 'Statistics'], key='selected_dataframe')
    if st.session_state['selected_dataframe'] == 'Data':
            select_data() 
    elif st.session_state['selected_dataframe'] == 'Statistics':
            data_description()
            
    data_dict()

else:
    st.info('Login to gain access to the app')

            
