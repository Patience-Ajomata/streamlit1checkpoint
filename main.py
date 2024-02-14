
import streamlit as st
import pypickle
import pandas as pd


# Define the features
features = ['REGION', 'TENURE', 'MONTANT', 'FREQUENCE_RECH', 'REVENUE',
            'ARPU_SEGMENT', 'FREQUENCE',
            'DATA_VOLUME', 'ON_NET', 'ORANGE', 'TIGO', 'ZONE1', 'ZONE2', 'MRG',
            'REGULARITY', 'TOP_PACK', 'FREQ_TOP_PACK']

# Create a Streamlit app
st.title('Churn Prediction App')

# Add input fields for each feature
input_data = {}
for feature in features:
    input_data[feature] = st.number_input(feature)

# Add a validation button
if st.button('Validate'):
    # Load and train model
    model = pypickle.load('model (1).pkl')

    # Convert input data to a DataFrame
    input_df = pd.DataFrame([input_data])

    # Make a prediction
    prediction = model.predict(input_df)[0]

    # Display the prediction
    if prediction == 0:
        st.write('Client is not likely to churn.')
    else:
        st.write('Client is likely to churn.')
