# 🏡 House Price Prediction

This project is a **Machine Learning application** that predicts house prices based on historical data and property features.  
It follows a modular pipeline including data loading, preprocessing, exploration, training, evaluation, and application deployment.

---

## Dataset
This project uses the [Housing Prices Dataset](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset) provided by YasserH on Kaggle.
Please refer to the dataset page for licensing terms and conditions.
## 📂 Project Structure

House Price Prediction/
│── main.py # Entry point of the project
│
└── src/ # Source code
├── loadData.py # Load dataset
├── preprocessing.py # Data cleaning & preprocessing
├── exploreData.py # Exploratory Data Analysis (EDA)
├── train.py # Model training
├── evaluate.py # Model evaluation (metrics, plots)
├── application.py # Application interface (predict function)
└── init.py # Make 'src' a Python package


---

## 🚀 Features

- Load and clean raw housing data  
- Preprocess categorical & numerical features (e.g., one-hot encoding, scaling)  
- Perform **Exploratory Data Analysis (EDA)** with visualization  
- Train regression models (e.g., Linear Regression, Random Forest, XGBoost)  
- Evaluate models using metrics such as **R² score, RMSE, MAE**  
- Provide an easy-to-use `app()` function to make predictions  

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/house-price-prediction.git
   cd house-price-prediction
2. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate   # MacOS/Linux
    venv\Scripts\activate      # Windows
3. Install dependencies:
    pip install -r requirements.txt

## Usage
1. Train the model
    python src/train.py
2. Evaluate the model
    python src/evaluate.py
3. Run the application
    python main.py

## Evaluation Metrics
R² Score (Coefficient of Determination)
Root Mean Squared Error (RMSE)
Mean Absolute Error (MAE)

## Author
[ngocbao200] (https://github.com/ngocbao220)
AI student ... 
# House-Price-Prediction
