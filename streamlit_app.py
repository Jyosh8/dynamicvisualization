import streamlit as st
import pandas as pd
from file_handling import download_template, upload_file
from visualization import prepare_visualization
# ✅ Set the page config FIRST before any other Streamlit commands
st.set_page_config(layout="wide")

def main():
    st.sidebar.title("Navigation")
    menu = ["Home", "Risk"]
    choice = st.sidebar.radio("Go to", menu)

    if choice == "Home":
        st.title("Welcome to the Risk Management App")
        st.write("Use the sidebar to navigate to different sections.")
    elif choice == "Risk":
        st.title("Risk Data Management")

        # Download the template
        download_template()

        # Upload the file
        uploaded_data = upload_file()

        # Check if data is uploaded
        if uploaded_data is not None:
            st.write("### Data Preview")
            st.dataframe(uploaded_data)

            # Prepare visualization using Plotly
            st.write("### Visualization")
            st.write("Click the button below to open the risk dashboard visualization.")

            if st.button("Show Risk Dashboard"):
                # Prepare Plotly visualizations
                table_fig, combined_fig = prepare_visualization(uploaded_data)

                # Display the charts
                st.plotly_chart(table_fig)
                st.plotly_chart(combined_fig)
        else:
            st.info("Please upload a risk data file.")

if __name__ == "__main__":
    main()
