import pandas as pd
import streamlit as st
st.title("Yield Risk Comparison")
products = pd.read_csv("data/products_snapshot.csv")
st.dataframe(products)