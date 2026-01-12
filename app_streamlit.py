
import streamlit as st
import pandas as pd
from predict import predict_single
from ai_assistant import get_mock_recommendation
from datetime import datetime

st.set_page_config(page_title="Student Lifestyle & Stress Analysis", page_icon="🎓", layout="wide")
st.title("🎓 Well come to Stressify")

st.markdown("This app predicts a student's **stress level (Low / Moderate / High)** based on their **daily lifestyle and academic performance**.")

st.sidebar.header("📋 Enter Lifestyle and Academic Details")

study = st.sidebar.slider("🕒 Study Hours Per Day", 0.0, 12.0, 6.0)
sleep = st.sidebar.slider("😴 Sleep Hours Per Day", 0.0, 12.0, 7.0)
activity = st.sidebar.slider("🏃‍♂️ Physical Activity Hours Per Day", 0.0, 4.0, 1.0)
social = st.sidebar.slider("🗣️ Social Hours Per Day", 0.0, 6.0, 2.0)
extra = st.sidebar.slider("🎭 Extracurricular Hours Per Day", 0.0, 6.0, 1.0)
cgpa = st.sidebar.slider(
    "🎓 CGPA",
    min_value=5.0,
    max_value=10.0,
    value=8.0,
    step=0.1
)


user_input = {
    "Study_Hours_Per_Day": study,
    "Sleep_Hours_Per_Day": sleep,
    "Physical_Activity_Hours_Per_Day": activity,
    "Social_Hours_Per_Day": social,
    "Extracurricular_Hours_Per_Day": extra,
    "CGPA": cgpa
}

st.write("### 🧾 Input Summary")
st.dataframe(pd.DataFrame([user_input]))

if st.button("🔍 Predict Stress Level"):
    stress_level = predict_single(user_input)
    st.success(f"Predicted Stress Level: **{stress_level}**")
    st.info(get_mock_recommendation(stress_level))
    with open("feedback.db", "a") as f:
        f.write(f"{datetime.now()},{stress_level}\n")

