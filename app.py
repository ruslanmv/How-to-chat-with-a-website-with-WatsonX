# For reading credentials from the .env file
import os
from dotenv import load_dotenv
import streamlit as st
import webchat

# URL of the hosted LLMs is hardcoded because at this time all LLMs share the same endpoint
url = "https://us-south.ml.cloud.ibm.com"

# These global variables will be updated in get_credentials() function
watsonx_project_id = ""
# Replace with your IBM Cloud key
api_key = ""

def get_credentials():
    load_dotenv()
    # Update the global variables that will be used for authentication in another function
    globals()["api_key"] = os.getenv("api_key", None)
    globals()["watsonx_project_id"] = os.getenv("project_id", None)


def set_theme():
    st.markdown("""
        <style>
            .reportview-container, .main {
                background: #ffffff;
                color: #000000;
            }
            .sidebar .sidebar-content {
                background: #f0f2f6;
                color: #000000;
            }
            .stButton>button {
                background-color: #0D62FE;
                color: white;
            }
            .stTextInput>div>div>input {
                color: #000000;
                background-color: #ffffff;
            }
            tTextArea>div>textarea {
                color: #000000;
                background-color: #ffffff;
            }
            label, .stTextInput>label, .stTextArea>label {
                color: #000000;
            }
            h1, h2, h3, h4, h5, h6 {
                color: #000000;
            }
            .sidebar .sidebar-content h2, .sidebar .sidebar-content h3, .sidebar .sidebar-content h4, .sidebar .sidebar-content h5, .sidebar .sidebar-content h6, 
            .sidebar .sidebar-content label, .sidebar .sidebar-content .stTextInput>label, .sidebar .sidebar-content .stTextArea>label {
                color: #000000;
            }
            .navbar {
                overflow: hidden;
                background-color: #000000;
                position: fixed;
                top: 0;
                width: 100%;
                z-index: 1000;
            }
            .navbar h1 {
                float: left;
                display: block;
                color: #ffffff;
                text-align: center;
                padding: 14px 1x;
                text-decoration: none;
                font-size: 17px;
                margin: 0;  
            }
            .menu-bar {
                background-color: #000000;
                padding: 10px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .menu-bar h1 {
                color: #ffffff;
                margin: 0;
                font-size: 18px; /* Reduced font size */
                font-family: 'IBM Plex Sans', sans-serif; /* IBM font */
            }
        </style>
    """, unsafe_allow_html=True)


from urllib.parse import urlparse

def create_collection_name(url):
    parsed_url = urlparse(url)
    domain_parts = parsed_url.netloc.split('.')
    if len(domain_parts) >= 2:
        return domain_parts[-2]  # Extracting the second-level domain
    else:
        return "base"

def main():
    # Get the API key and project id and update global variables
    get_credentials()

    # Use the full page instead of a narrow central column
    st.set_page_config(layout="wide", page_title="RAG Web Demo", page_icon="")

    # Set the theme
    set_theme()

    # Streamlit app title with style
    st.markdown("""
        <div class="menu-bar">
            <h1>IBM watsonx.ai - webchat</h1>
        </div>
        <div style="margin-top: 20px;"><p>Insert the website you want to chat with and ask your question.</p></div>
        
    """, unsafe_allow_html=True)

    # Sidebar for settings
    st.sidebar.header("Settings")
    st.sidebar.markdown("Insert your credentials of [IBM Cloud](https://cloud.ibm.com/login) for watsonx.ai", unsafe_allow_html=True)
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    api_key_input = st.sidebar.text_input("API Key", api_key, type="password")
    project_id_input = st.sidebar.text_input("Project ID", watsonx_project_id)

    # Update credentials if provided by the user
    if api_key_input:
        globals()["api_key"] = api_key_input
    if project_id_input:
        globals()["watsonx_project_id"] = project_id_input

    # Main input area
    #st.markdown("<hr>", unsafe_allow_html=True)
    user_url = st.text_input('Provide a URL')
    # Provide a unique name for this website (lower case). Use the same name for the same URL to avoid loading data multiple times.
    collection_name = create_collection_name(user_url)
    # UI component to enter the question
    question = st.text_area('Question', height=100)
    button_clicked = st.button("Answer the question")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Response")

    # Invoke the LLM when the button is clicked
    if button_clicked:
        response = webchat.answer_questions_from_web(api_key, watsonx_project_id, user_url, question, collection_name)
        st.write(response)


if __name__ == "__main__":
    main()
