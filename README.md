# 🚢 Titanic Survival Prediction App

This is a Machine Learning web application built using Streamlit that predicts whether a passenger would have survived the Titanic disaster based on input features such as age, gender, class, and more.

---

## 🚀 Live Demohttps://github.com/gurmeetpoonia/Titanic-project-/edit/main/README.md
👉 https://unxnuvmmjzxu9btybj4zqe.streamlit.app/

---

## 📊 Project Overview
This project demonstrates a complete end-to-end Machine Learning workflow:
- Data preprocessing
- Model training
- Model saving using pickle
- Web deployment using Streamlit

---

## 🧠 Features Used
- Passenger Class (Pclass)
- Gender (Sex)
- Age
- Siblings/Spouses aboard (SibSp)
- Parents/Children aboard (Parch)
- Fare

---

## 🤖 Machine Learning Model
- Algorithm: Logistic Regression / Decision Tree (whatever you used)
- Library: scikit-learn
- Model saved using: `pickle`

---

## 🛠️ Tech Stack
- Python 🐍
- Streamlit
- Pandas
- NumPy
- Scikit-learn

---

## 📁 Project Structure
- app.py
- titanic_model.pkl
- requirements.txt
- README.md

---
## 📌 How It Works
-1. User enters passenger details in UI
-2. Data is processed and encoded
-3.Trained ML model predicts survival
-4.Output is displayed as:
  - . 0 → Not Survived
  - . 1 → Survived
## 🎯 Key Learnings
-. Building ML pipeline from scratch
-. Handling real-world dataset
-. Model serialization using Pickle
-. Web deployment using Streamlit

## 👨‍💻 Author
-Gurmeet Punia
----

## ⚙️ How to Run Locally

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
streamlit run app.py
