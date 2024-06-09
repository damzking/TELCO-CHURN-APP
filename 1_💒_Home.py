import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth


st.set_page_config(
    page_title = 'Home Page',
    page_icon = '💒',
    layout = 'wide'
)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

st.title("Welcome to :violet[Telco Customer Churn Prediction App]")

# Check if the default Firebase app is already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('.streamlit/telco-customer-churn-predict-f7f9ee24bfdc.json')
    firebase_admin.initialize_app(cred)


def app():
    email_address = ''

    def login():
        try:
            display_name = auth.get_user_by_email(email_address)
            #print(display_name.uid)
            st.write('Login Successfully')

        except:
            st.warning('Invalid email or password')

    col1, col2 = st.columns(2)

    with col1:
        st.write('## How to run application')
        st.code('''
        # activate virtual environment
        env/scripts/activate
        streamlit run home.py
        ''')
        st.link_button('Repository on Github', url='https://github.com/Koanim/LP4-Telco-Customer-Churn-Prediction-APP')
        choice = st.selectbox('Login/Sign Up', ['Login', 'Sign Up'], key='unique_selectbox_key')

        if choice == 'Login':
            with st.form("login_form"):
                email_address = st.text_input('Email Address')
                password = st.text_input('Password', type='password')
                login_button = st.form_submit_button('Login', on_click = login)

            if login_button:
                st.success(f'Logged in as {email_address}')
    
        else:
            with st.form("signup_form"):
                username = st.text_input('Username')
                password = st.text_input('Password', type='password')
                email_address = st.text_input('Email Address')
                signup_button = st.form_submit_button('Sign up')

            if signup_button:
                user = auth.create_user(email = email_address, password = password, uid = username)
                st.success(f'Signed up as {username}')
                st.markdown('Please Login using your email and password')
                st.balloons()
                
    with col2:
        #Your additional content goes here
        with  st.container():
            st.write('## :violet[Predict Customer Churn]')
            st.write('### About Us')
            st.write(" This App's aim is to use Machine learning Algorithm to predict whether a new Telco customer will churn or not churn.To understand the dataset and find the lifeline value of each customer and determine which factors affect the rate at which customers stop using their network.")
            
            st.write('### Feedback Form')
            st.write('If you have any feedback, please contact us via telco@churnapp.com.')
app()
