import pandas as pd
import joblib


model = joblib.load("../model/rf_model.joblib")
scaler = joblib.load("../model/scaler.joblib")

def predict_single(sample_dict):
    df = pd.DataFrame([sample_dict])
    df_scaled = scaler.transform(df)
    pred = model.predict(df_scaled)[0]

    stress_map = {
        0: "Low",
        1: "Moderate",
        2: "High"
    }
    return stress_map[pred]



if __name__ == "__main__":
    print("=== Manual Stress Prediction ===")

    sample = {
        "Study_Hours_Per_Day": float(input("Enter Study Hours per Day: ")),
        "Sleep_Hours_Per_Day": float(input("Enter Sleep Hours per Day: ")),
        "Physical_Activity_Hours_Per_Day": float(input("Enter Physical Activity Hours per Day: ")),
        "Social_Hours_Per_Day": float(input("Enter Social Hours per Day: ")),
        "Extracurricular_Hours_Per_Day": float(input("Enter Extracurricular Hours per Day: ")),
        "CGPA": float(input("Enter CGPA (5–10): "))
    }

    
    if not (5 <= sample["CGPA"] <= 10):
        raise ValueError("CGPA must be between 5 and 10")

    result = predict_single(sample)
    print("\nPredicted Stress Level:", result)
