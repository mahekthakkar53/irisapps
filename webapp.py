import streamlit as st
st.title("iris prediction")
import pickle

model=pickle.load(open("model_svm.pkl", "rb"))

sl = st.slider("Sepal Length", 2.0, 10.0)
sw = st.slider("Sepal Width", 2.0, 10.0)
pl = st.slider("Petal Length", 2.0, 10.0)
pw = st.slider("Petal Width", 2.0, 10.0)

if st.button("Predict"):
    prediction = model.predict([[sl, sw, pl, pw]])
    st.success(prediction)
