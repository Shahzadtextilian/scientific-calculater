import streamlit as st
import math

# Function to handle scientific operations
def calculate(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {str(e)}"

# Title of the app
st.title("Scientific Calculator")

# Sidebar for options
st.sidebar.header("Scientific Calculator")

# Input for mathematical expression
expression = st.text_input("Enter a mathematical expression", "")

# Display the result if an expression is entered
if expression:
    result = calculate(expression)
    st.write(f"**Result:** {result}")

# Providing predefined options for basic scientific functions
st.header("Scientific Functions")

# Sine, Cosine, Tangent
angle = st.number_input("Enter angle in degrees", value=0.0)
radians = math.radians(angle)  # Convert to radians for trigonometric functions

# Display trigonometric values
st.write(f"Sine({angle}°) = {math.sin(radians)}")
st.write(f"Cosine({angle}°) = {math.cos(radians)}")
st.write(f"Tangent({angle}°) = {math.tan(radians)}")

# Square Root
number = st.number_input("Enter a number to calculate the square root", min_value=0.0)
if number >= 0:
    st.write(f"Square Root of {number} = {math.sqrt(number)}")
else:
    st.write("Please enter a non-negative number for the square root.")

# Logarithms (natural log and base 10)
log_value = st.number_input("Enter a number to calculate its logarithm", min_value=0.0)
if log_value > 0:
    st.write(f"Natural Log (ln) of {log_value} = {math.log(log_value)}")
    st.write(f"Logarithm base 10 of {log_value} = {math.log10(log_value)}")
else:
    st.write("Please enter a positive number for the logarithm.")

# Power operation
base = st.number_input("Enter the base number", value=0.0)
exponent = st.number_input("Enter the exponent", value=0.0)
st.write(f"{base} raised to the power of {exponent} = {math.pow(base, exponent)}")

# Pi and e constants
st.write(f"Value of Pi = {math.pi}")
st.write(f"Value of e (Euler's number) = {math.e}")
