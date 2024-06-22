import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title='Home Page',
    page_icon='',
    layout='wide'
)

def background():
    st.image('resources/brainchart.webp', width=200)
    st.header(":gray-background[Welcome to :rainbow[Telco Customer Churn Prediction App]]")
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

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

name, authentication_status, username = authenticator.login(location = 'sidebar')


if st.session_state['authentication_status']:
    authenticator.logout(location='sidebar')
    if st.sidebar.button('Reset Password'):
            st.session_state['reset_password'] = True
    if st.session_state.get('reset_password'):
        with st.form('reset_password_form'):
            new_password = st.text_input('Enter new password')
            confirm_password = st.text_input('Confirm new password', type='password') 
            if st.form_submit_button('Reset'):
                if new_password == confirm_password:
                    try:
                        if authenticator.reset_password(st.session_state["username"], new_password, location='sidebar'):
                            st.session_state['reset_password'] = False
                            st.success('Password modified successfully')
                    except Exception as e:
                        st.error(e)
                else:
                    st.error('Passwords do not match')
    background()

elif st.session_state['authentication_status'] is False:
    st.info('Invalid Email/Password')

elif st.session_state['authentication_status'] is None:
    st.info('Create an account to get access to the app')
    if st.sidebar.button('Create Password'):
            st.session_state['Create Password'] = True
    if st.session_state.get('Create Password'):
            with st.form('Create account'):
                name = st.text_input('Enter your name')
                username = st.text_input('Enter your username')
                email = st.text_input('Enter your email')
                password = st.text_input('Enter your password', type='password')
                confirm_password = st.text_input('Confirm password', type='password')
                if st.form_submit_button('Register'):
                    if password == confirm_password:
                        try:
                            email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(name, username, email, password, pre_authorization=False, location ='sidebar')
                            if email_of_registered_user:
                                st.success('User registered successfully')
                                st.ballons()
                                st.session_state['Create Password'] = False
                        except Exception as e:
                            st.error(e)
                    else:
                        st.error('Passwords do not match')   


    
    st.code("""
            Test Account
            Username: bamzzyy
            Password: 10101
            """)
    