# End-to-End Machine Learning: Boston House Price Prediction

This project demonstrates an end-to-end machine learning workflow, from data preprocessing and model training to deployment using Flask. We will build a model to predict house prices in Boston using the famous Boston Housing dataset.

## Project Structure

```
├── app.py         # Flask app for model deployment
└── model.ipynb    # Jupyter notebook for data analysis, preprocessing, model training, and evaluation
```

## Project Overview

1. **Data Analysis and Preprocessing (model.ipynb):**
   - Load the Boston Housing dataset.
   - Perform exploratory data analysis (EDA) to understand feature distributions and relationships.
   - Handle missing values using KNN Imputation and MICE Imputation.
   - Analyze feature correlations to identify potential multicollinearity.

2. **Model Training and Evaluation (model.ipynb):**
   - Split the dataset into training and testing sets.
   - Standardize features using `StandardScaler`.
   - Train a Linear Regression model.
   - Evaluate model performance using metrics like MAE, MSE, RMSE, R-squared, and adjusted R-squared.
   - Visualize model predictions and residuals.

3. **Model Deployment with Flask (app.py):**
   - Create a Flask web application.
   - Load the trained model and scaler from pickle files.
   - Define routes for a home page (`/`) and a prediction endpoint (`/predict`).
   - Create an HTML template (`home.html`) for user interaction.
   - Handle POST requests to the `/predict` endpoint, preprocess input data, generate predictions using the loaded model, and return the prediction to the user.

## How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/End-to-End-Ml-Boston-house-pricing.git
   cd End-to-End-Ml-Boston-house-pricing
   ```

2. **Install required libraries:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app:**

   ```bash
   flask run
   ```

4. **Access the web application in your browser at `http://127.0.0.1:5000/`.**

## Future Improvements

- Experiment with different regression algorithms (e.g., Ridge, Lasso, ElasticNet) to potentially improve model performance.
- Implement feature engineering techniques to extract more informative features from existing ones.
- Enhance the web application with a more user-friendly interface.
- Containerize the application using Docker for easier deployment.
