'''Create a Streamlit Dashboard that uploads a CSV dataset
and displays summary statistics, missing values, and 
interactive visualizations. '''

import streamlit as slt
import pandas as pd

slt.title("CSV Data Dashboard")     

slt.subheader("Upload your CSV file ")
file = slt.file_uploader("Upload your CSV file",type= "CSV")        # Takes the CSV file as input

if file is not None:
    df = pd.read_csv(file)
    slt.write("Dataframe : ")
    slt.dataframe(df)

    slt.subheader("Summary : ")
    slt.write(df.describe())

    slt.subheader("Missing Values : ")
    slt.write(df.isnull().sum())

    slt.subheader("Interactive Visualizations")
    column = slt.selectbox("Select a column for visualization", df.columns)     # Seletbox to select a column for visualization
    
    if column:
        slt.bar_chart(df[column].value_counts())
