import streamlit as st 
# Page config
st.set_page_config(page_title="Settings", page_icon="⚙️")

# Load custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown("""
    <div class="header-container">
        <h1>Settings</h1>
        <p class="subtitle">Customize Your Experience</p>
    </div>
""", unsafe_allow_html=True)

# Se