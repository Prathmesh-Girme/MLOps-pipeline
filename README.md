# Advertising Sales Prediction using Linear Regression 📈

A simple, well-structured **Linear Regression** pipeline built with `scikit-learn` to predict **Sales** based on advertising spend across **TV**, **Radio**, and **Newspaper** channels.

This project walks through the complete machine learning workflow — from data loading to model evaluation — with clear, step-by-step console output for easy understanding. Built as a practice project and portfolio showcase of core ML and data analysis skills.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Pipeline Steps](#pipeline-steps)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Sample Output](#sample-output)
- [Key Learnings](#key-learnings)
- [License](#license)

---

## 🔍 Overview

The pipeline implements an end-to-end supervised learning workflow that:

- Loads advertising data from a CSV file
- Cleans and inspects the dataset
- Analyzes correlations between features and the target variable
- Trains a **Linear Regression** model
- Evaluates performance using MSE, RMSE, and R² score
- Displays the learned coefficients and intercept

---

## 📊 Dataset

The dataset used is the classic **Advertising dataset**, which contains advertising budgets (in thousands of dollars) for **TV**, **Radio**, and **Newspaper**, along with the resulting **Sales** (in thousands of units).

| Column     | Description                          |
|------------|---------------------------------------|
| TV         | Advertising budget spent on TV        |
| radio      | Advertising budget spent on Radio     |
| newspaper  | Advertising budget spent on Newspaper |
| sales      | Product sales (target variable)       |

Place the dataset at:

```
Data/Advertising.csv
```

---

## ⚙️ Pipeline Steps

The script runs through the following 11 steps automatically:

1. **Load the data** from the CSV file
2. **Remove unwanted columns** (e.g., an unnamed index column)
3. **Check for missing values**
4. **Display statistical summary** of the dataset
5. **Compute correlation** between independent and dependent variables
6. **Separate features (X) and target (Y)**
7. **Split data** into training and testing sets (80/20 split)
8. **Train** a Linear Regression model
9. **Test** the model on unseen data
10. **Evaluate** the model using MSE, RMSE, and R² score
11. **Display model coefficients** and intercept

---

## 🧰 Requirements

- Python 3.7+
- numpy
- pandas
- scikit-learn

---

## 🚀 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/advertising-sales-regression.git
   cd advertising-sales-regression
   ```

2. Install the required dependencies:

   ```bash
   pip install numpy pandas scikit-learn
   ```

3. Make sure your dataset is placed at:

   ```
   Data/Advertising.csv
   ```

---

## ▶️ Usage

Run the script directly:

```bash
python regression.py
```

The script will print a detailed, step-by-step log of the entire regression pipeline to the console, including data previews, statistics, correlations, model training progress, predictions, and evaluation metrics.

---

## 📁 Project Structure

```
advertising-sales-regression/
│
├── Data/
│   └── Advertising.csv
│
├── regression.py
└── README.md
```

---

## 🧪 Sample Output

```
========================================
Step 1 : Load the data from CSV file
========================================
...
========================================
Step 10 : Evaluate the model
========================================
Mean Squared Error : 2.907756...
Root Mean Squared Error : 1.7052...
R2 Score : 0.9059...

========================================
Step 11 : Display coefficients of the model
========================================
TV Coefficient : 0.0544...
Radio Coefficient : 0.1070...
Newspaper Coefficient : 0.0003...
Intercept : 4.7143...

========================================
Linear Regression Pipeline Completed Successfully
========================================
```

*(Actual values will vary slightly depending on the dataset and train/test split.)*

---

## 🧠 Key Learnings

- Practiced a complete supervised learning workflow using `pandas` and `scikit-learn`
- Applied exploratory data analysis (EDA) techniques: missing value checks, statistical summaries, and correlation analysis
- Implemented train/test splitting and model evaluation using standard regression metrics (MSE, RMSE, R²)
- Interpreted model coefficients to understand feature impact on sales

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

### ✨ Author

Built as a hands-on practice project to strengthen and showcase machine learning fundamentals using scikit-learn.
