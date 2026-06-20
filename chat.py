import streamlit as st;
import ollama

def generate_llm_response(prompt, model = "llama3.2"):

    messages = [
            {
                'role' : 'user',
                'content' : prompt,
            }
        ]
    response = ollama.chat(model=model, messages=messages)
    return response['message']['content']

st.title("Mini Chat Bot")
st.write("Interact with Llama3.2 and genarate responses.")

user_prompt = st.text_area("Enter your prompt: ")

if(st.button("Generate Response")):
    if(user_prompt.strip()) != "":
        with st.spinner("Please wait... Your response is getting generated."):
            try:
                response = generate_llm_response(user_prompt)
                st.success("Response Generated!")
                st.text_area("Response: ", value=response, height=200)
            except Exception as e:
                st.error("Error: {str(e)}")
    else:
        st.warning("Please enter a prompt")