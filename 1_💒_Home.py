import streamlit as st


st.set_page_config(
    page_title = 'Home Page',
    page_icon = '💒',
    layout = 'wide'
)

st.title("Welcome to :violet[Telco Customer Churn Prediction App]")


def app():
    def login():
        try:
            display_name = auth.get_user_by_email(email)
            st.write('Login Successfully')

        except:
            st.warning('Invalid email or password')
   

    col1, col2 = st.columns(2)
    with col2:
        # Your additional content goes here
        st.write("Column 1 content")

    with col1:
        st.write('## How to run application')
        st.code('''
        # activate virtual environment
        env/scripts/activate
        streamlit run home.py
        ''')
        st.link_button('Repository on Github', url='https://github.com/Koanim/LP4-Telco-Customer-Churn-Prediction-APP/blob/dev/1_%F0%9F%92%92_Home.py')
        choice = st.selectbox('Login/Sign Up', ['Login', 'Sign Up'], key='unique_selectbox_key')
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
