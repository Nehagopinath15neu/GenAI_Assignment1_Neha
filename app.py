import streamlit as st
from backend import get_llm_response

# Streamlit UI configuration
st.title("Cooking Recipe Chatbot 🍳")

# Input field for user queries
user_query = st.text_input("Ask me anything about cooking recipes:")

# Conversation history storage
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Display conversation history
st.subheader("Conversation History")
for message in st.session_state.conversation_history:
    st.write(message)

# If the user submits a query, call the LLM
if st.button("Send"):
    if user_query:
        # Call the backend to get the response from the LLM
        model_name = "mistral"  # or "llama3"
        response = get_llm_response(model_name, user_query)
        
        # Store conversation in session state
        st.session_state.conversation_history.append(f"User: {user_query}")
        st.session_state.conversation_history.append(f"Bot: {response}")

        # Display the latest response
        st.write(f"Bot: {response}")







