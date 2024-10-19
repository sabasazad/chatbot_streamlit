import streamlit as st
from transformers import pipeline

# Load the T5 model from Hugging Face
@st.cache_resource
def load_model():
    # T5 is usually used in the 'text2text-generation' pipeline
    return pipeline("text2text-generation", model="t5-small")

# Chatbot function using the T5 model
def chatbot_response(model, user_input):
    # Generate a response from the model
    # T5 requires a task prefix; we use "chat" as a prompt
    prompt = f"chat: {user_input}"
    responses = model(prompt, max_length=50, num_return_sequences=1)
    # Get the generated response
    return responses[0]["generated_text"]

# Streamlit app UI
def main():
    st.title("AI-powered Chatbot using Hugging Face T5")

    # Load the model
    model = load_model()

    # Text input from the user
    user_input = st.text_input("You: ", "")

    # Check if there's input and display the chatbot's response
    if user_input:
        with st.spinner("Thinking..."):
            response = chatbot_response(model, user_input)
        st.write(f"Bot: {response}")

if __name__ == "__main__":
    main()
