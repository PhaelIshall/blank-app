import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="Welcome",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
   
)


# pg = st.navigation([st.Page("page_1.py"), st.Page("page_2.py")])
# pg.run()

# Load custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Main content area
def main():
    # Header section with custom styling
    st.markdown("""
        <div class="header-container">
            <h1>Trusting AI</h1>
            <p class="subtitle">An interactive journey into how AI systems work and why fairness matters</p>
        </div>
    """, unsafe_allow_html=True)

    # Create three columns for a modern layout
    col1, col2 = st.columns([1,1])

    with col1:
        st.markdown("""
            <div class="card">
                <h3>Learn the basiscs</h3>
                <img src="detection.jpg" alt="picture of facial detection" class="card-image">
                <p>Discover how AI facial recognition works and why bias can occur</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="card">
                <h3>Fact-checking</h3>
                <p>Check other pages for more examples</p>
            </div>
        """, unsafe_allow_html=True)

    # Footer section
    st.markdown("""
        <div class="footer">
            <p>Built with Streamlit ❤️</p>
        </div>
    """, unsafe_allow_html=True)
    
    
if __name__ == "__main__":
    main()
