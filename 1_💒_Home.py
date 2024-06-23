import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

st.set_page_config(
    page_title='Home Page',
    page_icon='',
    layout='wide'
)


col1, col2, col3 = st.columns(3)
with col2:
    st.image('resources/brainchart.webp', width=200)
st.header(":gray-background[Welcome to :rainbow[Telco Customer Churn Prediction App]]")
 
# Check if the default Firebase app is already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('.streamlit/telco-customer-churn-predict-f7f9ee24bfdc.json')
    firebase_admin.initialize_app(cred)
 
#def initialize_session_state():
#    if 'signedout' not in st.session_state:
#        st.session_state.signedout = False
#    if 'signout' not in st.session_state:
#        st.session_state.signout = False
#    if 'username' not in st.session_state:
#        st.session_state.username = ''
#    if 'useremail' not in st.session_state:
#        st.session_state.useremail = ''
 
#def sign_out():
#    st.session_state.signedout = False
#    st.session_state.signout = False
#    st.session_state.username = ''
#    st.session_state.useremail = ''


def initialize_session_state():
    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'sign_in' not in st.session_state:
        st.session_state.sign_in = False
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

def sign_out():
    st.session_state.signedout = False
    st.session_state.sign_in = False
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
        st.link_button('Repository on Github', url='https://github.com/Koanim/LP4-Telco-Customer-Churn-Prediction-APP')
        def sign_in():
            st.session_state.sign_in = True
            login_button = True
            return login_button
        def sign_up():
            st.session_state.sign_up = True
            signup_button = True
            return signup_button
            
        if not st.session_state.signedout:
            col3, col4 = st.columns(2)
            with col3:
                def login_form():
                    email_address = st.text_input('Email Address')
                    password = st.text_input('Password', type='password')
                    st.form_submit_button('Login', on_click=login_button)
            with col4:
                def signup_form():
                    username = st.text_input('Username')
                    password = st.text_input('Password', type='password')
                    email_address = st.text_input('Email Address')
                    st.form_submit_button('Sign Up', on_click=signup_button)
            
                #if login == 'Login':
                    #with st.form("login_form"):
                     #   email_address = st.text_input('Email Address')
                     #   password = st.text_input('Password', type='password')
                     #   login_button = st.form_submit_button('Login')
 
                def login_button():
                    try:
                        user = auth.get_user_by_email(email_address)
                        st.write('Login Successfully')
                        st.session_state.username = user.uid
                        st.session_state.useremail = user.email
                        st.session_state.signedout = True
                        st.session_state.sign_in = True
                    except Exception as e:
                        if st.session_state.useremail != user.email:
                            st.warning('Invalid email')
                        else:
                            st.warning('Invalid password')
 
                #if signup == 'SignUp':
                 #   with st.form("signup_form"):
                  #      username = st.text_input('Username')
                   #     password = st.text_input('Password', type='password')
                    #    email_address = st.text_input('Email Address')
                     #   signup_button = st.form_submit_button('SignUp')

                def signup_button():
                    try:
                        user = auth.create_user(email=email_address, password=password, uid=username)
                        st.success(f'Signed up as {username}')
                        st.markdown('Please Login using your email and password')
                        st.balloons()
                    except Exception as e:
                        st.warning('Please enter a valid email address')
                        
        else:
            st.text('Name: ' + st.session_state.username)
            st.text('Email Id: ' + st.session_state.useremail)
            st.button('Sign out', on_click=sign_out)
            st.write("### You are signed Out!")
            st.write("Now you can use the app to predict customer churn.")

    with col2:
        with st.container():
            st.write('## :violet[Predict Customer Churn]')
            st.write('### About Us')
            st.write("This App's aim is to use Machine learning Algorithm to predict whether a new Telco customer will churn or not churn. To understand the dataset and find the lifeline value of each customer and determine which factors affect the rate at which customers stop using their network.")
            st.write('### Feedback Form')
            st.write('If you have any feedback, please contact us via telco@churnapp.com.')


def background():
    with st.container():
        st.write('### :rainbow[Telco Customer Churn Overview]')
        
        st.write("""In the 2022 State of Customer Churn in Telecom survey, it was found that customer loyalty to telecom providers is down 22% post-pandemic, with customer stickiness being impacted more by the customer experience than ever. 
        Further, customers are now more price sensitive, with 58% perceiving telco offerings as expensive.
        [Source](https://techsee.com/resources/reports/state-of-customer-churn-telecom-survey-report/)""")

        st.markdown("""  Some reasons for churn in telecoms
        It emerged that churn in the telecom industry is most often due to high customer effort. Customers canceled their contracts for the following reasons:""")

        st.write("""    
            1. Companies wasted their time (37% waited too long to have their issue resolved)
            2. They had to call more than once (51%)
            3. Untrained or incompetent agents (37% thought the reps were rude or had a negative approach)
            4. Inferior self-service options (14%).
            [Source](https://techsee.com/resources/reports/state-of-customer-churn-telecom-survey-report/)

            Machine learning can be a powerful tool for telcos to predict customer churn and keep their customer base. ML is used across many industries, and its application in the telecommunications industry is no different. Machine learning is one way of achieving artificial intelligence.
            [Source](https://www.akkio.com/beginners-guide-to-machine-learning?utm_source=Akkio&utm_medium=content-marketing&utm_content=telecom-customer-churn)
            """)
    with st.container():
        st.write('### :rainbow[Project Objectives]')
        st.write("""
                
- In this project, task is to develop a Classification Machine learning model to predict whether a new Telco customer will churn or not churn.
- To understand the dataset and find the lifeline value of each cutomer and determine which factors affect the rate at which customers stop using their network.
                """)
    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            st.write("#### :rainbow[ANALYTICAL QUESTIONS]")
            st.write("""
                    The following analytical questions will help us gain insight and as well as confirm our hypothesis

1. How long Female and Male spent with Telco before Churning

2. What is the trend between Contract and churn

3. How long does it take each contract type before Churning

3. Which method of payment was prefered among the Senior Citizens and how much in total did both senior and non Senior citizens paid before churning

4. What is the churn trend for gender and dependents as well as their tenure

5. what is the trend between payment methods and gender and how it affect churning

6. What is the trend between tenure and paperlessBilling in relation to churn

7. What is the trend between tenure, Internet Service and senior citizen in relation to churn

8. What is the trend between StreamingMovies and senior citizen in relation to churn

9. How does internetService and OnlineSecurity affect churn

10. What is the trend between Contract and Payment Method in relation to churn
                """)
    with col2:
        st.write("#### :rainbow[HYPOTHESIS]")
        st.write("""
        The following hypothesis will be tested

1.  The average number of churn for Female customers is greater than or equal to that of Male customers.

2.  The average amount of TotalCharges for customers that churn is greater than or equal to those that did not churn.

3.  The average number of tenure for customers that churn is less than or equal to those that did not churn

4.  The average number of churn for customers that have Month_to_month contract is greater than or equal to those with 'One year' contract.

5.  The average number of churn for customers that have Yes value for streamingTV is less than or equal to those with No values.

6.  The average number of customers with dependents that will churn is greater than or equal to that of customers with no dependents.

7.  The average number of churn for customers that have **Yes** values for **seniorCitizen** is greater than or equal to those with **No** values.
                """)

#col1, col2, col3 = st.columns(3)

if __name__ == "__main__":
    app()
    
    background()
