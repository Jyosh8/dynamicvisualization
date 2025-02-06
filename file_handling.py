# file_handling.py
import pandas as pd
import streamlit as st

def download_template():
    """Provide a download link for the template."""
    st.write("Download the template here.")
    # You can implement the download functionality here

def upload_file():
    """Handle file upload and return the data."""
    uploaded_file = st.file_uploader("Upload your risk data file", type=["csv", "xlsx"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            data = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file type. Please upload a CSV or Excel file.")
            return None
        return data
    return None
