import streamlit as slt
import pandas as pd
import matplotlib.pyplot as plt

slt.title("Data Visualization App")
slt.write("Upload a CSV file.")

file = slt.file_uploader("Choose a CSV file", type="CSV")

if file is not None:
    df = pd.read_csv(file)
    slt.success("CSV Uploaded Successfully!")

    if slt.checkbox("Show Dataset"):
        slt.dataframe(df)

    # Select chart type
    chart = slt.selectbox(
        "Select Chart Type",
        ["Bar Chart", "Line Chart", "Scatter Plot", "Histogram", "Pie Chart"]
    )

    columns = df.columns.tolist()
    numCol = df.select_dtypes(include='number').columns
    fig, ax = plt.subplots()

    # Bar Chart
    if chart == "Bar Chart":
        col = slt.selectbox("Select the Column : ", columns)
        slt.bar_chart(df[col].value_counts())
    
    # Line Chart
    elif chart == "Line Chart":
        col = slt.selectbox("Select the Column : ", columns)
        slt.line_chart(df[col].value_counts())
    
    # Scatter Plot
    elif chart == "Scatter Plot":
        x = slt.selectbox("Select X-axis", numCol)
        y = slt.selectbox("Select Y-axis", numCol)

        ax.scatter(df[x], df[y])
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        slt.pyplot(fig)

    # Histogram
    elif chart == "Histogram":

        col = slt.selectbox("Select Numeric Column",numCol)

        ax.hist(df[col],
                color = "pink", 
                edgecolor = "black", 
                linewidth = 2, 
        )
        ax.set_title("Histogram")
        ax.set_xlabel(col)
        slt.pyplot(fig)

    # Pie Chart
    elif chart == "Pie Chart":

        col = slt.selectbox("Select Category", columns)
        pie_data = df[col].value_counts().head(10)

        fig, ax = plt.subplots()

        ax.pie(
            pie_data,
            labels=pie_data.index,                                                                                                                                  # type: ignore
            autopct="%1.1f%%",
            startangle=90
        )

        ax.set_title(f"Top 10 {col}")
        slt.pyplot(fig)

