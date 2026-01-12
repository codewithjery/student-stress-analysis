# 🎓 Student Stress Analysis System

An **AI-powered Student Stress Analysis System** that predicts student stress levels using **Machine Learning** and provides **personalized AI-based recommendations** through an interactive **Streamlit web application**.

---
## 🖼️ Application Screenshot

<img src="images/app_screenshot.png" width="700">

## 🚀 Project Overview

Student stress has become a major concern in modern academic environments. This project analyzes academic, lifestyle, and performance-related factors to **predict stress levels** and provide **actionable stress-management advice**.

The system uses a **Random Forest Machine Learning model** trained on a synthetic dataset and presents results through both a **command-line interface** and a **web-based dashboard**.

---

## ✨ Key Features

* Synthetic student dataset generation
* Data preprocessing (scaling & encoding)
* Random Forest–based stress prediction model
* Command-line prediction interface
* AI-style personalized stress advice
* Interactive Streamlit web application
* User feedback logging using SQLite
* Modular, scalable, and academic-friendly structure

---

## 🧠 Machine Learning Model

* **Algorithm:** Random Forest Classifier
* **Reason for Selection:**

  * Handles non-linear relationships effectively
  * Reduces overfitting
  * Works well with tabular data
  * Provides reliable performance and interpretability

---

## 📊 Dataset Features

The dataset captures academic workload, lifestyle balance, social support, and performance pressure:

* **Study_Hours_Per_Day**
  Represents the student’s daily academic workload and study pressure.

* **Sleep_Hours_Per_Day**
  A critical physiological indicator reflecting rest and recovery. Lower sleep duration often correlates with higher stress.

* **Physical_Activity_Hours_Per_Day**
  Measures lifestyle balance and physical well-being.

* **Social_Hours_Per_Day**
  Indicates time spent in social interactions and support systems.

* **Extracurricular_Hours_Per_Day**
  Accounts for participation in non-academic responsibilities such as clubs, hobbies, or part-time work.

* **CGPA**
  Quantifies academic performance pressure and expectations.

These features collectively allow the model to make **realistic and multidimensional stress predictions**.

---

## 📂 Project Structure

```
student-stress-analysis/
├── data/
│   └── dataset.csv                # Generated dataset
├── src/
│   ├── generate_dataset.py        # Synthetic data generation
│   ├── data_prep.py               # Data preprocessing
│   ├── train_model.py             # Model training
│   ├── predict.py                 # CLI prediction interface
│   ├── ai_assistant.py            # AI-based advice logic
│   └── app_streamlit.py           # Streamlit web app
├── model/
│   └── rf_model.joblib             # Trained ML model
├── feedback.db                     # User feedback database
└── requirements.txt               # Project dependencies
```

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn
* **Model Persistence:** Joblib
* **Web Framework:** Streamlit
* **Database:** SQLite

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd student-stress-analysis
```

---

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment:

* **Windows**

```bash
venv\Scripts\activate
```

* **Mac / Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

### 🔹 Step 1: Generate Dataset


```bash
cd src
```
```bash
python generate_dataset.py
```

---

### 🔹 Step 2: Train the Machine Learning Model

```bash
python train_model.py
```

---

### 🔹 Step 3: Run Prediction (Command Line)

```bash
python predict.py
```

---

### 🔹 Step 4: Launch the Web Application

```bash
streamlit run app_streamlit.py
```
****Mac users use python3 instead of python command****
---

## 📈 Output

* Predicted Stress Level (Low / Medium / High)
* AI-generated personalized stress management advice
* User interaction data stored for future analysis

---

## 🎯 Use Cases

* Final Year MCA Project
* AI & Machine Learning coursework
* Student mental health analysis
* Academic counseling support tools
* Resume and portfolio project

---

## 🔮 Future Enhancements

* Integration of real-world student datasets
* Deep Learning–based stress prediction
* Mobile or cloud deployment
* Advanced analytics and visualization dashboards
* Real-time stress monitoring

---

## 👨‍💻 Author

**Name:** Abhik Bhowmik
**Degree:** MCA
**Specialization:** Artificial Intelligence & Machine Learning

---

## 📜 License

This project is intended for **educational and academic use only**.


