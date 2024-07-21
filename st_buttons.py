"""
st_buttons.py
POC to select and enter text automatically in the chat window
Licence Apaache 2.0
"""

import streamlit as st

def main():
    # Set the title of the app
    st.title("🌞 Weather Chat Assistant")
    st.markdown("""
    Welcome to the Weather Chat Assistant! 
    Click on the buttons below to ask preset questions about staying cool in hot weather, or type your own message in the chat box.
    """)

    # Create buttons at the top with icons
    st.markdown("### Quick Questions")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("❄️ How can I keep cool?"):
            st.session_state.user_input = "Today is hot, how can I keep cool?"
            st.session_state.submit = True

        if st.button("🌳 Where can I find shade?"):
            st.session_state.user_input = "Today is hot, where can I find shade?"
            st.session_state.submit = True

    with col2:
        if st.button("🍃 How can I use nature to cool down?"):
            st.session_state.user_input = "Today is hot, how can I use nature to keep me cool?"
            st.session_state.submit = True

        if st.button("🧘‍♂️ What pranayama can I do to stay cool?"):
            st.session_state.user_input = "Today is hot, what pranayama can I do to keep me cool?"
            st.session_state.submit = True

    # Initialize chat history if it doesn't exist
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("💬 Type your message here:"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"Echo: {prompt}"  # Placeholder for actual response logic
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Check if a button was clicked and automatically submit
    if "submit" in st.session_state and st.session_state.submit:
        prompt = st.session_state.user_input
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"Echo: {prompt}"  # Placeholder for actual response logic
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Reset the submit flag
        st.session_state.submit = False
        st.session_state.user_input = ""

if __name__ == "__main__":
    main()
