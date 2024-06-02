import streamlit as st
import pyodbc
import pandas as pd

st.set_page_config(
    page_title = 'Data Page',
    page_icon = '🗃',
    layout = 'wide'
)

st.title('Telco Customer Churn Data 🗃')



@st.cache_resource(show_spinner='Connecting to database...')
def init_connection():
    connection_string = (
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={st.secrets['server']};"
        f"DATABASE={st.secrets['database']};"
        f"UID={st.secrets['username']};"
        f"PWD={st.secrets['password']}"
    )
    return pyodbc.connect(connection_string)


conn = init_connection()

@st.cache_data(show_spinner= 'running query...')
# Query the database and get a DataFrame
def get_dataframe(query):
    return pd.read_sql(query, conn)

@st.cache_data
def load_data():
    data = pd.read_csv('Data/telco_churn_git.csv')
    return data

@st.cache_data
def load_concat_data():
    concat_df = pd.read_csv('Data/df_churn.csv')
    return concat_df

# Function to get all columns from a specific table
def get_all_column():
    df = get_dataframe("SELECT * FROM dbo.LP2_Telco_churn_first_3000")
    data = pd.read_csv('Data/telco_churn_git.csv')
    concat_df = pd.read_csv('Data/df_churn.csv')
    st.session_state['dataframe'], st.session_state['data'], st.session_state['concat_df'] = df, data, concat_df

# Initialize the dataframe in session state if not already there
if 'dataframe' not in st.session_state and 'data' not in st.session_state and 'concat_df' not in st.session_state:
    get_all_column()


st.subheader('Telco churn data from SQL')
# Dropdown select box
selection = st.selectbox('Select..', options=['All columns', 'Numerical Columns', 'Categorical Columns'], on_change=get_all_column)

# Filter the DataFrame based on the selection
if selection == 'Numerical Columns':
    df_to_display = st.session_state['dataframe'].select_dtypes(include=['number'])
    data_to_display = st.session_state['data'].select_dtypes(include=['number'])
    concat_df_to_display = st.session_state['concat_df'].select_dtypes(include=['number'])
elif selection == 'Categorical Columns':
    df_to_display = st.session_state['dataframe'].select_dtypes(include=['object', 'category'])
    data_to_display = st.session_state['data'].select_dtypes(include=['object', 'category'])
    concat_df_to_display = st.session_state['concat_df'].select_dtypes(include=['object', 'category'])    
else:
    df_to_display = st.session_state['dataframe']
    data_to_display = st.session_state['data']
    concat_df_to_display = st.session_state['concat_df']

# Display the DataFrame
if st.checkbox('Show data from SQL'):
    st.subheader(f'**{selection}**')
    st.write(df_to_display)
    
if st.checkbox('Show data from GitHub'):    
    st.subheader('Telco churn data from GitHub')
    st.subheader(f'**{selection}**')
    st.write(data_to_display)

if st.checkbox('Show cleaned and merged data'):
    st.subheader('Cleaned and merged Telco churn data')
    st.subheader(f'**{selection}**')
    st.write(concat_df_to_display)
    
# Display the data
#if st.checkbox('Show data'):
   # st.subheader('Telco churn data from GitHub')
    #telco_churn_git = load_data()
    #st.write(telco_churn_git)

