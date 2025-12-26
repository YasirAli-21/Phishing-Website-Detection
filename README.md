# 🛡️ YSENTRY – Phishing Website Detection System

**Empowering Digital Safety through Intelligent Machine Learning Analysis**

---

## 📚 Table of Contents
- 🌟 [Overview](#overview)
- 🎯 [Problem Statement](#problem-statement)
- 🚀 [Getting Started](#getting-started)
- 🛠️ [Tech Stack & Libraries](#tech-stack--libraries)
- 💻 [Project Execution](#project-execution)
- 🧠 [Model Logic & Technical Details](#model-logic--technical-details)
- ⚙️ [System Workflow](#system-workflow)
- 📊 [System Features](#system-features)
- ✨ [Future Enhancements](#future-enhancements)
- 👨‍💻 [Author](#author)

---

## 🌟 Overview <a name="overview"></a>

With the rapid growth of online services, phishing websites have become one of the most dangerous cybersecurity threats. These malicious sites imitate trusted platforms to steal sensitive user information such as usernames, passwords, and financial data.

**YSENTRY** is an AI-powered phishing website detection system that helps users identify malicious URLs before interacting with them. By combining Machine Learning with a clean web-based interface, YSENTRY provides fast, accurate, and user-friendly protection against phishing attacks.

---

## 🎯 Problem Statement <a name="problem-statement"></a>

Phishing attacks are increasing every year, and most users lack the technical knowledge to identify fake or malicious websites. Traditional blacklist-based solutions fail to detect newly created phishing URLs, leaving users vulnerable.

The challenge is to build an intelligent system that can:
- Detect phishing websites in real time  
- Analyze URLs based on patterns rather than static lists  
- Provide clear and understandable results to non-technical users  

YSENTRY addresses this problem by using Machine Learning to classify URLs based on their structural and lexical characteristics.

---

## 🚀 Getting Started <a name="getting-started"></a>

Follow the steps below to run YSENTRY locally.

### 1️⃣ Clone the Repository
```bash
git clone [https://github.com/YasirAli21-cmd/YSentry.git](https://github.com/YasirAli21-cmd/YSentry.git)
2️⃣ Navigate to the Project Directory
Bash

cd YSentry
3️⃣ Create and Activate Virtual Environment
Bash

python -m venv .venv
.\.venv\Scripts\activate
4️⃣ Install Required Dependencies
Bash

pip install -r requirements.txt
🛠️ Tech Stack & Libraries <a name="tech-stack--libraries"></a>
YSENTRY is developed using the following technologies:

🐍 Python 3.13+ – Core programming language

🔥 Flask – Backend web framework

📊 Scikit-learn – Machine Learning model training and prediction

🧪 Pandas – Data preprocessing and handling

🔢 NumPy – Numerical computations

🌐 Requests – URL and SSL validation

💻 Project Execution <a name="project-execution"></a>
Run the Flask application using the following command:

Bash

python app.py
Once the server starts, open your browser and visit: http://127.0.0.1:5000

You will be redirected to the YSENTRY dashboard.

🧠 Model Logic & Technical Details <a name="model-logic--technical-details"></a>
🔹 Machine Learning Algorithm
Multinomial Naive Bayes Selected due to its high efficiency and performance in text-based classification tasks such as URL analysis.

🔹 Feature Engineering
The system performs lexical analysis on URLs, including:

URL length analysis

Frequency of special characters (@, ?, -, .)

Domain and protocol patterns

🔹 Vectorization
URLs are transformed into numerical vectors using a trained vectorizer.pkl. This enables statistical probability-based classification.

🔹 Dataset & Accuracy
Trained on 21,000+ phishing and legitimate URLs.

Achieved 96.4% accuracy.

⚙️ System Workflow <a name="system-workflow"></a>
Input Phase – User enters a URL in the dashboard.

Preprocessing Phase – URL is cleaned and standardized.

Feature Extraction Phase – Lexical features are extracted.

Classification Phase – ML model predicts the URL class.

Result Phase – Verdict displayed as 🟥 PHISHING or 🟩 LEGITIMATE.

Logging Phase – URL stored in scan history (last 21 scans).

📊 System Features <a name="system-features"></a>
🔍 Real-time phishing website detection.

📊 Scan history tracking (last 21 URLs).

🧠 Machine Learning–based classification.

🎯 Clean and responsive dashboard.

⚡ Fast and lightweight prediction engine.

✨ Future Enhancements <a name="future-enhancements"></a>
Planned improvements for upcoming versions of YSENTRY:

🌐 Browser extension (Chrome / Edge).

🤖 Deep Learning integration (LSTM models).

📱 Mobile API for SMS and messaging apps.

🛡️ Live threat intelligence feeds.

👨‍💻 Author <a name="author"></a>
Yasir Ali IT Enthusiast | © 2025 YSENTRY

🔗 GitHub

💼 LinkedIn