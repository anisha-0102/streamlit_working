import streamlit as st
from client import StockApi


## Create page title 

st.set_page_config(page_title="Stock Market app", layout ="wide")


## add title for page 

st.title("Stock Market app")


## add subheading 

st.subheader("By Anisha Shinde")

## Add box for company 
company = st.text_input("Company Name")