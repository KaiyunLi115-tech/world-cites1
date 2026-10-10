import streamlit as st

st.set_page_config(
    page_title="World Cities",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="auto"
)

# Main title
st.title("🌍 World Cities Explorer")

# Welcome text
st.markdown("""
Welcome to the **World Cities Explorer** app! 

This application provides insights and information about cities around the world. 
Explore different cities, their characteristics, and interesting facts.

Click the button below to get started and navigate to the main application.
""")

# Button to navigate to app.py
if st.button("Go to App →", use_container_width=True, type="primary"):
    st.switch_page("pages/app.py")

# Optional: Add footer
st.divider()
st.markdown("""
---
*Discover the world, one city at a time* 🌆
""")
