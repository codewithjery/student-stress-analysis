import pandas as pd
import numpy as np

np.random.seed(42)
n = 500

data = {
    "Study_Hours_Per_Day": np.random.uniform(1, 10, n),
    "Sleep_Hours_Per_Day": np.random.uniform(4, 10, n),
    "Physical_Activity_Hours_Per_Day": np.random.uniform(0, 3, n),
    "Social_Hours_Per_Day": np.random.uniform(0, 4, n),
    "Extracurricular_Hours_Per_Day": np.random.uniform(0, 4, n),
    "CGPA": np.random.uniform(5.0, 10, n)
}

df = pd.DataFrame(data)

def get_stress(row):
    if row["Study_Hours_Per_Day"] > 7 or row["Sleep_Hours_Per_Day"] < 5:
        return "High"
    elif 5 <= row["Sleep_Hours_Per_Day"] <= 7:
        return "Moderate" 
        
    else:
        return "Low"

df["Stress_Level"] = df.apply(get_stress, axis=1)
df["Stress_Level_Encoded"] = df["Stress_Level"].map({"Low": 0, "Moderate": 1, "High": 2})

df.to_csv("../data/dataset.csv", index=False)
print("✅ Student Lifestyle dataset saved to data/dataset.csv")
print(df.head())
