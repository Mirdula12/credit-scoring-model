import streamlit as st

st.title("Credit Scoring Model")

st.write("Predict whether a loan applicant is creditworthy.")

# User Inputs
age = st.number_input("Enter Age", min_value=18, max_value=100)

credit_amount = st.number_input("Enter Credit Amount", min_value=0)

duration = st.number_input("Enter Loan Duration (Months)", min_value=1)

# Prediction Button
if st.button("Predict"):

    if age > 25 and credit_amount < 5000:
        st.success("Good Credit Risk")

    else:
        st.error("Bad Credit Risk")