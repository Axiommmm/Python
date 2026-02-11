import streamlit as st

def ControlBdindex(bdindex : float):
    if(bdindex > 30.0):
        return "Obese"
    elif(bdindex > 25.0):
        return "Overweight"        
    elif(bdindex > 18.5):
        return "Normal"        
    else:
        return "Underweight"        
st.title("Body Mass Index App")
weight = st.number_input("Enter your weight in kg: ")
height = st.number_input("Enter your height im meter: ")
if st.button("Calculate"):
    bdindex = weight/height**2
    st.write("Your body mass index:", bdindex)
    st.write("You are", ControlBdindex(bdindex))
