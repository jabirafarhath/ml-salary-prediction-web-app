import streamlit as st
import predict_page
import explore_page



st.sidebar.title('Software Developer Salary Prediction')
page = st.sidebar.selectbox("Select",("Predict","Explore"))
st.sidebar.subheader('About Us')
st.sidebar.write('Software Developer Salary Prediction Web App is a simple machine learning application thats predicts the salary of a software developer based on years of experience. This Machine Learning apllication employs linear regression algorithm to calculate salary. Hope you will like it.')


st.title('Software Developer Salary Prediction')
if page == 'Predict':
    predict_page.show_predict_page()
elif page == 'Explore':
    explore_page.show_explore_page()
