import streamlit as st

st.title("Application Form")
st.header("Personal Information")

col1, col2 = st.columns(2)

with col1:
    st.text_input("First Name")

with col2:
    st.text_input("Last Name")

st.text_input("E-mail")

phone = st.text_input("Enter your phone number")

if phone:
    if phone.isdigit() and len(phone) == 10:
        st.success("Valid phone number")
    else:
        st.error("Invalid phone number (Enter 10 digits only)")

st.radio("Gender", ["Male", "Female", "Other"])
st.text_area("Address")
st.date_input("Date Of Birth")

st.header("Academic Information")
st.text_input("Name of College")
st.number_input("CGPA")
st.selectbox("Course", ["CSE", "AIML", "DS", "CS", "EEE", "ECE", "IT"])

st.button("Submit")