import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dasboard")
upload_file = st.file_uploader("Upload a CSV file here!", type="csv")

if upload_file is not None: 
    df = pd.read_csv(upload_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.to_list()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique() 
    selected_value = st.selectbox("Select value", unique_values)
    filter_df = df[df[selected_column]==selected_value]
    st.write(filter_df)

    st.subheader("Plot Data")
    x_axis_colum = st.selectbox("X-axis column",columns)
    y_axis_colum = st.selectbox("y-axis column",columns)

    if st.button("Generate a chart"):
        st.line_chart(filter_df.set_index(x_axis_colum)[y_axis_colum])

else: 
    st.write("waiting for file upload!")