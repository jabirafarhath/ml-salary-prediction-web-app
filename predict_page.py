import streamlit as st
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

def load_model():
    reload_model = pickle.load(open('linear_model.pkl','rb')) 
    return reload_model

data = load_model()

model = data['model']
yrs = data['yrs']


def show_predict_page():
    st.subheader("Salary Prediction")
    years = st.slider("Years of Experience",0,50)
    ok = st.button("Calculate salary")
    if ok:
        x = np.array([[years]])
        salary = model.predict(x)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")
   
