import pickle
import streamlit as st

with open('loan_predictor.pkl', 'rb') as pkl:
    train_model = pickle.load(pkl)


def predict(gender, married, dependent, education, self_employed, applicant_income,
            coApplicantIncome, loanAmount, loan_amount_term, creditHistory, propertyArea):
    print("hitting")
    # processing user input
    Gender_Female = 1 if gender == 'Female' else 0
    Gender_Male = 1 if gender == 'Male' else 0
    Married_No = 1 if gender == 'No' else 0
    Married_Yes = 1 if married == 'Yes' else 0
    Education_Graduate = 1 if education == 'Graduate' else 0
    Education_NotGraduate = 1 if education == 'Not Graduate' else 0

    Self_Employed_No = 1 if self_employed == 'No' else 0
    Self_Employed_Yes = 1 if self_employed == 'Yes' else 0
    if(dependent == "None"):
        dep = 0
    elif(dependent == "One"):
        dep = 1 
    elif(dependent == "Two"):
        dep = 2
    else:
        dep = 3         
    if (propertyArea == 'Rural'):
        Property_Area_Rural = 1
        Property_Area_Semiurban = 0
        Property_Area_Urban = 0
    if (propertyArea == 'Urban'):
        Property_Area_Rural = 0
        Property_Area_Semiurban = 0
        Property_Area_Urban = 1

    if (propertyArea == 'Semiurban'):
        Property_Area_Rural = 0
        Property_Area_Semiurban = 1
        Property_Area_Urban = 0

    # making predictions
    prediction = train_model.predict([[Gender_Female, Gender_Male, Married_Yes, Married_No, dep, Education_Graduate, Education_NotGraduate, Self_Employed_No, Self_Employed_Yes, applicant_income, coApplicantIncome,
                                       loanAmount, loan_amount_term, creditHistory, Property_Area_Rural, Property_Area_Semiurban, Property_Area_Urban]])
    print(Gender_Female, Gender_Male, Married_Yes, Married_No, dep, Education_Graduate, Education_NotGraduate, Self_Employed_No, Self_Employed_Yes, applicant_income, coApplicantIncome,
                                       loanAmount, loan_amount_term, creditHistory, Property_Area_Rural, Property_Area_Semiurban, Property_Area_Urban)
    print(prediction)
    verdict = 'Not Eligible' if prediction == 0 else 'Eligible'
    return verdict


def main():
    bg = """<div style='background-color:black; padding:13px'>
              <h1 style='color:white'>Streamlit Loan Elgibility Prediction App</h1>
       </div>"""
    st.markdown(bg, unsafe_allow_html=True)

    left, right = st.columns((2, 2))
    gender = left.selectbox('Gender', ('Male', 'Female'))
    married = right.selectbox('Married', ('Yes', 'No'))
    dependent = left.selectbox('Dependents', ('None', 'One', 'Two', 'Three'))
    education = right.selectbox('Education', ('Graduate', 'Not Graduate'))
    self_employed = left.selectbox('Self-Employed', ('Yes', 'No'))
    applicant_income = right.number_input('Applicant Income')
    coApplicantIncome = left.number_input('Coapplicant Income')
    loanAmount = right.number_input('Loan Amount')
    loan_amount_term = left.number_input('Loan Tenor (in months)')
    creditHistory = right.number_input('Credit History', 0.0, 1.0)
    propertyArea = st.selectbox(
        'Property Area', ('Semiurban', 'Urban', 'Rural'))
    button = st.button('Predict')

    # if button is clicked
    if button:

        # make prediction
        result = predict(gender, married, dependent, education, self_employed, applicant_income,
                         coApplicantIncome, loanAmount, loan_amount_term, creditHistory, propertyArea)
        st.success(f'You are {result} for the loan')


main()
