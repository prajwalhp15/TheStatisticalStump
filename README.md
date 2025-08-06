# Cricket Performance Predictor

## Project Description
This project is a web application that utilizes a machine learning model to predict a cricket player's performance category. The model, a Decision Tree Classifier, was trained on batting statistics from an ODI Cricket World Cup dataset. The application provides a user-friendly interface for players to input their data and receive a prediction, which classifies them as "Star," "Average," or "Flop." The app also displays the model's performance metrics, such as accuracy, precision, recall, and F1 score, providing a transparent view of its effectiveness.

## Features
- **Web Interface:** A simple and intuitive web form to input a player's batting statistics.
- **Machine Learning Model:** A pre-trained `DecisionTreeClassifier` model to make predictions.
- **Performance Metrics:** Displays key metrics of the model, including Accuracy, Precision, Recall, and F1 Score.
- **Categorical Prediction:** Classifies a player's performance into one of three categories: "Star," "Average," or "Flop."

## Project Structure
- `app.py`: The main Flask application file that handles web requests, loads the model, and renders the front-end.
- `model.pkl`: The serialized `scikit-learn` model object.
- `metrics.json`: A JSON file containing the performance metrics of the model.
- `requirements.txt`: A list of all Python dependencies required to run the project.
- `templates/index.html`: The HTML file for the web interface.

## Technologies Used
- **Backend:** Python, Flask
- **Machine Learning:** `scikit-learn`, `joblib`
- **Data Handling:** `numpy`, `pandas`

## How to Run the Project

### Step 1: Clone the Repository
```bash
git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name
```
Step 2: Install Dependencies
Ensure you have Python installed. It's recommended to use a virtual environment.


# Create a virtual environment (optional but recommended)
python -m venv venv
# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS and Linux
source venv/bin/activate

# Install the required libraries
pip install -r requirements.txt

Step 3: Run the Application
Start the Flask development server:
python app.py

Step 4: Access the Application
Open your web browser and navigate to http://127.0.0.1:5000 to see the application running.

You can copy this text and save it as `README.md` in the root of your project directory.
