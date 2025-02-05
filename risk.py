import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_template():
    """Function to provide a downloadable risk template."""
    with open("data/risk.xlsx", "rb") as file:
        st.download_button(
            label="Download Risk Template",
            data=file,
            file_name="risk.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

def process_uploaded_file():
    """Function to handle file upload and store it for visualization."""
    uploaded_file = st.file_uploader("Upload Risk Data", type=['xlsx'])
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.session_state['uploaded_risk_data'] = df
        st.success("File uploaded successfully!")
        return df
    elif 'uploaded_risk_data' in st.session_state:
        # Clear the session state if the file is canceled
        del st.session_state['uploaded_risk_data']
        st.info("Upload canceled. Please upload a new file to visualize the data.")
    return None


def display_metrics(df):
    """Display key metrics in a single row at the top."""
    if df is None:
        return
    
    # Calculate metrics
    total_risks = len(df)  # Total number of risks
    open_risks = df[df["Status"] == "Open"].shape[0]  # Count of open risks
    atr_provided = df[df["ATR Date"].notna()].shape[0]  # Count of ATR provided
    priority_risks = df["Priority"].value_counts().to_dict()  # Count of risks by priority
    
    # Display metrics in a single row with borders
    st.markdown('<div class="metric-box">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"**Total Risks:** {total_risks}")
    
    with col2:
        st.markdown(f"**Open Risks:** {open_risks}")
    
    with col3:
        st.markdown(f"**ATR Provided:** {atr_provided}")
    
    with col4:
        st.markdown("**Priority Risks:**")
        for priority, count in priority_risks.items():
            st.markdown(f"- {priority}: {count}")
    
    st.markdown('</div>', unsafe_allow_html=True)

def display_bar_chart(df):
    """Display a bar chart showing the number of risks (total and closed) for each work."""
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.write("### Number of Risks by Work")
    
    # Replace "Work Name" and "Status" with the actual column names in your dataset
    work_column = "Work Name"  # Replace with the actual column name for work
    status_column = "Status"   # Replace with the actual column name for status
    
    # Check if the required columns exist in the DataFrame
    if work_column not in df.columns or status_column not in df.columns:
        st.error(f"Required columns '{work_column}' or '{status_column}' not found in the dataset.")
        return
    
    # Group by work and status, then unstack for visualization
    work_risk_counts = df.groupby(work_column)[status_column].value_counts().unstack().fillna(0)
    
    # Plot the bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    work_risk_counts.plot(kind="bar", stacked=True, ax=ax)
    ax.set_title("Number of Risks (Total and Closed) by Work")
    ax.set_xlabel(work_column)
    ax.set_ylabel("Number of Risks")
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

def display_pie_chart(df):
    """Display a pie chart showing the distribution of risks work-wise."""
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.write("### Risk Distribution Work-wise")
    
    # Replace "Work Name" with the actual column name in your dataset
    work_column = "Work Name"  # Replace with the actual column name for work
    
    # Check if the required column exists in the DataFrame
    if work_column not in df.columns:
        st.error(f"Column '{work_column}' not found in the dataset.")
        return
    
    # Check if the DataFrame is empty
    if df.empty:
        st.warning("The dataset is empty. No data to visualize.")
        return
    
    # Calculate the count of each work name
    work_risk_total = df[work_column].value_counts()
    
    # Plot the pie chart
    fig, ax = plt.subplots(figsize=(8, 8))
    work_risk_total.plot(kind="pie", autopct="%1.1f%%", ax=ax)
    ax.set_title("Risk Distribution Work-wise")
    ax.set_ylabel("")  # Remove the default 'None' label
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

def display_table(df):
    """Display the DataFrame as a table in Streamlit."""
    st.markdown('<div class="table-box">', unsafe_allow_html=True)
    st.dataframe(df)
    st.markdown('</div>', unsafe_allow_html=True)

def app():
    """Risk page application logic."""
    st.title("Risk Management Dashboard")
    
    # Provide template for download
    load_template()
    
    # File upload section
    df = process_uploaded_file()
    
    if df is not None:
        

        
        # Display charts
        st.markdown('<h3 style="text-align: center;">Charts:</h3>', unsafe_allow_html=True)
        col1, col2 = st.columns([2, 1])  # 2/3 width for bar chart, 1/3 for pie chart
        with col1:
            display_bar_chart(df)
        with col2:
            display_pie_chart(df)
        
        # Display metrics
        st.markdown('<h3 style="text-align: center;">Metrics Overview:</h3>', unsafe_allow_html=True)
        display_metrics(df)
        
        # Display table
        st.markdown('<h3 style="text-align: center;">Data Table:</h3>', unsafe_allow_html=True)
        display_table(df)
    else:
        st.info("Please upload a file to visualize the data.")
