import streamlit as st
import numpy as np
import pandas as pd
import joblib

model = joblib.load(r'NBpipe.joblib')
columns = ['ur_specific_gravity', 'ur_albumin', 'blood glucose random',
           'serum creatinine', 'hemoglobin', 'packed cell volume',
           'red blood cell count', 'hypertension', 'diabetes']

st.title('Do you have chronic kidney disease? 🩸🩺')
specific_gravity = st.text_input("Specific Gravity")
albumin = st.text_input("Albumin")
blood_glucose = st.text_input("Blood Glucose")
serum_creatinine = st.text_input("Serum Creatinine")
hemoglobin = st.text_input("Hemoglobin")
packed_cell_volume = st.text_input("Packed Cell Volume")
red_blood_cell_count = st.text_input("Red Blood Cell Count")
hypertension = st.select_slider("Do you have hypertension ?", ['Yes', 'No'])
diabetes = st.select_slider("Do you have diabetes ?", ['Yes', 'No'])


def predict():
    if len(specific_gravity) > 0 and len(albumin) > 0\
            and len(blood_glucose) > 0 and len(serum_creatinine) > 0\
            and len(hemoglobin) > 0 and len(packed_cell_volume) > 0\
            and len(red_blood_cell_count) > 0 and len(hypertension) > 0 and len(diabetes) > 0:
        htn, dia = int, int
        if hypertension == 'Yes':
            htn = 1
        elif hypertension == 'No':
            htn = 0
        if diabetes == 'Yes':
            dia = 1
        elif diabetes == 'No':
            dia = 0
        row = np.array([specific_gravity, albumin, blood_glucose,
                        serum_creatinine, hemoglobin, packed_cell_volume,
                        red_blood_cell_count, htn, dia])
        X = pd.DataFrame([row], columns=columns)
        prediction = model.predict(X)
        if prediction[0] == 1:
            st.success('You have Chronic Kidney Disease 🤗 ')
        else:
            st.error('You don\'t have Chronic Kidney Disease 😔 ')
    else:
        st.warning('Make sure to fill all the fields', icon="⚠️")


trigger = st.button('Predict', on_click=predict)
