from flask import Flask, render_template, request
import pickle
import numpy as np
import time


from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load the trained model
with open('etc_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the encoders
with open('nameOrig_encoder.pkl', 'rb') as f:
    nameOrig_encoder = pickle.load(f)

with open('nameDest_encoder.pkl', 'rb') as f:
    nameDest_encoder = pickle.load(f)

# OPTIONAL: Load dataset (required to compute accuracy & data point count dynamically)
# Replace 'your_dataset.pkl' with actual dataset if available
with open('X_data.pkl', 'rb') as f:
    X = pickle.load(f)

with open('y_data.pkl', 'rb') as f:
    y = pickle.load(f)

# Split data to compute accuracy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

@app.route("/")
@app.route("/home")
def about():
    return render_template('home.html')

@app.route("/predict")
def predict_form():
    return render_template('predict.html')

@app.route("/pred", methods=["POST"])
def predict():
    try:
        start_time = time.time()

        # Extract form data
        step = float(request.form['step'])
        type_val = request.form['type']
        amount = float(request.form['amount'])
        nameOrig = request.form['nameOrig']
        oldbalanceOrg = float(request.form['oldbalanceOrg'])
        newbalanceOrig = float(request.form['newbalanceOrig'])
        nameDest = request.form['nameDest']
        oldbalanceDest = float(request.form['oldbalanceDest'])
        newbalanceDest = float(request.form['newbalanceDest'])

        # Encode 'type'
        type_map = {'PAYMENT': 0, 'TRANSFER': 1, 'CASH_OUT': 2, 'DEBIT': 3, 'CASH_IN': 4}
        type_encoded = type_map.get(type_val, -1)

        # Encode nameOrig
        if nameOrig not in nameOrig_encoder.classes_:
            nameOrig_encoder.classes_ = np.append(nameOrig_encoder.classes_, nameOrig)
        encoded_nameOrig = nameOrig_encoder.transform([nameOrig])[0]

        # Encode nameDest
        if nameDest not in nameDest_encoder.classes_:
            nameDest_encoder.classes_ = np.append(nameDest_encoder.classes_, nameDest)
        encoded_nameDest = nameDest_encoder.transform([nameDest])[0]

        # Final input vector
        features = [[
            step, type_encoded, amount, encoded_nameOrig,
            oldbalanceOrg, newbalanceOrig, encoded_nameDest,
            oldbalanceDest, newbalanceDest
        ]]

        x = np.array(features)

        # Prediction
        pred = model.predict(x)[0]
        confidence = round(np.max(model.predict_proba(x)) * 100, 2)
        prediction_text = "Fraud Detected" if pred == 1 else "Payment Secure"

        end_time = time.time()
        processing_time = round(end_time - start_time, 3)

        # Evaluate model accuracy on test set
        y_pred = model.predict(X_test)
        accuracy = round(accuracy_score(y_test, y_pred) * 100, 2)

        return render_template("submit.html",
            prediction_text=prediction_text,
            confidence=confidence,
            nameOrig=nameOrig,
            nameDest=nameDest,
            accuracy=accuracy,
            processing_time=processing_time,
            data_points=X_train.shape[0],
            algorithm_name="ETC"
        )

    except Exception as e:
        return f"Error during prediction: {e}"

if __name__ == "__main__":
    app.run(debug=True)
