# Create an app that takes two numbers as input and displays their sum.


import streamlit as slt

slt.title("Additon App !")

a = slt.number_input("Enter 1st Number : ")
b = slt.number_input("Enter 2nd Number : ")

c = a + b
if a < 0 or b < 0 :
    slt.warning("Can't Add Negative Number")
else :
    slt.success(f"Additon of {a} + {b} = {c}")