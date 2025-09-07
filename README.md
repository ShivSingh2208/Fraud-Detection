# 💳 Fraud Detection App using Machine Learning & Streamlit

A machine learning-based web application that detects fraudulent transactions in real time. This app is built with `scikit-learn` for modeling and `Streamlit` for the user interface.

🔗 **Live Demo:** [fraud-detect-app-ml.streamlit.app](https://fraud-detect-app-ml.streamlit.app/) 

---

## 🚀 Features

- 🔍 **Fraud Classification** using ML models like Logistic Regression, Random Forest, and XGBoost
- 📊 Real-time input for transaction features (amount, balance, etc.)
- ⚙️ Integrated `Pipeline` and `ColumnTransformer` for preprocessing
- 🌐 Deployed with **Streamlit Cloud**
- 📉 Visual insights using Matplotlib and Seaborn

---

## 🧠 Machine Learning Workflow

- **Data Preprocessing**: Scaling, encoding, and feature engineering
- **Model Training**: `LogisticRegression`, `RandomForestClassifier`, and `XGBClassifier`
- **Class Imbalance Handling**: `class_weight='balanced'` and threshold tuning
- **Evaluation**: Precision, recall, F1-score, confusion matrix, ROC/PR curves

---

## 🖥️ How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/Priyanshu7798/fraud_detection.git
cd fraud_detection
