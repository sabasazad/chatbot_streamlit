import streamlit as st
from transformers import pipeline

# Load the NLP model from Hugging Face (GPT-2)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

# Chatbot function using the Hugging Face model
def chatbot_response(model, user_input):
    # Generate a response from the model
    responses = model(user_input, max_length=50, num_return_sequences=1)
    # Get the generated response
    return responses[0]["generated_text"]

# Streamlit app UI
def main():
    st.title("AI-powered Chatbot using Hugging Face")

    # Load the model
    model = load_model()

    # Text input from the user
    user_input = st.text_input("You: ", "")

    # Check if there's input and display the chatbot's response
    if user_input:
        with st.spinner("Thinking..."):
            response = chatbot_response(model, user_input)
        st.write(f"Bot: {response[len(user_input):]}")  # Clean up response by removing the input part

if __name__ == "__main__":
    main()
