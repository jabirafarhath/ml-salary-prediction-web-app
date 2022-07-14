import streamlit as st
import pandas as pd
import matplotlib as plt

df = pd.read_csv('Salary_Data.csv')


def show_explore_page():
    st.subheader('Explore')
    st.line_chart(df)