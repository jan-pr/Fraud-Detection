
# 🧠 ML Model Deployment with Flask 

This repository contains a Flask web application for serving predictions using a trained machine learning model. The model, encoders, and preprocessed data are stored in a compressed archive (`training.7z`) and tracked using **Git LFS** due to GitHub's file size limitations.

---

## 📁 Project Structure

```
Fraud-Detection/
├── data/
│   └── online_fraud_detection.txt           # Link to the training dataset
├── flask/
│   ├── app.py                     # Main Flask application
│   ├── model.txt                  # Contains drive link with model, encoders, and training data in training folder
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

### 2. Run the Flask App

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

## 📦 Model & Training Files (Alternative Download)

Due to Git LFS issues or quota limits, you can alternatively download the required model, encoders, and preprocessed data manually.

- Inside the `flask/` folder, you'll find a file named [`model.txt`](flask/model.txt)
- This file contains a **Google Drive link** to a folder named `training/`
- The `training/` folder includes:
  - Trained ML model
  - Encoders and preprocessing artifacts
  - Input data files

🔽 **Please download and extract the contents of the Drive folder into your local `flask/training/` directory** before running the app.
