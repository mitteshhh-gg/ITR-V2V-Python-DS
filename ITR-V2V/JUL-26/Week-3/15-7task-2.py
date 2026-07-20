# Create a Streamlit app that asks the user to enter their name and displays a greeting.

import streamlit as slt

slt.title("Welcome to Streamlit App")

name = slt.text_input("Enter your name ")

if slt.button("SUBMIT"):
    slt.success(f"Welcome {name} !")