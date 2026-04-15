import streamlit as st
import requests

# Page config
st.set_page_config(page_title="AI Chatbot", page_icon="💬")

st.title("💬 Customer Support Chatbot")

# Initialize session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "user":
            st.markdown(msg["content"])
        else:
            for res in msg["content"]:
                st.markdown(f"**{res['answer']}**")
                st.caption(f"{res['category']} • Confidence: {round(res['score'],2)}")


# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Get response from API
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"text": user_input}
            )
            results = response.json()

        except:
            results = [{
                "answer": "Server not running. Start FastAPI first.",
                "category": "Error",
                "score": 0
            }]

    # Normalize response
    if isinstance(results, str):
        results = [{
            "answer": results,
            "category": "Unknown",
            "score": 0
        }]

    # Add bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": results
    })

    st.rerun()