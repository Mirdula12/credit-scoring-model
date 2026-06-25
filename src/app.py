# import streamlit as st
# import pandas as pd
# import pickle

# # Load trained model
# model = pickle.load(open("../models/credit_scoring_model.pkl", "rb"))

# st.set_page_config(page_title="Credit Scoring App")

# st.title("Credit Scoring Model")

# st.write("Predict whether a customer is a good or bad credit risk.")

# st.sidebar.header("Applicant Details")

# # User Inputs
# age = st.sidebar.slider("Age", 18, 100, 30)

# credit_amount = st.sidebar.number_input("Credit Amount", 0, 50000, 5000)

# duration = st.sidebar.slider("Loan Duration (Months)", 1, 72, 12)

# # Dummy dataframe matching training structure
# input_data = pd.DataFrame({
#     "Age": [age],
#     "Credit amount": [credit_amount],
#     "Duration": [duration]
# })

# # Add missing columns
# training_columns = model.feature_names_in_

# for col in training_columns:
#     if col not in input_data.columns:
#         input_data[col] = 0

# input_data = input_data[training_columns]

# # Prediction
# if st.button("Predict Credit Risk"):

#     prediction = model.predict(input_data)[0]

#     if prediction == 1:
#         st.success("Good Credit Risk")
#     else:
#         st.error("Bad Credit Risk")



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

    if prediction == 1:
        result = "Good Credit Risk"
        st.success(
            f"{result} - Confidence: {probability:.2%}"
        )

    else:
        result = "Bad Credit Risk"
        # st.error(
        #     f"{result} - Confidence: {(1 - probability):.2%}"
        # )

    # Save History
    st.session_state.history.append({
        "Age": age,
        "Credit Amount": credit_amount,
        "Duration": duration,
        "Prediction": result
    })

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



    # cd src
    # py -m streamlit run app.py