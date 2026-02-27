# 🧠 Mental-Health-Prediction-System  
### *A Full-Stack Machine Learning Web Application for Intelligent Mental Health Analysis*

The **Mental Health Prediction System (MHPS)** is a complete full-stack web application built using **Django and Machine Learning** to predict a user's mental health condition based on lifestyle and behavioral inputs such as sleep, study time, social activity, and more.

This project demonstrates a real-world integration of:

- 🌐 Web Development (Frontend + Backend)  
- 🤖 Machine Learning Model Deployment  
- 🔐 User Authentication & Security  
- 📊 Data Storage & Prediction Tracking  

Designed as a **portfolio-level project**, it showcases an end-to-end pipeline — from model training to real-time predictions and persistent data storage.

---

<p align="center">
  <strong>⚡ Mental Health AI System</strong><br/>
  <em>Smart Predictions • Secure System • Real-World Impact</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/Django-Web%20Framework-green?style=flat-square&logo=django"/>
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Database-SQLite-lightgrey?style=flat-square&logo=sqlite"/>
  <img src="https://img.shields.io/badge/Authentication-Secure-success?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square"/>
</p>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Architecture](#-architecture)
- [Machine Learning Module](#-machine-learning-module)
- [Application Flow](#-application-flow)
- [Core Modules](#-core-modules)
- [Database Design](#-database-design)
- [UI & UX Design](#-ui--ux-design)
- [Security](#-security-features)
- [Getting Started](#-getting-started)
- [Use Cases](#-use-cases)
- [Future Enhancements](#-future-enhancements)
- [Project Structure](#-project-structure)

---

## 🌟 Overview

The **Mental Health Prediction System** is a **full-stack intelligent application** that leverages machine learning to analyze user inputs and predict mental health conditions.

Users provide lifestyle and behavioral data such as:

- Sleep patterns  
- Study duration  
- Eating habits  
- Social media usage  
- Physical activity  
- Substance usage  
- Academic performance  

The system processes this data through a trained ML model and generates **accurate, category-based predictions**, which are then stored for tracking and analysis.

---

## ✨ Key Features

| Feature | Description |
|--------|------------|
| 🔐 **Authentication System** | Secure user registration, login, and session management |
| 🧠 **ML Prediction Engine** | Real-time mental health prediction using trained model |
| 📊 **Prediction History** | Stores user predictions with timestamps |
| 🗂 **Data Management** | Structured storage using Django ORM |
| 🎯 **User-Friendly UI** | Clean interface with interactive forms |

---

## 🛠 Technology Stack

| Layer | Technology | Purpose |
|------|-----------|--------|
| **Frontend** | HTML5, CSS3, Django Templates | UI rendering |
| **Backend** | Python, Django | Application logic |
| **Machine Learning** | Pandas, NumPy, Scikit-learn, Joblib | Model training & prediction |
| **Database** | SQLite | Data persistence |
| **Authentication** | Django Auth System | Security & access control |

---

## 🏗 Architecture

The system follows a **Django MVC architecture integrated with ML layer**:

```
User Input → Django Views → ML Model → Prediction → Database → UI Display
```

### Layers:

1. **Presentation Layer** → HTML templates & forms  
2. **Application Layer** → Django views & routing  
3. **ML Layer** → Model prediction logic  
4. **Data Layer** → SQLite database storage  

---

## 🧠 Machine Learning Module

### ⚙️ Model Training

The ML model is built using:

- **Pandas** → Data preprocessing  
- **NumPy** → Numerical operations  
- **Scikit-learn** → Model training  
- **Joblib** → Model serialization  

---

### 🔄 ML Workflow

```
1. Load dataset
2. Preprocess data
3. Train ML model
4. Save model using joblib
5. Load model in Django
6. Perform predictions in real-time
```

---

## 🔄 Application Flow

1. User registers an account  
2. Logs into the system  
3. Navigates to prediction page  
4. Inputs required parameters  
5. Backend sends data to ML model  
6. Prediction is generated  
7. Result displayed to user  
8. Result stored in database  

---

## 📦 Core Modules

### 📌 `views.py`
- Handles authentication  
- Processes form inputs  
- Loads ML model  
- Returns prediction results  

---

### 📌 `models.py`
- Defines database schema  
- Stores prediction results  

---

### 📌 `train_model.py`
- Trains ML model  
- Saves model for deployment  

---

### 📌 `urls.py`
- Routes user requests  
- Controls navigation  

---

## 🗄 Database Design

### 🧾 PredictionResult Table

- User reference  
- Input parameters  
- Prediction result  
- Timestamp  

---

## 🎨 UI & UX Design

- Clean homepage  
- Login & registration pages  
- Prediction input form  
- Result display page  
- Simple and intuitive navigation  

---

## 🔐 Security Features

- Django authentication system  
- Password hashing  
- Session management  
- Protected routes (login required)  

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x  
- Django  

---

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/mental-health-prediction.git
cd mental-health-prediction
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations
```bash
python manage.py migrate
```

### 5️⃣ Train Model (Optional)
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

## 🎯 Use Cases

- 🧠 Mental health awareness tools  
- 🎓 ML + Django learning projects  
- 💼 Portfolio demonstration  
- 🔬 Research and experimentation  

---

## 🌟 Highlights

✔ Full-stack ML application  
✔ Real-time prediction system  
✔ Secure authentication system  
✔ Data persistence & tracking  
✔ Real-world use case  

---

## 🔮 Future Enhancements

- 📊 Advanced analytics dashboard  
- 🤖 Deep learning integration  
- 🌐 Cloud deployment (AWS/Render)  
- 📱 Fully responsive UI  
- 📈 Model accuracy improvements  

---

## 📁 Project Structure

```
MentalHealthPrediction/
│
├── MHPS/
│   └── urls.py
│
├── prediction/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── templates/
├── static/
│
├── train_model.py
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 👨‍💻 Author

**Vaibhav Sharma**  
*Full Stack Developer | ML Enthusiast*

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 💡 Final Note

> Combining **Machine Learning + Web Development** unlocks powerful real-world applications.

This project is a strong step toward building **intelligent, scalable, and impactful AI systems 🚀**

---

<p align="center">
  Built with ❤️ using Django & Machine Learning<br/>
  <strong>Mental Health Prediction System</strong> — Intelligent Insights for Better Wellbeing
</p>
