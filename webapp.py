import streamlit as st
import pickle
import os

st.title("Iris Prediction")

# Get correct file path
model_path = os.path.join(os.path.dirname(__file__), "model_svm.pkl")

# Load model safely
with open(model_path, "rb") as file:
    model = pickle.load(file)

sl = st.slider("Sepal Length", 2.0, 10.0)
sw = st.slider("Sepal Width", 2.0, 10.0)
pl = st.slider("Petal Length", 2.0, 10.0)
pw = st.slider("Petal Width", 2.0, 10.0)

if st.button("Predict"):

    prediction = model.predict([[sl, sw, pl, pw]])

    if prediction[0] == 0:
        st.success("Setosa")
    elif prediction[0] == 1:
        st.success("Versicolor")
    else:
        st.success("Virginica")
