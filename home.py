import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
# change plotly theme

st.set_page_config(layout='wide')
st.title("Crime Data Analysis")
st.image("images/hero.png", use_column_width=True)
# function to load the data only once
@st.cache_data()
def load_crime_women_children():
    df = pd.read_csv('datasets/state_wise_crime.csv', index_col=0)
    return df
st.spinner("loading datasets")
df= load_crime_women_children()

st.sidebar.header("Navigation")

if st.sidebar.checkbox("Show crime datasets"):
    st.subheader('📅 Raw datasets')
    st.dataframe(df, use_container_width=True)

st.subheader('Analysis of Data')
rows,cols = df.shape
total_Murder = df['Murder'].sum()
deaths = int( rows - total_Murder)
c1, c2, c3 = st.columns(3)
c1.metric('Total Records', rows)    
c2.metric('Total Columns', cols)
c3.metric('Murder', total_Murder, delta=-deaths )
# if we have a dataframe - then we can use column names
# if we have a series - then we use index and values 
st.subheader('distribution of crime')
fig1 = px.area(df, df.index, 'Murder', title='Murder Data')
st.plotly_chart(fig1, use_container_width=True)
fig2 = px.area(df, df.index, 'Assault', title='Assault Data')
st.plotly_chart(fig2, use_container_width=True)
fig3 = px.area(df, df.index, 'Shoplifting', title='Shoplifting Data')
st.plotly_chart(fig3, use_container_width=True)
fig4 = px.area(df, df.index, 'robbery', title='robbery Data')
st.plotly_chart(fig4, use_container_width=True)