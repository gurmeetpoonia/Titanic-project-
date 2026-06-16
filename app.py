import streamlit as st
import numpy as np
import joblib

# load model
model = joblib.load("titanic_model.pkl")

st.title("🚢 Titanic Survival Predictor")

# inputs
pclass = st.selectbox("Pclass", ["Select",1, 2, 3])
sex = st.selectbox("Sex", ["Select","male", "female"])
age = st.number_input("Age",min_value=0, step=1)
fare = st.number_input("Fare")
embarked = st.selectbox("Embarked", ["Select","S", "C", "Q"])

# encoding


# prediction
if st.button("Predict"):
    if age <= 0:
        st.warning("Please enter Age")

    elif fare <= 0:
        st.warning("Please enter Fare")

    elif (
        pclass == "Select" or
        sex == "Select" or
        embarked == "Select" 
    ):
        st.warning("Please fill all dropdown fields")

    else:
        # encoding
        sex = 1 if sex == "female" else 0
    

        embarked = {
            "S": 0,
            "C": 1,
            "Q": 2
        }[embarked]


        input_data = np.array([[pclass, sex, age, fare, embarked]])
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.success("🎉 Survived")
        else:
            st.error("💀 Not Survived")