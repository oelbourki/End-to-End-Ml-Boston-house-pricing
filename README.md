# End-to-End Machine Learning: Boston House Price Prediction

This project is a practical demonstration of a complete machine learning pipeline, focusing on predicting house prices in Boston using the renowned Boston Housing dataset. It covers data preprocessing, exploratory analysis, model training, evaluation, and deployment as a user-friendly web application using Flask.

## Table of Contents

- [Project Structure](#project-structure)
- [Key Features](#key-features)
- [Project Stages](#project-stages)
  - [1. Data Analysis and Preprocessing](#1-data-analysis-and-preprocessing)
  - [2. Model Training and Evaluation](#2-model-training-and-evaluation)
  - [3. Model Deployment with Flask](#3-model-deployment-with-flask)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Future Enhancements](#future-enhancements)

## Project Structure

```
├── app.py         # Flask app for model deployment
├── model.ipynb    # Jupyter notebook: data analysis, preprocessing, training & evaluation
├── regmodel.pkl    # Saved trained machine learning model
├── scaler.pkl     # Saved data scaler for consistent input transformation
├── requirements.txt # Project dependencies
├── Dockerfile     # Instructions for building a Docker image
├── Procfile       # Process management for deployment (e.g., on Heroku)
└── templates/     # HTML templates for the web app
    └── home.html   # Main page for user interaction
```

## Key Features

- **End-to-end ML pipeline:** Covers all stages from raw data to deployed model.
- **Missing value imputation:** Employs KNN and MICE imputation to handle missing data effectively.
- **Exploratory Data Analysis (EDA):**  Uses visualizations and correlation analysis to gain insights.
- **Linear Regression model:**  A simple yet powerful model for predicting housing prices.
- **Model evaluation:** Employs various metrics (MAE, MSE, RMSE, R-squared) for robust assessment.
- **Flask web app:**  Provides an interactive platform for users to input data and get predictions.
- **Dockerization:** Simplifies deployment and ensures environment consistency.

## Project Stages

### 1. Data Analysis and Preprocessing (model.ipynb)

- **Data Loading:** Retrieves the Boston Housing dataset from a reliable source.
- **Exploratory Data Analysis (EDA):**
  - Visualizes feature distributions using histograms, scatter plots, etc.
  - Calculates correlation between features and target variable to understand relationships.
  - Identifies potential multicollinearity (high correlation between independent features).
- **Missing Value Handling:**
  - Utilizes KNN Imputation to fill missing values based on the nearest neighbors.
  - Applies MICE (Multivariate Imputation by Chained Equation) for robust imputation.
- **Data Splitting:** Divides the data into training and testing sets for model building and validation.
- **Feature Scaling:** Standardizes features using `StandardScaler` to ensure consistent scaling for the model.

### 2. Model Training and Evaluation (model.ipynb)

- **Model Selection:**  A Linear Regression model is chosen for its simplicity and interpretability.
- **Model Training:**  The model learns patterns from the training data to predict house prices.
- **Model Prediction:**  Predictions are made on the unseen test data to evaluate performance.
- **Performance Metrics:**
  - Mean Absolute Error (MAE): Average absolute difference between predicted and actual values.
  - Mean Squared Error (MSE): Average squared difference between predicted and actual values.
  - Root Mean Squared Error (RMSE): Square root of MSE, providing a more interpretable scale.
  - R-squared (R²):  Proportion of variance in the target variable explained by the model.
  - Adjusted R-squared:  R² adjusted for the number of predictors, penalizing model complexity.
- **Residual Analysis:**  Examines residuals (differences between predicted and actual values) to assess model assumptions.

### 3. Model Deployment with Flask (app.py)

- **Flask App Creation:**  A simple Flask web application is created to serve the model.
- **Model Loading:**  The trained model and data scaler are loaded from pickle files for inference.
- **Routing:**
  - `/`: Renders the main HTML template (`home.html`) for user interaction.
  - `/predict`: Handles POST requests, preprocesses input data, generates predictions, and sends them back to the user.
- **HTML Template (home.html):**
  - Creates a form for users to input feature values.
  - Displays the model's prediction dynamically upon submission.

## Getting Started

### Prerequisites

- Python 3.7+
- pip (package installer for Python)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/End-to-End-Ml-Boston-house-pricing.git
   cd End-to-End-Ml-Boston-house-pricing
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python3 -m venv venv 
   source venv/bin/activate 
   ```

3. **Install required libraries:**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Run the Flask app:**

   ```bash
   flask run
   ```

2. **Access the web application in your browser at `http://127.0.0.1:5000/`.**

## Future Enhancements

- **Experiment with More Models:** Explore other regression algorithms (Ridge, Lasso, Random Forest) to potentially improve accuracy.
- **Feature Engineering:**  Engineer new features from existing ones to potentially enhance model performance.
- **Web App Enhancement:**
  - Improve the user interface and design for a more engaging user experience.
  - Implement input validation to ensure data integrity.
- **Cloud Deployment:**  Deploy the application to a cloud platform (AWS, Heroku, GCP) for scalability and accessibility. 
- **Model Monitoring:** Implement mechanisms to monitor the model's performance over time and retrain as needed. 
