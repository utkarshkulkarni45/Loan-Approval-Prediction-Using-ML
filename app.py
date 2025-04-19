from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Load the trained model
model_path = "loan_approval_model.pkl"
model = None
if os.path.exists(model_path):
    with open(model_path, "rb") as file:
        model = pickle.load(file)
else:
    print(f"Error: Model file not found at {model_path}")

# Load the label encoders
encoders_path = "loan_approval_encoders.pkl"
label_encoders = None
if os.path.exists(encoders_path):
    with open(encoders_path, "rb") as file:
        label_encoders = pickle.load(file)
else:
    print(f"Error: Label encoder file not found at {encoders_path}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model and label_encoders:
        # Get input data from the form
        no_of_dependents = float(request.form['no_of_dependents'])
        education = request.form['education']
        self_employed = request.form['self_employed']
        income_annum = float(request.form['income_annum'])
        loan_amount = float(request.form['loan_amount'])
        loan_term = float(request.form['loan_term'])
        cibil_score = float(request.form['cibil_score'])
        residential_assets_value = float(request.form['residential_assets_value'])
        commercial_assets_value = float(request.form['commercial_assets_value'])
        luxury_assets_value = float(request.form['luxury_assets_value'])
        bank_asset_value = float(request.form['bank_asset_value'])

        # Encode categorical features using the loaded encoders
        education_encoded = label_encoders['education'].transform([education])[0]
        self_employed_encoded = label_encoders['self_employed'].transform([self_employed])[0]

        # Create input DataFrame (order must match training features)
        input_data = pd.DataFrame({
            'no_of_dependents': [no_of_dependents],
            'education': [education_encoded],
            'self_employed': [self_employed_encoded],
            'income_annum': [income_annum],
            'loan_amount': [loan_amount],
            'loan_term': [loan_term],
            'cibil_score': [cibil_score],
            'residential_assets_value': [residential_assets_value],
            'commercial_assets_value': [commercial_assets_value],
            'luxury_assets_value': [luxury_assets_value],
            'bank_asset_value': [bank_asset_value]
        })

        # Make the prediction
        prediction = model.predict(input_data)[0]

        # Decode the prediction using the loaded loan status encoder
        predicted_class = label_encoders['loan_status'].inverse_transform([prediction])[0].strip() # Remove potential leading/trailing spaces
        result = predicted_class

        return render_template('result.html', result=result)
    else:
        return "Error: Model or encoders not loaded."

if __name__ == '__main__':
    app.run(debug=True)