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



# Function to get all columns from a specific table
def get_all_column():
    df = get_dataframe("SELECT * FROM dbo.LP2_Telco_churn_first_3000")
    st.session_state['dataframe'] = df

# Initialize the dataframe in session state if not already there
if 'dataframe' not in st.session_state:
    get_all_column()

# Dropdown select box
selection = st.selectbox('Select..', options=['All columns', 'Numerical Columns', 'Categorical Columns'], on_change=get_all_column)

# Filter the DataFrame based on the selection
if selection == 'Numerical Columns':
    df_to_display = st.session_state['dataframe'].select_dtypes(include=['number'])
elif selection == 'Categorical Columns':
    df_to_display = st.session_state['dataframe'].select_dtypes(include=['object', 'category'])
else:
    df_to_display = st.session_state['dataframe']

# Display the DataFrame
st.write(df_to_display)


