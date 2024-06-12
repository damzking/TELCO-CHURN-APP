import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

st.set_page_config(
    page_title='Home Page',
    page_icon='',
    layout='wide'
)

 
st.title("Welcome to :violet[Telco Customer Churn Prediction App]")
 
# Check if the default Firebase app is already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('.streamlit/telco-customer-churn-predict-f7f9ee24bfdc.json')
    firebase_admin.initialize_app(cred)
 
def initialize_session_state():
    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
 
def sign_out():
    st.session_state.signedout = False
    st.session_state.signout = False
    st.session_state.username = ''
    st.session_state.useremail = ''
 
#if not firebase_admin._apps:
    #cred = credentials.Certificate('.streamlit/telco-customer-churn-predict-f7f9ee24bfdc.json')
    #firebase_admin.initialize_app(cred)

def initialize_session_state():
    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

def sign_out():
    st.session_state.signedout = False
    st.session_state.signout = False
    st.session_state.username = ''
    st.session_state.useremail = ''

def app():
    initialize_session_state()
 
    col1, col2 = st.columns(2)
 
    with col1:
        st.write('## How to run application')
        st.code('''
        # activate virtual environment
        env/scripts/activate
        streamlit run home.py
        ''')
        st.link_button('Repository on Github', url= 'https://github.com/Koanim/LP4-Telco-Customer-Churn-Prediction-APP')
 
        if not st.session_state.signedout:
            choice = st.selectbox('Login/Sign Up', ['Login', 'Sign Up'], key='unique_selectbox_keys')
 
            if choice == 'Login':
                with st.form("login_form"):
                    email_address = st.text_input('Email Address')
                    password = st.text_input('Password', type='password')
                    login_button = st.form_submit_button('Login')
 
                if login_button:
                    try:
                        user = auth.get_user_by_email(email_address)
                        st.write('Login Successfully')
                        st.session_state.username = user.uid
                        st.session_state.useremail = user.email
                        st.session_state.signedout = True
                        st.session_state.signout = True
                    except:
                        st.warning('Invalid email or password')
                        
 
            elif choice == 'Sign Up':
                with st.form("signup_form"):
                    username = st.text_input('Username')
                    password = st.text_input('Password', type='password')
                    email_address = st.text_input('Email Address')
                    signup_button = st.form_submit_button('Sign up')
 
                if signup_button:
                    try:
                        user = auth.create_user(email=email_address, password=password, uid=username)
                        st.success(f'Signed up as {username}')
                        st.markdown('Please Login using your email and password')
                        st.balloons()
                    except:
                        st.warning('Invalid email or password')
                        
        else:
            st.text('Name: ' + st.session_state.username)
            st.text('Email Id: ' + st.session_state.useremail)
            st.button('Sign out', on_click=sign_out)
            st.write("### You are signed in!")
            st.write("Now you can use the app to predict customer churn.")
 
 
 
    with col2:
        with st.container():
            st.write('## :violet[Predict Customer Churn]')
            st.write('### About Us')
            st.write("This App's aim is to use Machine learning Algorithm to predict whether a new Telco customer will churn or not churn. To understand the dataset and find the lifeline value of each customer and determine which factors affect the rate at which customers stop using their network.")
            st.write('### Feedback Form')
            st.write('If you have any feedback, please contact us via telco@churnapp.com.')
 
 





#st.title("Welcome to :violet[Telco Customer Churn Prediction App]")


st.header('General Telecommunication Customer Churn Overview')

st.write("""In the 2022 State of Customer Churn in Telecom survey, it was found that customer loyalty to telecom providers is down 22% post-pandemic, with customer stickiness being impacted more by the customer experience than ever. 
        Further, customers are now more price sensitive, with 58% perceiving telco offerings as expensive.
        [Source](https://www.akkio.com/beginners-guide-to-machine-learning?utm_source=Akkio&utm_medium=content-marketing&utm_content=telecom-customer-churn)""")

st.markdown("""  Some reasons for churn in telecoms
        It emerged that churn in the telecom industry is most often due to high customer effort. Customers canceled their contracts for the following reasons:

        - Companies wasted their time (37% waited too long to have their issue resolved)
        - They had to call more than once (51%)
        - Untrained or incompetent agents (37% thought the reps were rude or had a negative approach)
        - Inferior self-service options (14%).
        [Source](https://techsee.me/resources/reports/2019-telecom-churn-survey/#:~:text=Primary%20reasons%20for%20churn%20in,more%20than%20once%20(51%25))

        Machine learning can be a powerful tool for telcos to predict customer churn and keep their customer base. ML is used across many industries, and its application in the telecommunications industry is no different. Machine learning is one way of achieving artificial intelligence.
        [Source](https://www.akkio.com/beginners-guide-to-machine-learning?utm_source=Akkio&utm_medium=content-marketing&utm_content=telecom-customer-churn)""")

col1, col2, col3 = st.columns(3)

if __name__ == "__main__":
    app()
 


#with col1:
 #   st.header( )
 #   st.write()

# Check if the default Firebase app is already initialized
#if not firebase_admin._apps:
#    cred = credentials.Certificate('.streamlit/telco-customer-churn-predict-f7f9ee24bfdc.json')
#    firebase_admin.initialize_app(cred)


#def app():
 #   email_address = ''

#    def login():
#        try:
#            display_name = auth.get_user_by_email(email_address)
            #print(display_name.uid)
#            st.write('Login Successfully')

#        except:
#            st.warning('Invalid email or password')

#    col1, col2 = st.columns(2)

 #   with col1:
 #       st.write('## How to run application')
 #       st.code('''
        # activate virtual environment
  #      env/scripts/activate
  #      streamlit run home.py
  #      ''')
 #       st.link_button('Repository on Github', url='https://github.com/Koanim/LP4-Telco-Customer-Churn-Prediction-APP')
 #       choice = st.selectbox('Login/Sign Up', ['Login', 'Sign Up'], key='unique_selectbox_key')

 #       if choice == 'Login':
 #           with st.form("login_form"):
 #               email_address = st.text_input('Email Address')
 #               password = st.text_input('Password', type='password')
 #               login_button = st.form_submit_button('Login', on_click = login)

 #           if login_button:
#                st.success(f'Logged in as {email_address}')
    
 #       else:
 #           with st.form("signup_form"):
 #               username = st.text_input('Username')
#                password = st.text_input('Password', type='password')
 #               email_address = st.text_input('Email Address')
  #              signup_button = st.form_submit_button('Sign up')
#
 #           if signup_button:
  #              user = auth.create_user(email = email_address, password = password, uid = username)
 #               st.success(f'Signed up as {username}')
 #               st.markdown('Please Login using your email and password')
 #               st.balloons()
                
 #   with col2:
        #Your additional content goes here
 #       with  st.container():
  #          st.write('## :violet[Predict Customer Churn]')
  #          st.write('### About Us')
 #           st.write(" This App's aim is to use Machine learning Algorithm to predict whether a new Telco customer will churn or not churn.To understand the dataset and find the lifeline value of each customer and determine which factors affect the rate at which customers stop using their network.")
            
 #           st.write('### Feedback Form')
 #           st.write('If you have any feedback, please contact us via telco@churnapp.com.')
#app()
