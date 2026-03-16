import streamlit as st
st.title("iris prediction")
import pickle

model=pickle.load(open("model_svm.pkl", "rb"))

sl = st.slider("S1",2.0,10.0)
sw = st.slider("Sw",2.0,10.0)
pl = st.slider("P1",2.0, 10.0)
pw = st.slider("Pw",2.0, 10.0)

if st.button("Predict"):
    prediction = model.predict([[sl, sw, pl, pw]])
