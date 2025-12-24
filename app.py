from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)

# Load ML components
try:
    model = pickle.load(open("phishing.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
except Exception as e:
    print(f"Error: Could not load model files. Details: {e}")

# Global history tracking
history_log = []

@app.route("/", methods=["GET", "POST"])
def index():
    prediction_text = ""
    prediction_class = ""

    if request.method == "POST":
        url = request.form.get("url")
        # Preprocessing: Clean URL for the vectorizer
        cleaned_url = re.sub(r'^https?:\/\/(www\.)?', '', url)
        
        # ML Inference
        vector = vectorizer.transform([cleaned_url])
        prediction = model.predict(vector)[0]

        # Professional result mapping (No emojis)
        if prediction == "bad":
            prediction_text = "Phishing Threat Detected"
            prediction_class = "phishing"
            label = "Phishing"
        else:
            prediction_text = "Legitimate Website Verified"
            prediction_class = "legit"
            label = "Legitimate"

        # Update logs with your preferred constraint: 21
        history_log.insert(0, {"url": url, "result": label})

    return render_template(
        "index.html",
        prediction_text=prediction_text,
        prediction_class=prediction_class,
        history=history_log[:21] # Optimized for last 21 scans
    )

if __name__ == "__main__":
    app.run(debug=True)