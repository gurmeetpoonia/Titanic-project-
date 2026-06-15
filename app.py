<<<<<<< HEAD
import streamlit as st
import numpy as np
import joblib

# load model
model = joblib.load("titanic_model.pkl")

st.title("🚢 Titanic Survival Predictor")

# inputs
pclass = st.selectbox("Pclass", [1,2,3])
sex = st.selectbox("Sex", ["male","female"])
age = int(st.number_input("Age"))
fare = st.number_input("Fare")
embarked = st.selectbox("Embarked", ["S","C","Q"])

# encoding
sex = 0 if sex == "male" else 1
embarked = {"S":0,"C":1,"Q":2}[embarked]

# prediction
if st.button("Predict"):
    input_data = np.array([[pclass, sex, age, fare, embarked]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("🎉 Survived")
    else:
=======
import streamlit as st
import numpy as np
import joblib

# load model
model = joblib.load("titanic_model.pkl")

st.title("🚢 Titanic Survival Predictor")

# inputs
pclass = st.selectbox("Pclass", [1,2,3])
sex = st.selectbox("Sex", ["male","female"])
age = int(st.number_input("Age"))
fare = st.number_input("Fare")
embarked = st.selectbox("Embarked", ["S","C","Q"])

# encoding
sex = 0 if sex == "male" else 1
embarked = {"S":0,"C":1,"Q":2}[embarked]

# prediction
if st.button("Predict"):
    input_data = np.array([[pclass, sex, age, fare, embarked]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("🎉 Survived")
    else:
>>>>>>> 98ef076f6e063f5d120459537555a30116b3bc7e
        st.error("💀 Not Survived")