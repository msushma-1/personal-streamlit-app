import streamlit as st

st.title("Personal Profile App")

name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
dream_company = st.text_input("Enter your dream company")

if st.button("Submit"):

    if name and email and dream_company:

        st.success(f"Hello {name}")

        st.write("Email:")
        st.write(email)

        st.write("Dream Company:")
        st.write(dream_company)

    else:

        st.error("Please fill all fields")

st.write("---")
st.caption("Created by Sushma Mundlamuri")


