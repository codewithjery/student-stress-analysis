import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

def load_and_prep(path='../data/dataset.csv'):
    df = pd.read_csv(path)
    features = [
        "Study_Hours_Per_Day", "Sleep_Hours_Per_Day",
        "Physical_Activity_Hours_Per_Day", "Social_Hours_Per_Day",
        "Extracurricular_Hours_Per_Day", "CGPA"
    ]
    X = df[features]
    y = df["Stress_Level_Encoded"]
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    joblib.dump(scaler, "../model/scaler.joblib")
    return X_scaled, y, df

if __name__ == "__main__":
    X, y, df = load_and_prep()
    print(df.head())
