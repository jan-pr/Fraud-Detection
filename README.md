# 🧠 ML Model Deployment with Flask + Git LFS

This repository contains a Flask web application for serving predictions using a trained machine learning model. The model, encoders, and preprocessed data are stored in a compressed archive (`training.7z`) and tracked using **Git LFS** due to GitHub's file size limitations.

---

## 📁 Project Structure

```
Fraud-Detection/
├── data/
│   └── online_fraud_detection.txt           # Link to the training dataset
├── flask/
│   ├── app.py                     # Main Flask application
│   ├── training.7z                # Contains model, encoders, and training data
│   ├── templates/                 # HTML templates for Flask
│   │   └── *.html
```

---

## 🔗 Dataset

The dataset used for training is referenced in:  
`data/online_fraud_detection.txt`

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/jan-pr/Fraud-Detection.git
cd Fraud-Detection
```

---

### 2. Install Git LFS (Only Once)

```bash
git lfs install
git lfs pull
```

> If Git LFS isn't installed, get it from https://git-lfs.com/

---

### 3. Extract the Model Archive

```bash
7z x training.7z
```

This will extract:
- `etc_model.pkl` – Trained ML model
- `nameOrig_encoder.pkl`, `nameDest_encoder.pkl` – Preprocessing encoders
- `X_data.pkl`, `y_data.pkl` – Preprocessed training data

---

### 4. Install Required Python Packages

> *(Make sure you’re in the `flask/` directory)*

```bash
python -m venv venv
# Activate environment
venv\Scripts\activate     # on Windows
source venv/bin/activate  # on Linux/macOS

### 5. Run the Flask App

```bash
python app.py
```

The app should be accessible at:  
👉 http://127.0.0.1:5000/

---

## 💡 Notes

- The app uses the `templates/` folder to serve HTML pages (Jinja2 templates).
- The `training.7z` archive is stored with Git LFS. Make sure you’ve installed and pulled it before running the app.
- You will get a warning if you near GitHub's free LFS limits. GitHub **will not charge** you unless you manually purchase more space.

---
