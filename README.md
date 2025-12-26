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
Digital security is a growing concern as phishing attacks become more sophisticated. **YSENTRY** is a specialized tool designed to detect malicious URLs before they can cause harm.

* **Intelligent Analysis:** Uses Machine Learning to understand structural patterns of a URL.
* **User-Centric Design:** Built with a clean Flask interface for non-technical users.
* **Speed & Reliability:** Provides results in milliseconds.
* **Activity Intelligence:** Tracks the last **21** ⚡ scans for history tracking.

---

## 🎯 Problem Statement <a name="problem-statement"></a>
Phishing attacks are increasing every year, and most users lack the technical knowledge to identify fake websites. Traditional solutions fail to detect newly created phishing URLs. **YSENTRY** addresses this by using Machine Learning to classify URLs based on their structural characteristics.

---

## 🚀 Getting Started <a name="getting-started"></a>
Follow these steps to run YSENTRY locally:

### Step 1: Clone the Repository
Open your terminal and use the following command to download the project:
`git clone https://github.com/YasirAli21-cmd/YSentry.git`

### Step 2: Navigate to the Project Directory
Enter the project folder:
`cd YSentry`

### Step 3: Setup Environment
Create and activate a virtual environment to isolate dependencies:
* Create: `python -m venv .venv`
* Activate (Windows): `.\.venv\Scripts\activate`

### Step 4: Install Dependencies
Install all required libraries using:
`pip install -r requirements.txt`

---

## 🛠️ Tech Stack & Libraries <a name="tech-stack--libraries"></a>
The project utilizes a robust stack of technologies:
* 🐍 **Python 3.13+** – Core programming language.
* 🔥 **Flask** – Backend web framework.
* 📊 **Scikit-learn** – Machine Learning model (Multinomial Naive Bayes).
* 🧪 **Pandas & NumPy** – Data handling.
* 🌐 **Requests** – URL and SSL validation.

---

## 💻 Project Execution <a name="project-execution"></a>
Run the Flask application using the following command in your terminal:
`python app.py`

*Once running, open your browser and visit: `http://127.0.0.1:5000`*

---

## 🧠 Model Logic & Technical Details <a name="model-logic--technical-details"></a>
The "Brain" of YSENTRY is based on high-performance text classification logic.



### 🔹 Machine Learning Algorithm
We use **Multinomial Naive Bayes (MNB)** because it is highly efficient for text-based classification.

### 🔹 Feature Engineering
The system performs lexical analysis of URL length and special characters.

### 🔹 Vectorization
Raw URLs are transformed into numerical vectors using a trained `vectorizer.pkl`.

### 🔹 Dataset & Accuracy
Achieved a verified **96.4% Accuracy** rate on 21,000+ samples.

---

## ⚙️ System Workflow <a name="system-workflow"></a>
1. **Input:** User enters a URL in the dashboard.
2. **Analysis:** System extracts lexical features and checks SSL status.
3. **Prediction:** The MNB model classifies the URL as safe or malicious.
4. **Result:** Verdict displayed as 🟥 **PHISHING** or 🟩 **LEGITIMATE**.
5. **Logging:** Result is automatically saved in the history of the last **21** scans.

---

## 📊 System Features <a name="system-features"></a>
* 🔍 Real-time phishing website detection.
* 📊 Scan history tracking (last **21** URLs).
* 🧠 Machine Learning–based classification.
* ⚡ Fast and lightweight prediction engine.

---

## ✨ Future Enhancements <a name="future-enhancements"></a>
* 🌐 Browser extension (Chrome / Edge) for real-time protection.
* 🤖 Deep Learning integration (LSTM models).
* 📱 Mobile API for messaging apps.
* 🛡️ Live threat intelligence feeds.

---

## 👨‍💻 Author <a name="author"></a>
**Yasir Ali** | IT Enthusiast | © 2025 YSENTRY

I am a developer passionate about bridging the gap between AI and Cybersecurity.

[![github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/YasirAli-21)
[![linkedin](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yasisahito)