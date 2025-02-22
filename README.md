# Prediction-of-Disease-Outbreaks

This project aims to develop a system that can predict the likelihood of three major diseases (Diabetes, Heart Disease, and Parkinson's Disease) using machine learning models. The system utilizes models trained on relevant datasets to predict whether a person is at risk of contracting these diseases, based on their health parameters.

Features
Diabetes Prediction: Predict whether an individual is diabetic based on health factors like glucose level, blood pressure, BMI, age, and more.
Heart Disease Prediction: Determine if a person is at risk for heart disease by analyzing attributes such as age, chest pain type, blood pressure, cholesterol level, and heart rate.
Parkinson's Disease Prediction: Predict the likelihood of Parkinson's disease based on voice features such as jitter, shimmer, and other speech-related parameters.
Tech Stack
Python: The core language used for developing the application.
Streamlit: Used to create the interactive web-based user interface.
scikit-learn: A machine learning library for building and using predictive models.
Pickle: Used for serializing and saving the trained machine learning models.
streamlit-option-menu: Provides a navigation sidebar menu to switch between different disease prediction sections.
Requirements
Python 3.x
Streamlit
scikit-learn
Pickle
streamlit-option-menu
To install the required libraries, run the following command:

pip install streamlit scikit-learn pickle streamlit-option-menu
How to Run
Clone the repository to your local machine:

git clone https://github.com/deepakgit-1/Prediction-of-Disease-Outbreaks.git

Navigate to the project directory:

cd Prediction-of-Disease-Outbreaks
Run the Streamlit application:

streamlit run app.py
The application will open in your default browser. Use the sidebar to select a disease prediction (Diabetes, Heart Disease, or Parkinson's Disease) and input the required parameters to get the prediction.

How it Works
The user selects a disease prediction model from the sidebar.
They are prompted to input relevant health data into the form fields.
The model processes the inputs and provides a prediction:
Diabetes: Predicts whether the user is diabetic based on factors like age, glucose level, BMI, and others.
Heart Disease: Determines if the user is at risk of heart disease using input data such as chest pain type, cholesterol level, and more.
Parkinson's Disease: Evaluates the likelihood of Parkinson's disease using voice-related features.
The result is displayed to the user with a message indicating whether they are at risk or not.
Models Used
The following machine learning models are used for prediction:

Diabetes Prediction: A model trained on a dataset of diabetes-related attributes.
Heart Disease Prediction: A model trained on a dataset of heart disease-related health metrics.
Parkinson's Disease Prediction: A model trained on voice features to predict Parkinson's disease.
These models are serialized (saved) as .sav files and loaded into the application for prediction.

Future Enhancements
Data Visualization: Adding interactive charts to help users better understand the prediction results.
More Disease Predictions: Integrating models for predicting other diseases.
Model Optimization: Improving the performance of the machine learning models using advanced techniques.
