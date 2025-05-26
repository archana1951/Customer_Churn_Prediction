from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('churn_model.pkl')

@app.route('/')
def index():
    return "Customer Churn Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return jsonify({'churn_prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
