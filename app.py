import streamlit as st # type: ignore
import pandas as pd
import joblib # type: ignore

model = joblib.load("fraud_detection_pipeline.pkl")


st.title("Fraud Detection")
st.markdown("This app predicts if a transaction is fraudulent or not.")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["CASH_OUT", "CASH_IN", "DEBIT", "PAYMENT", "TRANSFER"])

amount = st.number_input("Amount", min_value=0.0, max_value=1000000.0, value=0.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, max_value=1000000.0, value=0.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, max_value=1000000.0, value=0.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, max_value=1000000.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, max_value=1000000.0, value=0.0)

if st.button("Predict"):
  # created new data frame
  input_data = pd.DataFrame({
    "type": [transaction_type],
    "amount": [amount],
    "oldbalanceOrg": [oldbalanceOrg],
    "newbalanceOrig": [newbalanceOrig],
    "oldbalanceDest": [oldbalanceDest],
    "newbalanceDest": [newbalanceDest]
  })
  
  
  prediction = model.predict(input_data)[0]
  
  st.subheader(f"Prediction : '{int(prediction)}'")
  
  if prediction == 0:
    st.success("The transaction is not fraudulent.")
  else:
    st.error("The transaction is fraudulent.")