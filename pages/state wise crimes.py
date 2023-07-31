import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
# change plotly theme

st.set_page_config(layout='wide')
# function to load the data only once
@st.cache_data()
def load_Sates_wise_crimes_dataset():
    df = pd.read_csv(r'datasets\total_crimes\IPC_crimes_(State-UT-wise)_2019-2021.csv', index_col='Name')
    df['2019'] = df['2019'].replace('-', np.nan)
    df['2019'] = df['2019'].astype(float)
    return df
st.spinner("loading datasets")
df= load_Sates_wise_crimes_dataset()

if st.sidebar.checkbox("Show states wise crime datasets"):
    st.subheader('📅 States wise crimes data')
    st.dataframe(df, use_container_width=True)

# group by 
state_year_group = df.groupby('State/UT')[['2019','2020','2021']].sum().reset_index()
st.dataframe(state_year_group, use_container_width=True)
fig2 = px.bar(state_year_group, 'State/UT', ['2019','2020','2021'], )
st.plotly_chart(fig2, use_container_width=True)

st.subheader('distribution of crime')
fig3 = px.area(df, df.index, 'midPopulation', title='Mid Population Data')
st.plotly_chart(fig3, use_container_width=True)
fig4 = px.area(df, df.index, 'RateofCognizableCrimes', title='Rate of congnizable Crimes Data')
st.plotly_chart(fig4, use_container_width=True)
fig5 = px.area(df, df.index, 'ChargesSheetingRate', title='Charges Sheeting Rate Data')
st.plotly_chart(fig5, use_container_width=True)

# group by 
st.subheader('Important Observation and visualization')
state_year_group = df.groupby('State/UT')[['midPopulation','RateofCognizableCrimes','ChargesSheetingRate']].sum().reset_index()
fig6a = px.pie(state_year_group, 'State/UT', 'midPopulation' )
fig6b = px.pie(state_year_group, 'State/UT', 'RateofCognizableCrimes' )
fig6c = px.pie(state_year_group, 'State/UT', 'ChargesSheetingRate' )
c1,c2,c3 = st.columns(3)
c1.plotly_chart(fig6a, use_container_width=True)
c2.plotly_chart(fig6b, use_container_width=True)
c3.plotly_chart(fig6c, use_container_width=True)
st.dataframe(state_year_group, use_container_width=True)

