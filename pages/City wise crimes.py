import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
# change plotly theme

st.set_page_config(layout='wide')
# function to load the data only once
@st.cache_data()
def load_City_wise_crimes_dataset():
    df = pd.read_csv(r'datasets\total_crimes\IPC_crimes_(City-wise)_2019-2021.csv', index_col='City')
    df['2019'] = df['2019'].replace('-', np.nan)
    df['2019'] = df['2019'].astype(float)
    return df
st.spinner("loading datasets")
df= load_City_wise_crimes_dataset()

if st.sidebar.checkbox("Show states wise crime datasets"):
    st.subheader('📅 States wise crimes data')
    st.dataframe(df, use_container_width=True)


# group by 
st.subheader("Year wise crime in different cities")
state_year_group = df.groupby('City')[['2019','2020','2021']].sum().reset_index()
st.dataframe(state_year_group, use_container_width=True)
fig2 = px.bar(state_year_group, 'City', ['2019','2020','2021'], )
st.plotly_chart(fig2, use_container_width=True)

st.subheader('distribution of crime')
fig3 = px.area(df, df.index, 'Population', title='Population Data')
st.plotly_chart(fig3, use_container_width=True)
fig4 = px.area(df, df.index, 'RateofCognizableCrimes', title='Rate of congnizable Crimes Data')
st.plotly_chart(fig4, use_container_width=True)
fig5 = px.area(df, df.index, 'ChargesSheetingRate', title='Charges Sheeting Rate Data')
st.plotly_chart(fig5, use_container_width=True)
