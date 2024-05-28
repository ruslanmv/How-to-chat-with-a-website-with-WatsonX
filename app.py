import os
from dotenv import load_dotenv
import streamlit as st
import webchat
import utils

# URL of the hosted LLMs is hardcoded because at this time all LLMs share the same endpoint
url = "https://us-south.ml.cloud.ibm.com"

def main():
    # Initialize session state for credentials
    if 'watsonx_project_id' not in st.session_state:
        st.session_state['watsonx_project_id'] = ""
    if 'api_key' not in st.session_state:
        st.session_state['api_key'] = ""

    st.set_page_config(layout="wide", page_title="RAG Web Demo", page_icon="")
    utils.load_css("styles.css")
    
    # Streamlit app title with style
    st.markdown("""
        <div class="menu-bar">
            <h1>IBM watsonx.ai - webchat</h1>
        </div>
        <div style="margin-top: 20px;"><p>Insert the website you want to chat with and ask your question.</p></div>
    """, unsafe_allow_html=True)
    
    # Sidebar for settings
    st.sidebar.header("Settings")
    st.sidebar.markdown("Insert your credentials of [IBM Cloud](https://cloud.ibm.com/login) for watsonx.ai \n The data is not saved in the server. Your data is secured.", unsafe_allow_html=True)
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    
    # Input fields for API Key and Project ID
    api_key_input = st.sidebar.text_input("API Key", st.session_state['api_key'], type="password")
    project_id_input = st.sidebar.text_input("Project ID", st.session_state['watsonx_project_id'])
    
    # Update session state with the provided credentials
    if api_key_input:
        st.session_state['api_key'] = api_key_input
    if project_id_input:
        st.session_state['watsonx_project_id'] = project_id_input
    
    # Main input area
    user_url = st.text_input('Provide a URL')
    # UI component to enter the question
    question = st.text_area('Question', height=100)
    button_clicked = st.button("Answer the question")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Response")
    
    collection_name = "base"
    client = utils.chromadb_client()
    
    if st.session_state['api_key'] and st.session_state['watsonx_project_id']:
        if button_clicked and user_url:
            # Invoke the LLM when the button is clicked
            response = webchat.answer_questions_from_web(st.session_state['api_key'], st.session_state['watsonx_project_id'], user_url, question, collection_name, client)
            st.write(response)
    else:
        st.warning("Please provide API Key and Project ID in the sidebar.")
  
    # Cleaning Vector Database
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    st.sidebar.header("Memory")
    clean_button_clicked = st.sidebar.button("Clean Memory")
    if clean_button_clicked:
        if collection_name:
            utils.clear_collection(collection_name, client)
            st.sidebar.success("Memory cleared successfully!")
            print("Memory cleared successfully!")
        else:
            st.sidebar.error("Collection name is not defined or empty.")

if __name__ == "__main__":
    main()
