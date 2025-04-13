import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

fb_credentials = {"type": st.secrets.firebase["type"],
  "project_id": st.secrets.firebase["project_id"],
  "private_key_id": st.secrets.firebase["private_key_id"],
  "private_key": st.secrets.firebase["private_key"],
  "client_email": st.secrets.firebase["client_email"],
  "client_id": st.secrets.firebase["client_id"],
  "auth_uri": st.secrets.firebase["auth_uri"],
  "token_uri": st.secrets.firebase["token_uri"],
  "auth_provider_x509_cert_url": st.secrets.firebase["auth_provider_x509_cert_url"],
  "client_x509_cert_url": st.secrets.firebase["client_x509_cert_url"],
  "universe_domain": st.secrets.firebase["universe_domain"]
}
answer = ""
# Use a service account.
cred = credentials.Certificate(fb_credentials)
db = firestore.client()

# Configure page settings
st.set_page_config(
    page_title="Welcome",
    page_icon="✨",
    layout="wide",
    # initial_sidebar_state="collapsed",
   
)

# Load custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def submit():
    doc_ref = db.collection("question1").document(st.session_state.widget)
    st.toast(f"You submitted {st.session_state.widget}")
    doc_ref.set({"answer": st.session_state.widget})
    st.session_state.widget = ""
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
                <p> Interact with a chatbot and ask it some of our suggested questions, see if these tools can make mistakes!</p>
                <img src="https://media.canva.com/v2/files/uri:ifs%3A%2F%2FM%2Fc1d3b292-ffd2-4c7d-8a73-a199bd9607de?csig=AAAAAAAAAAAAAAAAAAAAALjo0qJT2Oxw7L9MzrxIEOXTNESeowF1YVAXh976IbYI&exp=1744506393&signer=media-rpc&token=AAIAAU0AJGMxZDNiMjkyLWZmZDItNGM3ZC04YTczLWExOTliZDk2MDdkZQAAAAABliyvEajIqZ1TJSLqjIxd9u5WUNv2b57csGHWpUd6fF_v3o4T3Q" alt="Avatar" style="width:100%;border-radius: 20px; margin-top: 10px;">
            </div>
        """, unsafe_allow_html=True)
    # Print results.

    st.markdown("""
            <div class="card" style="background-image: url('https://img.freepik.com/premium-photo/colorful-collection-question-marks-question-mark_1109006-146882.jpg?w=1380'); background-size: cover; background-position: center;>
                <h2>How can AI help us in our daily lives?</h2>
                <p> Type your answers below and let's discuss the answers. You will also be able to see your peers' responses. </p>            
            </div>
        """, unsafe_allow_html=True)


    # Text input for answers
    answer = st.text_input("Enter your answer:", key="widget", on_change=submit)
    # Create a reference to the Google post.
  
    answers = db.collection("question1")
    docs = answers.stream()
    col1, col2, col3 = st.columns([1,1,1])
    i = 0
    for doc in docs: 
      i+=1
      if i%3== 0:
        with col1:
          st.button(doc.id, type="primary")
      if i%2== 0:
        with col2:
          st.button(doc.id, type="secondary")
      else:
        with col3:
          st.button(doc.id, type="tertiary")

    # When Enter is pressed
    # if answer:
    #     st.session_state.answers.append(answer)
    #     # Clear the input
    #     st.session_state.answer = ""


    # Footer section
    st.markdown("""
        <div class="footer">
            <p> UCL AI Outreach program 2025 </p>
        </div>
    """, unsafe_allow_html=True)
    
    
if __name__ == "__main__":
    main()
