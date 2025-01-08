import json
import xgboost
import streamlit as st
import pandas as pd
import numpy as np
import os

# Load the JSON file with variable descriptions
with open('variables_info.json') as f:
    variables_info = json.load(f)

# Load the pre-trained XGBoost model
loaded_model = xgboost.Booster()
loaded_model.load_model('xgb_model.bin')

# Page title
st.title('Heart Attack Prediction using ML')

# Sidebar for variable information
st.sidebar.title("Variable Information")

# Function to show information about each variable
def display_variable_info(variable):
    variable_data = variables_info.get(variable, None)
    if variable_data:
        st.sidebar.header(variable_data["full_name"])
        st.sidebar.write(variable_data["description"])
        st.sidebar.write("Possible values:")
        st.sidebar.write(variable_data["possible_values"])

# Initialize session state for focused input tracking
if 'focused_input' not in st.session_state:
    st.session_state['focused_input'] = None

# Input collection and variable info display
st.markdown("### Input patient details:")

# Dictionary to store input values
features_values = {}

# Age
age = st.slider('Enter Age', 1, 120, 30)
features_values['age'] = age
if st.button("Info: Age", key="age_info"):
    st.session_state['focused_input'] = 'age'
    display_variable_info('age')

# Sex
sex = st.selectbox('Enter Sex', ('Male', 'Female'))
sex = 1 if sex == 'Male' else 0
features_values['sex'] = sex
if st.button("Info: Sex", key="sex_info"):
    st.session_state['focused_input'] = 'sex'
    display_variable_info('sex')

# Chest Pain Type
cp = st.selectbox('Enter Chest Pain Type', (0, 1, 2, 3))
features_values['cp'] = cp
if st.button("Info: Chest Pain Type", key="cp_info"):
    st.session_state['focused_input'] = 'cp'
    display_variable_info('cp')

# Resting Blood Pressure
trtbps = st.slider('Enter Resting Blood Pressure (mm Hg)', 90, 200, 120)
features_values['trtbps'] = trtbps
if st.button("Info: Resting BP", key="bp_info"):
    st.session_state['focused_input'] = 'trtbps'
    display_variable_info('trtbps')

# Cholesterol
chol = st.slider('Enter Cholesterol (mg/dl)', 100, 600, 200)
features_values['chol'] = chol
if st.button("Info: Cholesterol", key="chol_info"):
    st.session_state['focused_input'] = 'chol'
    display_variable_info('chol')

# Fasting Blood Sugar
fbs = st.selectbox('Is fasting blood sugar > 120 mg/dl?', ('Yes', 'No'))
fbs = 1 if fbs == 'Yes' else 0
features_values['fbs'] = fbs
if st.button("Info: FBS", key="fbs_info"):
    st.session_state['focused_input'] = 'fbs'
    display_variable_info('fbs')

# Resting ECG
restecg = st.selectbox('Enter Resting ECG Result', (0, 1, 2))
features_values['restecg'] = restecg
if st.button("Info: Resting ECG", key="ecg_info"):
    st.session_state['focused_input'] = 'restecg'
    display_variable_info('restecg')

# Maximum Heart Rate
thalachh = st.slider('Enter Maximum Heart Rate', 50, 220, 150)
features_values['thalachh'] = thalachh
if st.button("Info: Max Heart Rate", key="heart_rate_info"):
    st.session_state['focused_input'] = 'thalachh'
    display_variable_info('thalachh')

# Exercise-induced Angina
exng = st.selectbox('Exercise-induced Angina', ('Yes', 'No'))
exng = 1 if exng == 'Yes' else 0
features_values['exng'] = exng
if st.button("Info: Exercise-induced Angina", key="exng_info"):
    st.session_state['focused_input'] = 'exng'
    display_variable_info('exng')

# Oldpeak
oldpeak = st.slider('Enter Oldpeak value', 0.0, 6.0, 1.0, 0.1)
features_values['oldpeak'] = oldpeak
if st.button("Info: Oldpeak", key="oldpeak_info"):
    st.session_state['focused_input'] = 'oldpeak'
    display_variable_info('oldpeak')

# Slope of Peak Exercise ST Segment
slp = st.selectbox('Enter Slope of Peak Exercise ST Segment', (0, 1, 2))
features_values['slp'] = slp
if st.button("Info: Slope", key="slope_info"):
    st.session_state['focused_input'] = 'slp'
    display_variable_info('slp')

# Coronary Artery Anomaly
caa = st.selectbox('Enter Coronary Artery Anomaly', (0, 1, 2, 3))
features_values['caa'] = caa
if st.button("Info: CAA", key="caa_info"):
    st.session_state['focused_input'] = 'caa'
    display_variable_info('caa')

# Thalassemia
thall = st.selectbox('Enter Thalassemia', (0, 1, 2))
features_values['thall'] = thall
if st.button("Info: Thalassemia", key="thall_info"):
    st.session_state['focused_input'] = 'thall'
    display_variable_info('thall')

# Prediction button
if st.button('Predict'):
    if any(value == 0 or value == 0.00 for value in features_values.values()):
        st.warning('Please input all the details.')
    else:
        # Ensure the input only contains the features the model was trained on
        trained_features = ['thall', 'caa', 'cp', 'oldpeak', 'exng', 'chol', 'thalachh']
        filtered_input = {key: features_values[key] for key in trained_features}

        # Check if the JSON file exists and is properly formatted
        if os.path.exists('new_data.json'):
            try:
                # Load existing data
                with open('new_data.json', 'r') as json_file:
                    data = json.load(json_file)
                # Ensure it's a list
                if not isinstance(data, list):
                    data = []  # Reset if not a list
            except json.JSONDecodeError:
                data = []  # Reset if file contents are invalid
        else:
            data = []  # Initialize a new list if the file doesn't exist

        # Append the new input to the list
        data.append(filtered_input)

        # Save the updated list back to the JSON file
        with open('new_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        # Convert the filtered input to a DataFrame
        input_df = pd.DataFrame([filtered_input])

        # Make prediction
        dtest = xgboost.DMatrix(input_df)
        prediction = loaded_model.predict(dtest)
        threshold = 0.5
        prediction = np.where(prediction >= threshold, 1, 0)

        if prediction == 0:
            st.markdown("<h2 style='text-align: center; color: green;'>Patient has no risk of Heart Attack</h2>", unsafe_allow_html=True)
        else:
            st.markdown("<h2 style='text-align: center; color: red;'>Patient has risk of Heart Attack</h2>", unsafe_allow_html=True)
