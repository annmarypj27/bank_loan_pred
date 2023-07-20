# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st





#loaded model
loaded_model=pickle.load(open('C:/Users/hp/Downloads/model_saved','rb'))

def loan_prediction(input_data):
 Gender, Married, Dependents, Education, Self_Employed = int(input_data[0]), int(input_data[1]), float(input_data[2]), int(input_data[3]), int(input_data[4])
 ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area = float(input_data[5]), float(input_data[6]), float(input_data[7]), float(input_data[8]), float(input_data[9]), int(input_data[10])
 
 #input_data=(1,0,0.0,0,0,5849,0.0,120.0,360.0,1.0,2)
 input_data_as_numpy_array = np.asarray([Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area])

 input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
 prediction=loaded_model.predict(input_data_reshaped)
 print(prediction)
 if (prediction[0] == 1):
   return 'The loan has approved '
 else:
   return 'The loan has not approved'


def main():
   st.title('APPROVAL OF LOAN')

   Gender = st.selectbox('Gender', ['Male', 'Female'])
   
   if Gender == 'Male':
    Gender = 1
   else:
    Gender = 0

   st.write(Gender)
   Married=st.selectbox('Married', ['yes','no'])
   if Married == 'yes':
    Married = 1
   else:
    Married = 0

   st.write(Married)
   
   Dependents=st.text_input('applicant has any dependents or not')
   Education=st.selectbox('applicant is Graduate or not Graduate',['Graduate','not Graduate'])
   if Education== 'Graduate':
     Education=0
   else:
     Education=1
   st.write(Education)
   Self_Employed=st.selectbox('applicant is self-employed i.e. Yes/ No',['yes','no'])
   if Self_Employed=='Yes':
     Self_Employed=0
   else:
     Self_Employed=1
   st.write(Self_Employed)
   ApplicantIncome=st.text_input('Applicant income')
   CoapplicantIncome=st.text_input('Co-applicant income')
   LoanAmount=st.text_input('Loan amount (in thousands)')
   Loan_Amount_Term=st.text_input('Terms of loan (in months)')
   Credit_History=st.text_input('Credit history of individual’s repayment of their debts')
   Property_Area=st.selectbox('Area of property i.e. Rural/Urban/Semi-urban ',['Rural','Urban','semiurban'])
   if Property_Area=='Rural':
    Property_Area=0
   elif Property_Area=='Urban':
    Property_Area=1
   else:
     Property_Area=2
   st.write(Property_Area)

   loan  = ''

   if st.button('loan prediction approve or not'):
     loan = loan_prediction([Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area])
     st.success(loan)


if __name__ == '__main__':
  main()

