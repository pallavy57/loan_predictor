import streamlit as st
import pandas as pd
import numpy as np
import pickle

file1 = open('loan_predictor.pkl', 'rb')
rf = pickle.load(file1)
file1.close()

data = pd.read_csv("trainedData.csv")
st.title("Loan Prediction App")


# gender_options = {
#     1.0: "Data Scientist",
#     0.0: "Data Science Engineer",
# }