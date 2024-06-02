import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px

st.set_page_config(
    page_title = 'Dashboard Page',
    page_icon = '📊',
    layout = 'wide'
)

st.title('EDA & Dashboard')

@st.cache_data
def load_concat_data():
    concat_df = pd.read_csv('Data/df_churn.csv')
    return concat_df

concat_df = load_concat_data()
st.write(concat_df)


fig = px.histogram(concat_df, x='tenure', nbins=100, title='Distribution of Tenure')

st.plotly_chart(fig)


sns.set(style="ticks")
pairplot = sns.pairplot(concat_df, hue='Churn', height=1.2, aspect=2)

for ax in pairplot.axes.flatten():
    for label in ax.get_xticklabels():
        label.set_rotation(25)
    for label in ax.get_yticklabels():
        label.set_rotation(25)

# Display the plot in Streamlit
st.pyplot(pairplot)

catplot1 = sns.catplot(concat_df, x='gender', y= 'tenure', hue='Churn', kind='violin', palette=['blue', 'red'], height=3, aspect=2 )
st.subheader('How long Female and Male stay with Telco before Churning')
plt.show()
st.pyplot(catplot1)

catplot2 = sns.catplot(concat_df, x='Contract', y= 'tenure', hue='Churn', kind='box', aspect=1, palette=['blue', 'red'])
plt.title('How long does it take each contract type before Churning')
plt.show()
st.pyplot(catplot2)