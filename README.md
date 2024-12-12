# 🌱 Crop Recommendation System

This project is a **web-based application** designed to recommend the best crop to cultivate based on soil and climate conditions. Using **machine learning**, the system provides accurate predictions by analyzing key factors like Nitrogen, Phosphorus, Potassium, temperature, humidity, pH, and rainfall.

## 🚀 Features

- **User-Friendly Interface**: A simple and responsive web form for inputting soil and weather parameters.
- **Accurate Predictions**: Utilizes a trained machine learning model to recommend crops based on scientific data.
- **Dynamic Feedback**: Displays the recommended crop instantly after submission.
- **Customizable Limits**: Input fields include recommended ranges for each parameter to guide users.
- **Modern Design**: Includes header, footer, and a marquee line for a clean and engaging user experience.

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Machine Learning**: Trained with Scikit-learn
- **Deployment**: Compatible with local hosting and cloud platforms

## 📂 Structure

- **`app.py`**: The Flask application handling routing and prediction logic.
- **`model.pkl`**: The trained machine learning model file.
- **`templates/`**: HTML files for rendering the user interface.
- **`static/css/styles.css`**: CSS file for styling the web pages.
- **Dataset**: A CSV file used to train the model, containing agricultural data.

## 📊 Parameters Used for Prediction

- **Nitrogen (N)**: 0–145 kg/ha
- **Phosphorus (P)**: 4–150 kg/ha
- **Potassium (K)**: 4–206 kg/ha
- **Temperature (°C)**: 9–44°C
- **Humidity (%)**: 14%–100%
- **pH**: 3–10
- **Rainfall (mm)**: 20–300 mm/year

## 💻 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/crop-recommendation-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd crop-recommendation-system
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## 🌟 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the project.

## 📜 License

This project is licensed under the [MIT License](LICENSE).
