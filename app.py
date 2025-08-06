from flask import Flask, render_template, request
import joblib
import numpy as np
import json

app = Flask(__name__)

# Load model and metrics
model = joblib.load("model.pkl")
with open("metrics.json") as f:
    metrics = json.load(f)

@app.route("/")
def home():
    return render_template("index.html", metrics=metrics)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        I = float(request.form["innings"])
        R = float(request.form["runs"])
        B = float(request.form["balls"])
        SR = float(request.form["sr"])
        fours = float(request.form["fours"])
        sixes = float(request.form["sixes"])
        
        input_data = np.array([[I, R, B, SR, fours, sixes]])
        result = model.predict(input_data)[0]

        label_map = {0: "Average", 1: "Flop", 2: "Star"}
        prediction = label_map.get(result, "Unknown")

        return render_template("index.html", prediction=prediction, metrics=metrics)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
