import streamlit as st
import pandas as pd
import numpy as np

# Bar-chart
np.random.seed(100)
df = pd.DataFrame({
  'Tahun': ['2015', '2016', '2017', '2018', '2019'],
  'Filter': np.random.randint(100, 500, 5),
  'Malboro': np.random.randint(100, 500, 5),
  'Sampoerna': np.random.randint(100, 500, 5)
  })

st.write('Data Penjualan Rokok:')
st.bar_chart(df.set_index('Tahun'))