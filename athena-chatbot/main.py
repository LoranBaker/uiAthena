import streamlit as st
from pydantic import BaseModel
import requests


class ChatResponse(BaseModel):
    session_id: str
    answer: str

def main():
    st.image("athena-chatbot/logo.png", width=120)
    st.title("Athena AI")

    st.markdown(
    """
    **Hallo, ich bin Athena AI!** Lass uns chatten!
    """
    )


    # Initialize chat history in session_state if not already present.
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "session_id" not in st.session_state:
        st.session_state.session_id = None
    
    # Button to start a new chat.
    if st.button("New Chat"):
        st.session_state.messages = []
        st.session_state.session_id = None
    
    # Display chat history with colored labels
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f'<p> <span style="color: #FFD700;"><strong>You:</strong></span> {msg["content"]} </p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p> <span style="color: #1E90FF;"><strong>Athena:</strong></span> {msg["content"]} </p>', unsafe_allow_html=True)


    # Placeholder for status message (above input field)
    status_placeholder = st.empty()

    # Chat input form.
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("Your question:", "")
        submit = st.form_submit_button("Send")
        
        if submit and user_input:
            # Add the user's message to the chat history.
            st.session_state.messages.append({"role": "user", "content": user_input})
            url = "https://b48c-77-77-254-219.ngrok-free.app/api/chat"
            payload = {
                "prompt": user_input,
                "session_id": st.session_state.session_id,
            }

            response = requests.post(url, json=payload)
            status_placeholder.empty()

            if response.status_code == 200:
                chat_response = ChatResponse(**response.json())
                st.session_state.session_id = chat_response.session_id
                st.session_state.messages.append(
                    {"role": "bot", "content": chat_response.answer}
                )
            else:
                st.session_state.messages.append(
                    {
                        "role": "bot",
                        "content": f"Error {response.status_code}: {response.text}",
                    }
                )


            if 'user_input' not in st.session_state:
                st.session_state.user_input = ''

            st.rerun()

if __name__ == "__main__":
    main()