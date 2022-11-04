import streamlit as st
import pandas as pd
import numpy as np
from collections.abc import Mapping

st.title('Welcome To Churn Prediction')


st.sidebar.header('User Input Parameters')

def user_input_features():
    
    vm = st.sidebar.selectbox("Voice mail plan",("Yes","No"))
    ip = st.sidebar.selectbox("International plan",("Yes","No"))
    
    im = st.sidebar.number_input("Iinternational mins",min_value=0,max_value=25,value=0)
    cs = st.sidebar.number_input("Customer service calls",min_value=0,max_value=10,step=1)
    ic = st.sidebar.number_input("International calls",min_value=0,max_value=20,step=1)
    tc = st.sidebar.number_input("Total Charge",min_value=0,max_value=100,step=0)
    
    new = {
         'voice_mail_plan': vm,
         'international_plan': ip,
         'Iinternational_mins': im,
         'customer_service_calls': cs,
         'international_calls': ic,
         'Total Charge': tc,
            }
    features = pd.DataFrame(new,index = [0])
    return features 


df = user_input_features()
st.write(df)



import pickle

with open(file="Final_model.pkl",mode="rb") as f:
    model = pickle.load(f)
    
st.write("Model loaded")



result = model.predict(df)
st.subheader('Predicted Result')

if result[0]==0:
    st.write("Customer will not Churn")
    
else:
    st.write("Customer will Churn")
