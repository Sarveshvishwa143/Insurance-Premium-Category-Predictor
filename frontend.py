import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict" 

st.title("Insurance Premium Category Predictot")

st.markdown("Enter your details below: ")

age=st.number_input("Age" , min_value=10 , max_value=119 , value=30)
weight = st.number_input("Weight (Kg)" , min_value= 1.0 , max_value= 100.0)
height = st.number_input("Height (cm)" , min_value = 50 , max_value=250 , value=170)
income_lpa = st.number_input("Annual Income (LPA)" , min_value=1 , value= 10)
smoker = st.selectbox("Are you a smoker ?",options=[True , False])
city = st.selectbox(
     "city",
     [
        "Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune",
        "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
        "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
        "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
        "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
        "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
        "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
     ]
)
occupation = st.selectbox(
    "Occupation",
    ['Factory Worker', 'Businessman', 'Sales Manager', 'Banker',
       'Marketing Manager', 'Insurance Agent', 'HR Manager', 'Pharmacist',
       'Teacher', 'Software Engineer', 'Consultant', 'Driver',
       'Shop Owner', 'Nurse', 'Accountant', 'Government Employee',
       'Architect', 'Engineer', 'Real Estate Agent', 'Civil Servant',
       'Plumber', 'Retail Manager', 'Chef', 'Electrician', 'Carpenter',
       'Doctor', 'Lab Technician', 'Data Analyst', 'Lawyer',
       'Content Writer']
)


@st.dialog("📊 Prediction Result")
def show_result_popup():
    result = st.session_state.prediction_result

    st.success(f"Predicted Category: **{result['predicted_category']}**")


if st.button("Predict Premium Category"):
    
    input_data ={
        "age":age,
        "weight":weight,
        "height":height,
        "income_lpa":income_lpa,
        "smoker":smoker,
        "city" : city,
        "occupation": occupation
     }

    try:
        with st.spinner("Predicting..."):
            response = requests.post(API_URL, json=input_data)
            result = response.json()

        if response.status_code == 200:
            st.session_state.prediction_result = result
            show_result_popup()   # 🔥 trigger popup

        else:
            st.error(f"API Error: {response.status_code}")
            st.write(result)

    except requests.exceptions.ConnectionError:
        st.error("❌ FastAPI server not running")