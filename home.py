import streamlit as st
import pandas as pd

def upload_and_preview_data():
    uploaded_file = st.file_uploader("Choose a file (CSV or Excel)", key="file_uploader", type=["csv","xlsx"])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            return df
        except Exception as e:
            st.error(f"Error: {str(e)}")
            return None
    return None

def home_page():
    st.write("# Welcome to Insightful Data Explorer! 📊")
    st.markdown('''
    This application helps you analyze and visualize your data efficiently.
    
    ### Features:
    - Upload and preview your data
    - Chat with your data using natural language
    - Edit and clean your dataset
    - Generate comprehensive data profiles
    - Create interactive visualizations
    - Perform feature engineering
    - Build machine learning models automatically
    
    ### Get Started:
    Upload your data file (CSV or Excel) below to begin your analysis journey!
    ''')
    
    df = upload_and_preview_data()
    if df is not None:
        st.write("### Preview of your data:")
        st.dataframe(df.head())
        st.write(f"Dataset Shape: {df.shape[0]} rows and {df.shape[1]} columns")
    