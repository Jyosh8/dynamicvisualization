# Copyright (c) 2024 Jyosh8
# Licensed under the MIT License (see LICENSE file for details)

import streamlit as st
from streamlit_option_menu import option_menu
# ✅ Set the page config FIRST before any other Streamlit commands
st.set_page_config(layout="wide")

import risk

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=[
            'Risk',
            'Work Progress',
            'Issue',
            'Safety',            
            'Drawing',
            'Contract'
            'user'
            
        ],
        icons=["alert-triangle", "book", "bar-chart", "file-check", "file", "tool", "users", "dashboard"],
        default_index=0
    )

# Main content area
if selected == 'Risk':
    risk.app()

