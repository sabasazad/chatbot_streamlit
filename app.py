import streamlit as st

# Basic chatbot function that processes user input
def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I am a simple chatbot created for demo purposes.",
        "bye": "Goodbye! Feel free to come back anytime."
    }

    # Basic keyword-based response logic
    for key in responses:
        if key in user_input.lower():
            return responses[key]
    
    return "I'm sorry, I don't understand. Can you rephrase?"

# Streamlit app UI
def main():
    st.title("Simple Chatbot")

    # Text input from the user
    user_input = st.text_input("You: ", "")

    # Check if there's input and display the chatbot's response
    if user_input:
        response = chatbot_response(user_input)
        st.write(f"Bot: {response}")

if __name__ == "__main__":
    main()
