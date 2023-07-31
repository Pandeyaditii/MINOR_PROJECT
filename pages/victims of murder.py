import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
# change plotly theme

st.set_page_config(layout='wide')
# function to load the data only once
@st.cache_data()
def load_Victims_of_murder_dataset():
    df = pd.read_csv(r'datasets\murder_cases\victims_of_murder_(Gender_Age_Group-wise)_2021.csv', index_col='Name')
    # df['2019'] = df['2019'].replace('-', np.nan)
    # df['2019'] = df['2019'].astype(float)
    return df
st.spinner("loading datasets")
df= load_Victims_of_murder_dataset()

if st.sidebar.checkbox("Show victims of murder datasets"):
    st.subheader('📅 Victims of murder data')
    st.dataframe(df, use_container_width=True)


# group by 
state_year_group = df.groupby('Name')[['Male','Female','Trans','Total']].sum().reset_index()
st.dataframe(state_year_group, use_container_width=True)
fig2 = px.bar(state_year_group, 'Name', ['Male','Female','Trans'])
st.plotly_chart(fig2, use_container_width=True)
fig2a = px.funnel_area(state_year_group, 'Name', 'Total')
st.plotly_chart(fig2a, use_container_width=True)
