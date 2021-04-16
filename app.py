import streamlit as st
import joblib
model=joblib.load("Email_class")
st.title('review classifier')
ip=st.text_input('enter your review')
op=model.predict([ip])
st.title(op[0])
