import streamlit as st
import pandas as pd
import numpy as np

# Layout Column
st.header('Data Penjualan Rokok')

np.random.seed(100)
df = pd.DataFrame({
  'Tahun': ['2015', '2016', '2017', '2018', '2019'],
  'Filter': np.random.randint(100, 500, 5),
  'Malboro': np.random.randint(100, 500, 5),
  'Sampoerna': np.random.randint(100, 500, 5)
  }, index=[1,2,3,4,5])

col1, col2 = st.columns(2)
with col1:
  st.subheader('Tabel:')
  st.dataframe(df)

with col2:
  st.subheader('Linechart:')
  st.line_chart(df.set_index('Tahun'))