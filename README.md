---
title: WatsonX WebChat
emoji: 🚀
colorFrom: pink
colorTo: gray
sdk: docker
app_port: 8501  
pinned: false
---
# WatsonX-WebChat

WatsonX-WebChat is an interactive web application that uses IBM Watson's language models to answer questions based on the content of a provided web page URL. This application leverages Retrieval-Augmented Generation (RAG) techniques to provide accurate and contextually relevant answers.

## Features

- Extracts and processes text from a given URL.
- Embeds the text and stores it in a database.
- Answers user questions based on the embedded content using IBM Watson's language models.
- Interactive web interface built with Streamlit.

## Setup and Deployment

### Prerequisites

- WatsonX IBM
- Docker (optional)
### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/ruslanmv/WatsonX-WebChat.git
    cd WatsonX-WebChat
    ```

2. **Create a `.env` file with your IBM Cloud credentials:**

    ```plaintext
    API_KEY=your_ibm_cloud_api_key
    PROJECT_ID=your_ibm_cloud_project_id
    ```

There are two methods that we can use to run this application    
## Local Method

```sh
pip install -r requirments.txt
```

```sh
streamlit run app.py
```


## Docker Method

1. **Build the Docker image:**

    ```sh
    docker build -t watsonx-webchat .
    ```

2. **Run the Docker container:**

    ```sh
    docker run -p 8501:8501 --env-file .env watsonx-webchat
    ```
### Usage

1. **Access the application:**

    Open your browser and go to the URL provided by Hugging Face after deploying the application.

2. **Enter the required information:**

    - **API Key**: Your IBM Cloud API key.
    - **Project ID**: Your IBM Cloud project ID.
    - **URL**: The URL of the webpage you want to extract content 
    - **Question**: The question you want to ask based on the webpage content.

3. **Get the response:**

    Click the "Answer the question" button to get a response from the application.

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have suggestions for new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
