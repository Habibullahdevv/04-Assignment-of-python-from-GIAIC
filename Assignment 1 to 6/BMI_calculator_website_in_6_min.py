import streamlit as st

st.title("BMI Calculator")

user_weight = st.number_input("Enter your weight (kg)", min_value=0.0)
user_height = st.number_input("Enter your height (m)", min_value=0.0)

if st.button("Calculate BMI"):
    if user_height > 0:
        bmi_result = user_weight / (user_height ** 2)
        st.success(f"Your BMI is: {bmi_result:.2f}")
    else:
        st.error("Height must be greater than zero.")
