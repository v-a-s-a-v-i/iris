import streamlit as st
import joblib
model = joblib.load('iris')
st.slider('IRIS CLASSIFIER')
ip = st.text_input('enter the message')
op = model.predict([ip])
if st.button('Predict'):
  st.slider(op[0])
        
