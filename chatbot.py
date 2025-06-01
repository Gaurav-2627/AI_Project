import streamlit as st

st.set_page_config(page_title="Simple Chatbot", page_icon="🤖")

st.title("🤖 Basic Chatbot")
st.write("This is a simple chatbot using if-else logic.")

# Store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chatbot logic
def get_bot_response(user_msg):
    user_msg = user_msg.lower()

    if "hello" in user_msg or "hi" in user_msg:
        return "Hey there! 👋 How can I help you?"
    elif "how are you" in user_msg:
        return "I'm good, thanks for asking! What about you?"
    elif "bye" in user_msg:
        return "Goodbye! Have a great day! 👋"
    elif "name" in user_msg or "your name" in user_msg:
        return "I’m a mini chatbot made with Streamlit. You can call me StreamBot!"
    else:
        return "Sorry, I didn't understand that. I'm still learning 🤖"

# Input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:")
    submit_button = st.form_submit_button(label="Send")

if submit_button and user_input:
    bot_response = get_bot_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 {sender}:** {message}")
    else:
        st.markdown(f"**🤖 {sender}:** {message}")
