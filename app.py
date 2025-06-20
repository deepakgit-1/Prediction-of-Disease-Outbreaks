import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon='doctor')
diabetes_model = pickle.load(open(r"C:\Users\deepak\Desktop\Disease Outbreaks\training_models\diabetes_model.sav",'rb'))
heart_model = pickle.load(open(r"C:\Users\deepak\Desktop\Disease Outbreaks\training_models\heart_model.sav",'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\deepak\Desktop\Disease Outbreaks\training_models\parkinsons_model.sav",'rb'))
with st.sidebar:
    selected = option_menu('Prediction of Disesse outbreak System',
                           ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                           menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)
    
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using Ml')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        Bloodpressure = st.text_input('Blood Pessure value')
    with col1:
        skinThickness = st.text_input('Skin thickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis  = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, Bloodpressure, skinThickness, Insulin, 
                  BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
          diab_diagnosis = 'The Person is Diabetic'
        else:
          diab_diagnosis = 'The Person is Not Diabetic'
    st.success(diab_diagnosis)


if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using Ml')
    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('sex')
    with col3:
        cp = st.text_input('chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographi results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal:0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis  = ''
    if st.button('Heart Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_model.predict([user_input])
        if heart_prediction[0] == 1:
          heart_diagnosis = 'The Person is Suffer From heart Disease'
        else:
          heart_diagnosis = 'The Person is not Suffer From heart Disease'
    st.success(heart_diagnosis)



if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Disease Prediction using Ml')
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        MDVP = st.text_input('MDVP Fo(Hz)')
    with col2:
        MDVP = st.text_input('MDVP Fhi(Hz)')
    with col3:
        MDVP = st.text_input('MDVP Flo(Hz)')
    with col4:
        MDVP = st.text_input('MDVP Jitter(%)')
    with col5:
        MDVP = st.text_input('MDVP Jitter(Abs)')
    with col1:
        MDVP = st.text_input('MDVP:RAP')
    with col2:
        MDVP = st.text_input('MDVP:PPQ')
    with col3:
        Jitter = st.text_input('Jitter:DDP')
    with col4:
        MDVP = st.text_input('MDVP:Shimmer')
    with col5:
        MDVP = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        Shimmer = st.text_input('Shimmer:APQ3')
    with col2:
        Shimmer = st.text_input('Shimmer:APQ5')
    with col3:
        MDVP = st.text_input('MDVP:APQ')
    with col4:
        Shimmer = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis  = ''
    if st.button('Pakinsons Test Result'):
        user_input = [MDVP,MDVP,MDVP,MDVP,MDVP,MDVP,MDVP,Jitter,MDVP,MDVP,Shimmer,
                  Shimmer,MDVP,Shimmer,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        if parkinsons_prediction[0] == 1:
           parkinsons_diagnosis = 'The person is diagnosed with Parkinsons disease'
        else:
           parkinsons_diagnosis = 'The person is not diagnosed with Parkinsons disease'
    st.success(parkinsons_diagnosis)




