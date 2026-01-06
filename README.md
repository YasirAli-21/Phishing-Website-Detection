# 🛡️ YSENTRY – Phishing Website Detection System

![CI](https://github.com/YasirAli-21/Phishing-Website-Detection/actions/workflows/python-ci.yml/badge.svg?branch=master)

**Empowering Digital Safety through Intelligent Machine Learning Analysis**

---

## 📚 Table of Contents
- Overview
- Problem Statement
- Getting Started
- Tech Stack & Libraries
- Project Execution
- Model Logic & Technical Details
- System Architecture (Text-based)
- System Workflow
- System Features
- Future Enhancements
- Author

---

## 🌟 Overview
Phishing attacks are increasing rapidly and pose a serious threat to digital security.  
**YSENTRY** is a Machine Learning–based system designed to detect phishing websites by analyzing URL patterns and structural characteristics.

Key highlights:
- Machine Learning–based URL classification
- Simple and user-friendly Flask interface
- Fast and lightweight prediction system
- Scan history tracking (last 21 URLs)

---

## 🎯 Problem Statement
Most internet users are unable to identify phishing websites due to their realistic appearance.  
Traditional rule-based systems often fail to detect newly created phishing URLs.

**YSENTRY** addresses this problem by using Machine Learning to classify URLs as **Safe** or **Phishing** based on extracted features.

---

## 🚀 Getting Started

### Clone the Repository
```bash
git clone https://github.com/YasirAli-21/Phishing-Website-Detection.git
Navigate to Project Directory
bash
Copy code
cd Phishing-Website-Detection
Create Virtual Environment
bash
Copy code
python -m venv .venv
Activate Environment (Windows)
bash
Copy code
.\.venv\Scripts\activate
Install Dependencies
bash
Copy code
pip install -r requirements.txt
🛠️ Tech Stack & Libraries
Python – Core programming language

Flask – Web framework

Scikit-learn – Machine Learning model

Pandas & NumPy – Data processing

HTML/CSS – Frontend interface

💻 Project Execution
Run the application using:

bash
Copy code
python app.py
Open your browser and visit:

cpp
Copy code
http://127.0.0.1:5000
🧠 Model Logic & Technical Details
Machine Learning Algorithm
The system uses Multinomial Naive Bayes, which is efficient for text-based classification problems.

Feature Engineering
URL length

Special characters

Lexical patterns

Vectorization
URLs are converted into numerical features using a trained vectorizer.pkl.

Dataset & Accuracy
Dataset size: 21,000+ URLs

Achieved accuracy: 96.4%

🏗️ System Architecture (Text-based)
User
→ Web Interface (HTML / Flask UI)
→ Flask Backend
→ Feature Extraction & Preprocessing
→ Machine Learning Model (Scikit-learn)
→ Prediction Result (Safe / Phishing)

Components
Frontend: HTML/CSS (Flask templates)

Backend: Flask (Python)

ML Model: Multinomial Naive Bayes

Output: Binary classification

⚙️ System Workflow
User enters a URL through the web interface.

Flask backend receives the request.

URL features are extracted and preprocessed.

The trained ML model performs classification.

Result is displayed to the user.

Scan result is saved in history (last 21 scans).

📊 System Features
Real-time phishing detection

Machine Learning–based analysis

Scan history tracking

Fast and lightweight processing

Simple and clean UI

✨ Future Enhancements
Browser extension (Chrome / Edge)

Deep Learning models (LSTM, Transformers)

Mobile API integration

Live threat intelligence feeds

👨‍💻 Author
Yasir Ali
Final Year BS(IT) Student
© 2025 – YSENTRY

GitHub: https://github.com/YasirAli-21
LinkedIn: https://www.linkedin.com/in/yasisahito
