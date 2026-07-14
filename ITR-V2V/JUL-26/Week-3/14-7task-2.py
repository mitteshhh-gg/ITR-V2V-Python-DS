import streamlit as slt

slt.title("My 1st Streamlit App")

name = slt.text_input("Enter your name : ")
if slt.button("SUBMIT"):
    slt.success(f"Welcome {name} !")  