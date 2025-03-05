import streamlit as st 
import random
import time
import os
from huggingface_hub import InferenceClient
# st.set_page_config(page_title="Chatbot", page_icon="")

# Load custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown("""
    <div class="header-container">
        <h1>Chatbot</h1>
        <p class="subtitle">Are you using this for homework? You might want to reconsider!</p>
    </div>
""", unsafe_allow_html=True)

def generate_pastel_color():
    """Generate a random pastel color in HSL format"""
    hue = random.randint(0, 360)  # Random hue
    saturation = random.randint(50, 65)  # Moderate saturation for pastel
    lightness = random.randint(80, 90)  # High lightness for pastel
    return f"hsl({hue}, {saturation}%, {lightness}%)"

# Initialize session state for info cards
if 'info_cards' not in st.session_state:
    st.session_state.info_cards = [
        {"id": 1, "color": generate_pastel_color(), "title": "Hint!", "content": "Try to ask the Chatbot how many Rs are in Stawberry! A kid can answer so Chatbot probably can... right?"},
        {"id": 2, "color": generate_pastel_color(), "title": "Tips & Tricks", "content": "A lot of people actually ask chatbots for advice, but can we rely on them for basic commonsense? Ask Chatbot: Name 5 countries that start and end with the same letter. "},
    ]

# Create container for cards
cards_container = st.container()

# Display info cards
for i, card in enumerate(st.session_state.info_cards):
    col1, col2 = cards_container.columns([11, 1])
    with col1:
        st.markdown(f"""
            <div class="info-card" style="background: {card['color']}">
                <h3 class="info-card-title">✨ {card['title']}</h3>
                <p class="info-card-content">{card['content']}</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        if st.button("×", key=f"close_{card['id']}"):
            st.session_state.info_cards.remove(card)
            st.rerun()
# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


API_KEY =  st.secrets("API_KEY")



client = InferenceClient(
	provider="hf-inference",
	api_key=API_KEY
)




# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    completion = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.3", 
        messages=st.session_state.messages, 
        max_tokens=500,
    )
    resp = completion.choices[0].message.content
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        print(resp)
        # response = st.write(resp)
        st.session_state.messages.append({"role": "assistant", "content": resp})
        st.write(resp)
    # Add assistant response to chat history
    