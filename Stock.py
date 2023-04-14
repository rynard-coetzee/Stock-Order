from pathlib import Path  # Python Standard Library

import pandas as pd  # pip install pandas
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Stock Order",
                   page_icon=":bar_chart:",
)

df = pd.read_excel(
    io='Stock Order Form.xlsm',
    engine='openpyxl',
    sheet_name='Sheet1',
    skiprows=0,
    usecols='D',
    nrows=100,
  )
  
st.write(df)

st.sidebar.header("Select Product/Quantity Here:")
product = st.sidebar.selectbox(
        "Select the Product:",
        options=df["Column1"].unique(),
)
quantity = st.sidebar.text_input(
        "Enter the Amount:")

  
print(df)
    
