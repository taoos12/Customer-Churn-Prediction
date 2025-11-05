import numpy as np
import pickle
import streamlit as st


model = pickle.load(open("C:/Practices/Projects/Customer Churn Prediction/model/model.pkl", 'rb'))

def customer_churn(input):
    input_to_arr = np.asarray(input)
    reshaped_inp = input_to_arr.reshape(1, -1)
    prediction = model.predict(reshaped_inp)

    return "No, The customer is not going to churn" if 0 else "Yes"

def main():
    st.title("Churn Prediction")

    # customerID,gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges,    



    inputs = ['gender','SeniorCitizen','Partner','Dependents','tenure','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','MonthlyCharges','TotalCharges']
    
    # binary_inps = ['gender','SeniorCitizen','Partner','PhoneService']
    # tri_inps = ['MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract']
    # paper_billing =  'PaperlessBilling'
    input_taken = []

    for col in inputs:
        value = st.number_input(f"Enter {col}")
        input_taken.append(value)

    result = ''
    if(st.button("Predict")):
        result = customer_churn(input_taken)
        st.success(result)
    

if __name__ == "__main__":
    main()