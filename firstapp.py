import pandas as pd
import numpy as np
import streamlit as st
import pickle

model = pickle.load(open('log_tuned_model_telco_churn','rb'))

st.title("Telco Churn Project")

st.write("Please fill the required blanks!!!")

def find_churn(tenure, gender, dependents, internet_service_fiber_optic, internet_service_no, contract_one_year, contract_two_year):
	arr = np.array([tenure, gender, dependents, internet_service_fiber_optic, internet_service_no, contract_one_year, contract_two_year]).reshape((1,-1))
	churn = model.predict(arr)
	if churn == 1:
		return "Churn"
	else:
		return "Not Churn"

def main():

	gender = st.selectbox("Gender Type:", ["Female", "Male"])
	dependents = st.selectbox("Dependents:", ["Yes", "No"])
	tenure = st.number_input("Insert tenure:")
	internet_service = st.selectbox("Internet Service:", ["DSL", "Fiber optic", "No"])
	contract = st.selectbox("Contract", ["Month-to-Month", "One Year", "Two Year"])
	
	if gender == "Male":
		gender = 1
	else:
		gender = 0
	
	if dependents == "Yes":
		dependents = 1
	else:
		dependents = 0
		
	if internet_service == "DSL":
		internet_service_fiber_optic = 0
		internet_service_no = 0
	elif internet_service == "Fiber optic":
		internet_service_fiber_optic = 1
		internet_service_no = 0
	else:
		internet_service_fiber_optic = 0
		internet_service_no = 1
	
	if contract == "Month-to-Month":
		contract_one_year = 0
		contract_two_year = 0
	elif contract == "One Year":
		contract_one_year = 1
		contract_two_year = 0
	else:
		contract_one_year = 0
		contract_two_year = 1

	
	if st.button("Predict the churn"):
		output = find_churn(tenure, gender, dependents, internet_service_fiber_optic, internet_service_no, contract_one_year, contract_two_year)
		st.success(output)
	

	
if __name__=='__main__':
	main()