# Mental-Health-Prediction-System
Mental Health Prediction System is a Django + Python web app that predicts student mental health from inputs like sleep, study time, meals, social media, activity, substance use, and academics. It includes login/registration, stores prediction history, and uses a trained scikit-learn model to generate reliable category-based results well.

# 🧠 Mental Health Prediction System

### A Full-Stack Machine Learning Web Application

---

## 📌 Overview

The **Mental Health Prediction System** is a full-stack web application built using **Django** and **Machine Learning** that predicts a user's mental health condition based on input parameters.

This project combines:

* 🌐 **Web Development (Frontend + Backend)**
* 🤖 **Machine Learning Model Training**
* 🧩 **User Authentication System**
* 📊 **Prediction Storage & Analysis**

It is designed as a **complete portfolio-level project**, demonstrating end-to-end development — from data processing to deployment-ready architecture.

---

## 🚀 Key Features

### 🔐 Authentication System

* User Registration
* Secure Login & Logout
* Password hashing using Django authentication system

### 🧠 Mental Health Prediction

* Machine learning model trained using dataset
* Real-time prediction via web interface
* Input-based prediction logic

### 📊 Data Management

* Stores prediction results in database
* Tracks user activity
* SQLite database integration

### 🎯 User Experience

* Clean and simple UI
* Interactive forms
* Responsive templates

---

## 🏗️ Project Architecture

```
MentalHealthPrediction/
│
├── MHPS/                  # Main project configuration
│   └── urls.py
│
├── prediction/            # Core app
│   ├── models.py          # Database models
│   ├── views.py           # Business logic
│   ├── urls.py            # Routing
│
├── templates/             # HTML UI files
├── static/                # CSS/JS assets
│
├── train_model.py         # ML model training script
├── db.sqlite3             # Database
├── manage.py              # Django entry point
```

---

## 🧠 Machine Learning Module

### ⚙️ Model Training

The ML model is trained using:

* **Pandas** → Data processing
* **NumPy** → Numerical computation
* **Scikit-learn / Joblib** → Model building & saving

### 🔁 Workflow

1. Dataset is loaded
2. Data preprocessing is applied
3. Model is trained
4. Model is saved using `joblib`
5. Django loads the model for predictions

---

## 🖥️ Tech Stack

### 🌐 Frontend

* HTML5
* CSS3
* Django Templates

### ⚙️ Backend

* Python
* Django Framework

### 🤖 Machine Learning

* Pandas
* NumPy
* Joblib
* Scikit-learn (assumed from structure)

### 🗄️ Database

* SQLite (default Django DB)

---

## 🔄 Application Flow

1. User registers an account
2. Logs into the system
3. Navigates to prediction page
4. Enters required inputs
5. ML model processes inputs
6. Prediction result is displayed
7. Result is saved in database

---

## 📂 Core Components Explained

### 📌 `views.py`

Handles:

* Authentication logic
* Form handling
* Prediction processing
* Rendering templates

### 📌 `models.py`

Defines:

* PredictionResult model
* Database structure

### 📌 `train_model.py`

* Trains machine learning model
* Saves trained model for later use

### 📌 `urls.py`

* Maps routes to views
* Controls navigation

---

## 🎨 UI Features

* Clean welcome page
* Login & registration forms
* Prediction interface
* User-friendly navigation

---

## ⚡ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/mental-health-prediction.git
cd mental-health-prediction
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```bash
python manage.py migrate
```

### 5️⃣ Train Model (Optional if not pre-trained)

```bash
python train_model.py
```

### 6️⃣ Run Server

```bash
python manage.py runserver
```

### 7️⃣ Open in Browser

```
http://127.0.0.1:8000/
```

---

## 📊 Database Schema

### 🧾 PredictionResult

* User reference
* Input data
* Prediction output
* Timestamp

---

## 🔐 Security Features

* Password hashing (Django built-in)
* Authentication middleware
* Login-required routes

---

## 🌟 Highlights

✔ Full-stack project from scratch
✔ Machine learning integration
✔ Clean MVC architecture
✔ Real-world use case
✔ Beginner to intermediate level project

---

## 🧩 Future Enhancements

* 📈 Add advanced ML models
* 📊 Dashboard with analytics
* 🌍 Deployment on cloud (AWS/Heroku)
* 📱 Mobile responsive UI
* 🧠 Deep Learning integration

---

## 👨‍💻 Author

**Vaibhav Sharma**

* Passionate Full Stack Developer & ML Enthusiast
* Built this project from scratch as part of learning & portfolio

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 💡 Final Note

This project demonstrates the power of combining **web development + machine learning** to solve real-world problems like mental health awareness.

If you found this helpful ⭐, consider giving it a star!

---
