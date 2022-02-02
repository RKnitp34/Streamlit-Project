from re import S
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
#1 .Title and Subheader
st.title('Data Analysis')
st.subheader('Data Analysis with Python')
# streamlit run main.py --global.dataFrameSerialization legacy

#2 Upload Dataset
upload =st.file_uploader("Upload Your Dataset(In csv Format)")
if upload is not None:
    df =pd.read_csv(upload)

#3 Show Dataset
if upload is not None:
    if st.checkbox('Preview Dataset'):
        if st.button("Head"):
            st.write(df.head())
        if st.button("Tail"):
            st.write(df.tail())

#4 Check Datatype of Each Column
if upload is not None:
    if st.checkbox("Data type of each column"):
        st.text("Datatypes")
        st.write(df.dtypes)
           
#5 Find Shape of Our Dataset (Number of Rows And Number of Columns)
if upload is not None:
    if st.checkbox('Number of Rows OR Columns'):
        data_shape = st.radio("Rows or Columns",('Rows','Columns'))
        if(data_shape=='Rows'):
            st.text('Rows')
            st.write(df.shape[0])
        if(data_shape=='Columns'):
            st.text('Columns')
            st.write(df.shape[1])
# 7.Find Null Values in the Dataset
if upload is not None:
    if st.checkbox('Check Null Values'):
        test = df.isnull().values.any()
        if test==True:
            bt =st.radio('Select which you want to showValues OR Heatmap' , ('Values' , 'Heatmap') )
            if(bt=='Values'):
                st.write(df.isnull().sum())
            if(bt=='Heatmap'):
                sns.heatmap(df.isnull())
                st.pyplot()
        else: 
            st.success("Congratulations!!! , No Missing Values")
#8 . Duplicates value in Dataset 
if upload is not None:
    if st.checkbox('Duplicates Value'):
        test = df.duplicated().any()
        if test==True:
            st.warning("This Dataset Contains Some Duplicate Values")
            dup =st.selectbox('Do You Want to Remove Duplicate Value?' , ('Select One',"Yes","No"))
            if dup=="Yes":
                df =df.drop_duplicates()
                st.text("Duplicates Values are Removed")
            if dup=='No':
                st.text('Ok No Problem')
        else:st.success("No Duplicates are Found")
#9 Overall Statics
if upload is not None:
    if st.checkbox('Overall Statics'):
        st.write(df.describe())

#10 About Section
if st.button("About App"):
    st.text('Built With Streamlit')
    st.text("Thanks To Streamlit")

#11 By
if st.button("By"):
    st.text("Rakesh Kumar")

# streamlit run main.py --global.dataFrameSerialization legacy
# if upload is not None:
#     if st.     
# streamlit run app.py