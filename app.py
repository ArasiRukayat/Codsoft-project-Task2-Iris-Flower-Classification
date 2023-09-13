import streamlit as st
import pandas as pd
import  numpy as np
import pickle 
import sklearn

pickle_in = open('LogisticRegression.pkl','rb')
model = pickle.load(pickle_in)

st.title("IRIS Flower Classification")

### inputting variables
sepal_length = st.number_input("sepal_length")
sepal_width   =st.number_input("sepal_width")
petal_length  =st.number_input("petal_length")
petal_width   =st.number_input("petal_width")
button= st.button("predict")
# Convert prediction to a human-readable response
if button:
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    if prediction == 0:
        st.write("The Species is Iris-setosa Flower")
    elif prediction ==1:
        st.write("The Species is Iris-versicolor Flower")
    else:
        st.write("The species is Iris-versicolor Flower")
    