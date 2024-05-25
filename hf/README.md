# WatsonX-WebChat

WatsonX-WebChat is an interactive web application that uses IBM Watson's language models to answer questions based on the content of a provided web page URL. This application leverages Retrieval-Augmented Generation (RAG) techniques to provide accurate and contextually relevant answers.

## Features

- Extracts and processes text from a given URL.
- Embeds the text and stores it in a database.
- Answers user questions based on the embedded content using IBM Watson's language models.
- Interactive web interface built with Streamlit.

## Setup and Deployment

### Prerequisites

- Docker
- WatsonX IBM
### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/WatsonX-WebChat.git
    cd WatsonX-WebChat
    ```

2. **Create a `.env` file with your IBM Cloud credentials:**

    ```plaintext
    API_KEY=your_ibm_cloud_api_key
    PROJECT_ID=your_ibm_cloud_project_id
    ```

3. **Build the Docker image:**

    ```sh
    docker build -t watsonx-webchat .
    ```

4. **Run the Docker container:**

    ```sh
    docker run -p 8501:8501 --env-file .env watsonx-webchat
    ```

### Deploy on Hugging Face

1. **Log in to Hugging Face CLI:**

    ```sh
    huggingface-cli login
    ```

2. **Create a new repository on Hugging Face.**

3. **Push the Docker image to Hugging Face:**

    ```sh
    docker tag watsonx-webchat huggingface.co/your-username/watsonx-webchat
    docker push huggingface.co/your-username/watsonx-webchat
    ```

4. **Configure the Hugging Face repository to use the Docker image:**

    - Go to your Hugging Face repository page.
    - Click on "Settings".
    - Under "Custom Docker Image", set the image to `huggingface.co/your-username/watsonx-webchat`.

### Usage

1. **Access the application:**

    Open your browser and go to the URL provided by Hugging Face after deploying the application.

2. **Enter the required information:**

    - **API Key**: Your IBM Cloud API key.
    - **Project ID**: Your IBM Cloud project ID.
    - **URL**: The URL of the webpage you want to extract content from.
    - **Collection Name**: A unique name for the webpage's data collection.
    - **Question**: The question you want to ask based on the webpage content.

3. **Get the response:**

    Click the "Answer the question" button to get a response from the application.

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have suggestions for new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
