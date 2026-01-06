🛡️ YSENTRY – Phishing Website Detection System

Empowering Digital Safety through Intelligent Machine Learning Analysis

📚 Table of Contents

🌟 Overview

🎯 Problem Statement

🚀 Getting Started

🛠️ Tech Stack & Libraries

💻 Project Execution

🧠 Model Logic & Technical Details

🏗️ System Architecture (Text-based)

⚙️ System Workflow

📊 System Features

✨ Future Enhancements

👨‍💻 Author

🌟 Overview <a name="overview"></a>

Digital security is a growing concern as phishing attacks become more sophisticated. YSENTRY is a specialized tool designed to detect malicious URLs before they can cause harm.

Intelligent Analysis: Uses Machine Learning to understand structural patterns of a URL.

User-Centric Design: Built with a clean Flask interface for non-technical users.

Speed & Reliability: Provides results in milliseconds.

Activity Intelligence: Tracks the last 21 ⚡ scans for history tracking.

🎯 Problem Statement <a name="problem-statement"></a>

Phishing attacks are increasing every year, and most users lack the technical knowledge to identify fake websites. Traditional solutions fail to detect newly created phishing URLs. YSENTRY addresses this by using Machine Learning to classify URLs based on their structural characteristics.

🚀 Getting Started <a name="getting-started"></a>
Step 1: Clone the Repository
git clone https://github.com/YasirAli-21/YSentry.git

Step 2: Navigate to the Project Directory
cd YSentry

Step 3: Setup Environment
python -m venv .venv
.\.venv\Scripts\activate

Step 4: Install Dependencies
pip install -r requirements.txt

🛠️ Tech Stack & Libraries <a name="tech-stack--libraries"></a>

🐍 Python 3.13+

🔥 Flask

📊 Scikit-learn (Multinomial Naive Bayes)

🧪 Pandas & NumPy

🌐 Requests

💻 Project Execution <a name="project-execution"></a>
python app.py


Visit:

http://127.0.0.1:5000

🧠 Model Logic & Technical Details <a name="model-logic--technical-details"></a>
🔹 Machine Learning Algorithm

Multinomial Naive Bayes (MNB) is used due to its efficiency in text-based classification problems.

🔹 Feature Engineering

Lexical analysis of:

URL length

Special characters

Token frequency

🔹 Vectorization

URLs are converted into numerical form using a trained vectorizer.pkl.

🔹 Dataset & Accuracy

21,000+ samples

96.4% accuracy

🏗️ System Architecture (Text-based) <a name="system-architecture-text-based"></a>

The system follows a clean and modular pipeline-based architecture:

User
 ↓
Web Interface (HTML / Flask UI)
 ↓
Flask Backend API
 ↓
Feature Extraction & Preprocessing
 ↓
Machine Learning Model (Scikit-learn)
 ↓
Prediction Result (Safe / Phishing)

Component Breakdown:

Frontend: HTML/CSS rendered via Flask templates

Backend: Flask REST-based processing

ML Model: Trained Naive Bayes classifier

Output: Binary classification (Legitimate / Phishing)

⚙️ System Workflow <a name="system-workflow"></a>

User enters a URL through the web interface.

Flask backend receives the request.

URL features are extracted and preprocessed.

The trained ML model classifies the URL.

Result is displayed to the user.

Scan history is saved (last 21 entries).

📊 System Features <a name="system-features"></a>

🔍 Real-time phishing detection

📊 Scan history tracking

🧠 ML-based classification

⚡ Fast response time

🔐 Secure processing

✨ Future Enhancements <a name="future-enhancements"></a>

🌐 Browser Extension (Chrome / Edge)

🤖 Deep Learning (LSTM / Transformers)

📱 Mobile API integration

🛡️ Live threat intelligence feeds

👨‍💻 Author <a name="author"></a>

Yasir Ali
IT Enthusiast | Final Year BS(IT)
© 2025 YSENTRY


