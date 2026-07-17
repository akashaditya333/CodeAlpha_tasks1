import streamlit as st
from chatbot import get_answer

st.title("FAQ Chatbot")

question = st.text_input("Ask your question")

if st.button("Submit"):

    if question:

        answer = get_answer(question)

        st.success(answer)