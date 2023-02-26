import streamlit as st
import pandas as pd
import numpy as np

# create random dataframe
np.random.seed(0)
year = range(2015, 2023)
sales = np.random.randint(10000, 30000, len(year))
df = pd.DataFrame({'Year': year,'Sales': sales});

st.header("Sales-Data")

# convert dataframe 'Year' to datetime format
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df = df.set_index('Year')
df.index = df.index.strftime('%Y')

# showing dataframe
st.write("Data Table:")
st.dataframe(df, width=400)
st.write("Line Chart:")
st.line_chart(df)