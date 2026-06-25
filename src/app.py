import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("../models/credit_scoring_model.pkl", "rb"))

# Page Config
st.set_page_config(
    page_title="Credit Scoring App",
    layout="centered"
)

# Title
st.title("Credit Scoring Model")

st.write("Predict whether a customer is a good or bad credit risk.")

# Initialize History
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar Inputs
st.sidebar.header("Applicant Details")

age = st.sidebar.slider(
    "Age",
    18,
    100,
    30
)

credit_amount = st.sidebar.number_input(
    "Credit Amount",
    min_value=0,
    max_value=50000,
    value=5000
)

duration = st.sidebar.slider(
    "Loan Duration (Months)",
    1,
    72,
    12
)

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Age", age)

col2.metric("Credit Amount", credit_amount)

col3.metric("Duration", duration)

# Input Data
input_data = pd.DataFrame({
    "Age": [age],
    "Credit amount": [credit_amount],
    "Duration": [duration]
})

# Match Training Columns
training_columns = model.feature_names_in_

for col in training_columns:
    if col not in input_data.columns:
        input_data[col] = 0

input_data = input_data[training_columns]

# Prediction
if st.button("Predict Credit Risk"):

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    # Prediction Result
    if prediction == 1:
        result = "Good Credit Risk"

        st.success(result)

    else:
        result = " Bad Credit Risk"

        st.error(result)

    # Check Duplicate Entry
    duplicate_found = False

    for item in st.session_state.history:

        if (
            item["Age"] == age and
            item["Credit Amount"] == credit_amount and
            item["Duration"] == duration
        ):

            duplicate_found = True
            break

    # If Duplicate
    if duplicate_found:

        st.warning(
            "⚠️ Entered already in history"
        )

    # Save New Entry
    else:

        st.session_state.history.append({
            "Age": age,
            "Credit Amount": credit_amount,
            "Duration": duration,
            "Prediction": result
        })

        st.success("Added to history")

# Show History
if st.session_state.history:

    st.subheader("Prediction History")

    for index, item in enumerate(st.session_state.history):

        col1, col2, col3, col4, col5 = st.columns(
            [1, 2, 2, 2, 1]
        )

        col1.write(item["Age"])

        col2.write(item["Credit Amount"])

        col3.write(item["Duration"])

        col4.write(item["Prediction"])

        # Delete Button
        if col5.button("🗑", key=index):

            st.session_state.history.pop(index)

            st.rerun()

    # Download CSV
    history_df = pd.DataFrame(
        st.session_state.history
    )

    csv = history_df.to_csv(index=False)

    st.download_button(
        label="Download History CSV",
        data=csv,
        file_name="prediction_history.csv",
        mime="text/csv"
    )

# Clear Entire History
if st.button("Clear Entire History"):

    st.session_state.history = []

    st.rerun()

# Footer
st.markdown("---")

st.caption(
    "Developed using Streamlit & Machine Learning"
)