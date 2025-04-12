import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="AI Outreach",
    page_icon="✨",
    layout="wide",
    # initial_sidebar_state="collapsed",
)

# Load custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Main content area
def main():
    # Header section with custom styling
   st.markdown("""
        <div class="header-container">
            <h1>Trusting AI</h1>
            <p style="text-align:center; font-size: 1.35rem;">An interactive journey into how AI systems work and why fairness matters</p>
        </div>
    """, unsafe_allow_html=True)

    # Create three columns for a modern layout
    col1, col2 = st.columns([1,1])


    with col1:
        st.markdown("""
            <div class="card">
                <h2 style="color:black">Facial Recognition</h2>
                <p> Discover how AI facial recognition works and why bias happens with our interactive AI predictor! </p>
                <img src="https://media.canva.com/v2/files/uri:ifs%3A%2F%2FM%2Ff7a76fe6-3dd5-45a0-8858-964b5d1f1519?csig=AAAAAAAAAAAAAAAAAAAAAMmFB-ZPhcGW0LoMAk97dW95BqsrQ4AItNI5Ip4pTVBw&exp=1744507053&signer=media-rpc&token=AAIAAU0AJGY3YTc2ZmU2LTNkZDUtNDVhMC04ODU4LTk2NGI1ZDFmMTUxOQAAAAABliy5I8hCHhSgRryTOrU7beSAXYeMZkxkDrtb6_gEJk91M_PTtg" alt="Avatar" style="width:100%;border-radius: 20px; margin-top: 10px;">
            
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="card">
                <h2 style="color:black">Fact-checking</h2>
                <p> Interract with a chatbot and ask it some of our suggested questions, see if these tools can make mistakes!</p>
                <img src="https://media.canva.com/v2/files/uri:ifs%3A%2F%2FM%2Fc1d3b292-ffd2-4c7d-8a73-a199bd9607de?csig=AAAAAAAAAAAAAAAAAAAAALjo0qJT2Oxw7L9MzrxIEOXTNESeowF1YVAXh976IbYI&exp=1744506393&signer=media-rpc&token=AAIAAU0AJGMxZDNiMjkyLWZmZDItNGM3ZC04YTczLWExOTliZDk2MDdkZQAAAAABliyvEajIqZ1TJSLqjIxd9u5WUNv2b57csGHWpUd6fF_v3o4T3Q" alt="Avatar" style="width:100%;border-radius: 20px; margin-top: 10px;">
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
