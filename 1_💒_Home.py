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
    st.header(":gray-background[Welcome to :rainbow[Telco Customer Churn Prediction App]]")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.caption('My First Machine Learning App 🎉')
    with col2:
        st.image('resources/brainchart.webp', width=200)
    with col3:
        pass
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            with st.container():
                st.write('#### About App')
                st.caption(
                    "This APP will help a Telco determine whether an existing customer or a new customer is likely to churn, based on customer response,\
                    using three different trained Machine learning Model pipelines, these pipelines include :orange[**XGBoost, Category boosting and Gradient boosting**].")
                st.caption("\nThis will help the Telco understand the lifeline value of each customer and determine which factors affect the rate at which customers will stop using their network.")
                st.caption("\nA History of this App will store all predictions made, this data can be used later to determine whether and which of the models is predicting well, for future improvement"
                        )
                st.write("""#### Key Features of App """)
                #st.caption(":violet[Data page] - ")
                with st.expander(":violet[**Data Page**] -"):
                    st.caption('This page contains the datasets used to train our machine learning models, as well as the statistics, the Datasets were acquired from SQL server and a GitHub repository, they were cleaned and merged before modeling ')
                with st.expander(":violet[**Dashboard Page**] -"):
                    st.caption('The dashboard page is made of two visualizations types')
                    st.caption('EDA (Exploratory Data Analysis) Visualizations helps to understand characteristics of the various variables in the datasets, this also will help us understand the distribution of the datasets')
                    st.caption('KPI - these visualizations helps us answer some specific questions, especially in relation to the target variable, in this case :red[Churn]. This help understand how other variables affect :red[Churn]')
                with st.expander(":violet[**Predict Page**] -"):
                    st.caption('The predict page takes responses based on following variables :orange[gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges], then you can select which model you prefer to run your prediction ')
                with st.expander(':violet[**History page**]'):
                    st.caption('This page keeps the records of all predictions made by this app, these data will be valuable to determine if our models needs improvement, as well as understand which model is predicting more accurately')
                
                st.write("""#### Contact Me 📧""")
                st.caption(""" 
                        - For Help with this app
                        - For Collaboration on a different project
                        - For feedback and Enquiry
                        
                        email me via victor.nyarko@ymail.com
                        """)
                st.caption('For more information about me, checkout my!')
                st.write(':red[[GitHub](https://github.com/Koanim/LP4-Telco-Customer-Churn-Prediction-APP), [LinkdIn](https://www.linkedin.com/in/victor-anim-83115818/), [Medium]()] pages')
                
        with col2:                    
            st.write('#### :rainbow[ Telco Churn Overview]')
        
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
            
            col1, col2 = st.columns(2)
            with col1:
                with st.container():
                    with st.expander("###### :rainbow[ANALYTICAL QUESTIONS]"):
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
                with st.expander("###### :rainbow[HYPOTHETICAL QUESTIONS]"):
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
    st.sidebar.write(f'welcome {username}')
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
                    st.error('Passwords do not match 😕')
    background()

elif st.session_state['authentication_status'] is False:
    st.info('Invalid Email/Password 😕')

elif st.session_state['authentication_status'] is None:
    st.info('Please use test account below to get access to the app')
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
                        st.error('😕 Password incorrect')   


    
    st.code("""
            Test Account
            Username: guser
            Password: guestuser
            """)
    