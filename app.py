import streamlit as st
import pickle
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np

# Load Preprocessor
with open('preprocessor (1).pkl', 'rb') as f:
    preprocessor = pickle.load(f)

# Load Model
model = load_model('architecture (1).keras')

# Load Dataset
df = pd.read_csv('genz_college_admission_prediction.csv')

st.set_page_config(page_title="College Admission Prediction", page_icon="🎓")

st.title("🎓 GenZ College Admission Prediction")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age",min_value=int(df['age'].min()),max_value=int(df['age'].max()),value=int(df['age'].mean()))
    
    gender = st.selectbox("Gender",df['gender'].unique())
    
    state = st.selectbox("State",sorted(df['state'].unique()))
    
    family_income = st.number_input( "Family Income",min_value=0.0,value=float(df['family_income'].median()))
    
    high_school_gpa = st.number_input("High School GPA",min_value=0.0,max_value=4.0,value=3.0)
    
    sat_score = st.number_input("SAT Score",min_value=400,max_value=1600,value=1000)
    
with col2:

    act_score = st.number_input("ACT Score",min_value=1,max_value=36,value=20)

    attendance_rate = st.slider( "Attendance Rate (%)", 0, 100,90)

    ap_courses = st.number_input( "AP Courses",min_value=0,value=2)

    extracurricular_count = st.number_input("Extracurricular Activities",min_value=0,value=2)

    volunteer_hours = st.number_input("Volunteer Hours",min_value=0,value=20)

    leadership_positions = st.number_input("Leadership Positions",min_value=0,value=1)
    
with col3:    

    coding_projects = st.number_input("Coding Projects",min_value=0,value=2)

    social_media_hours = st.number_input("Social Media Hours Per Day",min_value=0.0,value=3.0)

    online_certifications = st.number_input("Online Certifications",min_value=0,value=2)

    essay_score = st.slider( "Essay Score",0,100,75)

    recommendation_score = st.slider("Recommendation Score",0,100,80)

    interview_score = st.slider("Interview Score",0,100,80)

# Create DataFrame
data = pd.DataFrame({
    'age': [age],
    'gender': [gender],
    'state': [state],
    'family_income': [family_income],
    'high_school_gpa': [high_school_gpa],
    'sat_score': [sat_score],
    'act_score': [act_score],
    'attendance_rate': [attendance_rate],
    'ap_courses': [ap_courses],
    'extracurricular_count': [extracurricular_count],
    'volunteer_hours': [volunteer_hours],
    'leadership_positions': [leadership_positions],
    'coding_projects': [coding_projects],
    'social_media_hours': [social_media_hours],
    'online_certifications': [online_certifications],
    'essay_score': [essay_score],
    'recommendation_score': [recommendation_score],
    'interview_score': [interview_score]
})

# Convert categorical columns
data['gender'] = data['gender'].astype(object)
data['state'] = data['state'].astype(object)

# Prediction
if st.button("Predict Admission"):

    preprocessed_data = preprocessor.transform(data)

    probability = model.predict(preprocessed_data)

    prediction = np.where(probability > 0.5, 1, 0)

    st.subheader("Prediction Result")

    if prediction[0][0] == 1:
        st.success("🎉 Congratulations! Student is likely to be ADMITTED.")
    else:
        st.error(" Student is likely to be NOT ADMITTED.")

    st.write(f"### Admission Probability : **{probability[0][0]*100:.2f}%**")

    st.progress(float(probability[0][0]))