# For reading credentials from the .env file
import os
from dotenv import load_dotenv
import streamlit as st
import webchat

# URL of the hosted LLMs is hardcoded because at this time all LLMs share the same endpoint
url = "https://us-south.ml.cloud.ibm.com"

# These global variables will be updated in get_credentials() function
watsonx_project_id = ""
api_key = ""

def get_credentials():
    load_dotenv()
    # Update the global variables that will be used for authentication in another function
    globals()["api_key"] = os.getenv("API_KEY", "")
    globals()["watsonx_project_id"] = os.getenv("PROJECT_ID", "")

def main():
    # Get the API key and project id and update global variables
    get_credentials()

    # Use the full page instead of a narrow central column
    st.set_page_config(layout="wide")

    # Streamlit app title
    st.title("🌠Demo of RAG with a Web page")

    # Sidebar for settings
    st.sidebar.header("Settings")
    api_key_input = st.sidebar.text_input("API Key", api_key)
    project_id_input = st.sidebar.text_input("Project ID", watsonx_project_id)
    
    # Update credentials if provided by the user
    if api_key_input:
        globals()["api_key"] = api_key_input
    if project_id_input:
        globals()["watsonx_project_id"] = project_id_input

    user_url = st.text_input('Provide a URL')
    collection_name = st.text_input('Provide a unique name for this website (lower case). Use the same name for the same URL to avoid loading data multiple times.')

    # UI component to enter the question
    question = st.text_area('Question', height=100)
    button_clicked = st.button("Answer the question")

    st.subheader("Response")

    # Invoke the LLM when the button is clicked
    if button_clicked:
        response = webchat.answer_questions_from_web(api_key, watsonx_project_id, user_url, question, collection_name)
        st.write(response)

if __name__ == "__main__":
    main()
