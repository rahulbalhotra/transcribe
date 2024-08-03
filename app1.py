import streamlit as st
from ai21 import AI21Client
from ai21.models.chat import ChatMessage
# # New Section

client = AI21Client(api_key="atCFs8nr2hoZ3b6RG9tHa5bs0ZGcWqXR")
def func1(user_query):
  messages = [
        ChatMessage(
            role="user",
            content=user_query
        )
    ]
  response = client.chat.completions.create(
        model="jamba-instruct-preview",
        messages=messages,
        top_p=1.0 # Setting to 1 encourages different responses each call.
    )
  return response
 
Content = CaptureResponse.choices[0].message.content

user_query = st.text_input("Ask me anything")

def_func1(user_query)

st.write(Content)
