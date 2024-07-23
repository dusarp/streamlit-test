import streamlit as st
import pandas as pd
st.header('Visualize Data!')
st.subheader('Please upload your csv file')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(5))
    st.subheader('Select the columns you want to plot aginst each other in a scatter plot')
    columns = df.columns.tolist()
    column1 = st.selectbox('Select column 1', columns)
    column2 = st.selectbox('Select column 2', columns)
    st.write(f'scatter plot of {column1} vs {column2}')
    st.scatter_chart(df, x=column1, y=column2)