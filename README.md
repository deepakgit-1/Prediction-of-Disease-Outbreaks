# 🧠 Prediction of Disease Outbreaks

A machine learning-powered web application for predicting the likelihood of three major diseases — **Diabetes**, **Heart Disease**, and **Parkinson's Disease**. Built with **Python**, **Streamlit**, and **scikit-learn**, this system helps users assess their risk based on medical inputs.

---

## 🚀 Features

🔹 **Diabetes Prediction**  
Predict whether an individual is diabetic based on health metrics like:
- Glucose level
- Blood pressure
- BMI
- Age
- Pregnancies
- Insulin, Skin Thickness, etc.

🔹 **Heart Disease Prediction**  
Predict the risk of heart disease using:
- Chest pain type
- Cholesterol level
- Resting blood pressure
- Maximum heart rate
- Age, Thal, etc.

🔹 **Parkinson’s Disease Prediction**  
Predict the likelihood of Parkinson’s disease using voice features:
- Jitter
- Shimmer
- Fo, Fhi, Flo
- RPDE, DFA, NHR, PPE, etc.

---

## 🧰 Tech Stack

| Technology | Description |
|------------|-------------|
| **Python** | Core programming language |
| **Streamlit** | Interactive web app interface |
| **scikit-learn** | Machine learning model training and prediction |
| **Pickle** | Serialization of trained ML models |
| **streamlit-option-menu** | Sidebar navigation for selecting disease prediction |

---
## 📦 Requirements

Ensure Python 3.x is installed. Then, install the required libraries:
pip install streamlit scikit-learn streamlit-option-menu

## 🛠️ How to Run the Application

Clone the repository
git clone https://github.com/deepakgit-1/Prediction-of-Disease-Outbreaks.git

Navigate into the project directory
cd Prediction-of-Disease-Outbreaks

Launch the application
streamlit run app.py

The app will open in your default browser. Use the sidebar to choose a disease, fill out the required form fields, and get instant predictions.

## 🔍 How It Works
- User Interaction: Users input relevant health parameters for one of the three diseases.
- Prediction Model: The app loads a pre-trained machine learning model (stored as .sav files).
- Output: The model predicts whether the user is likely to have the disease, displaying a success message with the result.


## 📄 License
This project is licensed under the MIT License. Feel free to use and adapt for educational or personal use.


