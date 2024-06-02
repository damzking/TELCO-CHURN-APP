import streamlit as st


st.set_page_config(
    page_title = 'Home Page',
    page_icon = '💒',
    layout = 'wide'
)

st.title("Welcome to :violet[Telco Customer Churn Prediction App]")


def app():
    choice = st.selectbox('Login/Sign Up', ['Login', 'Sign Up'])

    if choice == 'Login':
        with st.form("login_form"):
            username = st.text_input('Username')
            password = st.text_input('Password', type='password')
            login_button = st.form_submit_button('Login')

        if login_button:
            st.success(f'Logged in as {username}')
    
    else:
        with st.form("signup_form"):
            username = st.text_input('Username')
            password = st.text_input('Password', type='password')
            email_address = st.text_input('Email Address')
            signup_button = st.form_submit_button('Sign up')

        if signup_button:
            st.success(f'Signed up as {username}')

if __name__ == '__main__':
    app()
