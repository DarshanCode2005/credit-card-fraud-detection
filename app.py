import streamlit as st
import joblib
import numpy as np

# Load your pre-trained model
model_path = 'logistic_regression_model_credit_card.joblib'  # Update this path to your model file
model = joblib.load(model_path)

# App title
st.title('Credit Card Fraud Detection')

# Input fields for the parameters
input_data = st.text_input('Enter the parameters (comma-separated):')

# Predict button
if st.button('Predict'):
    try:
        # Convert input data to numpy array
        input_data = np.array([float(i) for i in input_data.split(',')]).reshape(1, -1)
        
        # Generate prediction
        prediction = model.predict(input_data)
        
        # Display result
        if prediction[0] == 0:
            st.write('Prediction: Fraud')
        else:
            st.write('Prediction: Legitimate')
    except Exception as e:
        st.write(f'Error: {e}')
