import pickle
from flask import Flask, render_template, request
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the user input values from the form
    nitrogen = float(request.form['nitrogen'])
    phosphorus = float(request.form['phosphorus'])
    potassium = float(request.form['potassium'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])

    # Create a feature array for prediction
    features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])

    # Predict the crop type using the model
    prediction = model.predict(features)

    # Convert the prediction to a readable format (if necessary)
    crop_prediction = prediction[0]  # Assuming model returns a label

    return render_template('index.html', prediction_text=f"Recommended Crop: {crop_prediction}")

if __name__ == "__main__":
    app.run(debug=True)
