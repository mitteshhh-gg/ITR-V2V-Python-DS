import streamlit as slt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

slt.title("My 2nd Streamlit App")
slt.write("# Charts")

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns= ["a","b","c"]
)
if slt.button("Show Bar Chart"):
    slt.bar_chart(chart_data)
if slt.button("Show Line Chart"):
    slt.line_chart(chart_data)
    