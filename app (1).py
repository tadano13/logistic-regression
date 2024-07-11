import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model
clf = pickle.load(open("cloud_avinash_model.pkl","rb"))

def predict(data):
    clf = pickle.load(open("cloud_avinash_model.pkl","rb"))
    return clf.predict(data)


st.title("Titanic Survival Prediction using Machine Learning")
st.markdown("This Model Identify weather people survived or not")

st.header("Passenger Details")
col1,col2 = st.columns(2)

with col1:
	st.text("Age")
	age = st.slider("Age", 1.0, 100.0, 0.5)
	st.text("fare")
	fare = st.slider("Ticket Fare", 0.0, 10000.0, 0.5)
	st.text("family Size")
	fs = st.slider("Family Size", 1,10,2)
with col2:
	st.text("class 1: First, 2: 2nd,3:3rd")
	pc=st.selectbox("Passenger Class:",[1,2,3])
	st.text("Boarding From 1:Chernourg , 2:Queenstown ,3:Southhampton")
	bc=st.selectbox("Boarding From:",[1,2,3])


st.text('')
if st.button("Predict Survied Or Not "):
    result = clf.predict(
        np.array([[age,fare,fs,pc,bc,1,1,1]]))
    st.text(result[0])

st.markdown("Developed By Avinash Pawar at NIELIT Daman")
