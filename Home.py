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
# firebase_admin.get_app(name='outreach')

# Use a service account.
cred = credentials.Certificate(fb_credentials)
# app = firebase_admin.initialize_app(cred)
try:
    firebase_admin.get_app()
except ValueError as e:
    firebase_admin.initialize_app(cred)
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
                <img src="https://github.com/PhaelIshall/blank-app/blob/main/1.jpg?raw=true" alt="Avatar" style="width:100%;border-radius: 20px; margin-top: 10px;">
            
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="card">
                <h2 style="color:black">Fact-checking</h2>
                <p> Interact with a chatbot and ask it some of our suggested questions, see if these tools can make mistakes!</p>
                <img src="https://github.com/PhaelIshall/blank-app/blob/main/2.jpg?raw=true" alt="Avatar" style="width:100%;border-radius: 20px; margin-top: 10px;">
            </div>
        """, unsafe_allow_html=True)
    # Print results.

    st.markdown("""
            <div class="card" style="background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2-h0-c8HwrKm7tLa_tc8vUEFssuU3-Qy7_Q&s'); background-size: fit; background-position: center;">
                <h2 style="color: white; background-color:rgba(60, 60, 60,0.4);">How can AI help us in our daily lives?</h2>        
            </div>
        """, unsafe_allow_html=True)


    # Text input for answers
    st.markdown("Type your answers below, you will also be able to see your peers' responses. Next, we will take some time to discuss the topic!")    
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
          st.markdown(f'<button class="success"> {doc.id} </button>', unsafe_allow_html=True)
          # st.button(doc.id, type="primary")
      elif i%2== 0:
        with col2:
          st.markdown(f'<button class="danger"> {doc.id} </button>', unsafe_allow_html=True)
          # st.button(doc.id, type="secondary")
      else:
        with col3:
          st.markdown(f'<button class="secondary"> {doc.id} </button>', unsafe_allow_html=True)
          # st.button(doc.id, type="tertiary")

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
