import streamlit as st


st.set_page_config(
    page_title="ChatGPT Clone",
    layout="wide",
    page_icon="🤖"
)

st.title("Chat with AI 🤖")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant",
         "content": "Hello, feel free to ask anything!"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_prompt = st.chat_input()

if user_prompt is not None:
    st.session_state.messages.append(
         {"role": "assistant",
         "content": user_prompt}
    )
    with st.chat_message("user"):
        st.write(user_prompt)