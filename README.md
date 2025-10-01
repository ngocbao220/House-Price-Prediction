# 🏡 House Price Prediction

This project is a **Machine Learning application** that predicts house prices based on historical data and property features.  
It follows a modular pipeline including data loading, preprocessing, exploration, training, evaluation, and application deployment.

---

## Dataset
This project uses the [Housing Prices Dataset](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset) provided by YasserH on Kaggle.
Please refer to the dataset page for licensing terms and conditions.

## 🚀 Features

- Load and clean raw housing data  
- Preprocess categorical & numerical features
- Perform **Exploratory Data Analysis (EDA)** with visualization (See it in fig folder)
- Train regression models (Logistic Regression)  
- Evaluate models using metrics such as **R² score, RMSE, MAE**  
- Provide an easy-to-use `app()` function to make predictions  

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ngocbao220/House-Price-Prediction.git
   cd house-price-prediction
2. Create and activate a conda environment:
    ```bash
    conda create -n houseprice python=3.12
    conda activate houseprice
3. Install dependencies:
    ```bash
    pip install -r requirements.txt

## Usage
1. Train the model
    python src/train.py
2. Evaluate the model
    python src/evaluate.py
3. Run the application
    python main.py

## Evaluation Metrics
- R² Score (Coefficient of Determination)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)

## Author
- 👨‍💻[ngocbao200](https://github.com/ngocbao220)
- AI student ... 
