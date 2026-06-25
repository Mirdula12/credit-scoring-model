# Credit Scoring Model

## Project Overview

This project predicts whether a customer is a good or bad credit risk using Machine Learning.

The application is built using:

* Python
* Streamlit
* Scikit-learn
* Pandas

## Features

* Credit risk prediction
* Interactive Streamlit web application
* Prediction history tracking
* CSV export functionality

## Dataset

German Credit Dataset

## Machine Learning Model

Random Forest Classifier

## Project Structure

credit-scoring-model/
│
├── data/
├── models/
├── src/
├── train_model.py
├── requirements.txt
└── README.md

## Installation

Install dependencies:

pip install -r requirements.txt

## Run the Application

cd src
py -m streamlit run app.py

## Output

The model predicts whether the applicant is:

* Good Credit Risk
* Bad Credit Risk

## Future Improvements

* Add probability scores
* Deploy online
* Improve UI design
