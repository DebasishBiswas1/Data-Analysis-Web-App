import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

# Title

st.title("Data Analysis")
st.subheader("data analysis using python and streamlit")

# Upload dataset

upload = st.file_uploader("Upload your file(In CSV format)")
if upload is not None:
    data=pd.read_csv(upload)

# Show checkbox

if upload is not None:
    if st.checkbox("Preview"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

# Show datatypes
if upload is not None:
    if st.checkbox("Datatypes"):
        st.write(data.dtypes)

# Show shape of the dataset (Number of rows and columns)
if upload is not None:
    data_shape=st.radio("What shape you want to see?",('rows','columns'))

    if data_shape=='rows':
        st.write("No of rows: ")
        st.write(data.shape[0])
    if data_shape=='columns':
        st.write("No of columns: ")
        st.write(data.shape[1])

# Check null values
if upload is not None:
    test=data.isnull().any().any()
    if test==True:
        if st.checkbox("Check for null values"):
            sns.heatmap(data.isnull(), cmap='viridis')
            plt.xticks(rotation=90)
            plt.tight_layout()
            st.pyplot()
    else:
        st.success("No null values")

# Check for duplicate values
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("Dataset contains duplicate values !")
        dup=st.selectbox("Do you want to remove duplicate values ?",("Select One",'Yes','No'))
        if dup=='Yes':
            data=data.drop_duplicates()
            st.success("Duplicate values dropped successfully !")
        if dup=='No':
            st.text("No problem.")
    else:
        st.success("Data set has no duplicate values !")

# Get overall statistics
if upload is not None:
    if st.checkbox("Get overall statistics"):
        st.write(data.describe(include='all'))

# About section
if st.button("About App"):
    st.write("Built with streamlit")

# By
if st.checkbox("By"):
    st.success("Debasish Biswas")