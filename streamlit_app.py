import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="Modern Streamlit App",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
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
            <h1>Welcome to Modern Streamlit</h1>
            <p class="subtitle">A multi-page application template</p>
        </div>
    """, unsafe_allow_html=True)

    # Create three columns for a modern layout
    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.markdown("""
            <div class="card">
                <h3>Getting Started</h3>
                <p>Navigate through pages using the sidebar menu</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="card">
                <h3>Features</h3>
                <p>Modern design with multiple interactive pages</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="card">
                <h3>Documentation</h3>
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