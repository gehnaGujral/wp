import streamlit as st
import pickle

st.subheader("Weather Prediction App..")
pn=st.number_input("Enter precipitation")
maxt=st.number_input("Enter Maximum Temp")
mint=st.number_input("Enter Mainimum Temp")
wind=st.number_input("Enter Wind Speed")
button=st.button("predict")
if button:
    lr=pickle.load(open("wp.pkl","rb"))
    res=lr.predict([[pn,maxt,mint,wind]])[0]
    st.markdown(f"today weather situation,{res}")

