## How to Chat with a Website Using WatsonX

Hello everyone! Today, we're going to create an exciting web app that allows us to chat with any website using Watsonx.ai.

Watsonx.ai is a powerful SaaS service that leverages the full capabilities of IBM's cloud infrastructure. This tool provides a robust platform for integrating advanced AI functionalities into your applications, making it easier than ever to enhance user interactions with intelligent, context-aware responses.


## Step 1: Environment Creation

There are several ways to create an environment in Python. Follow these steps to set up your environment locally:

1. **Install Python 3.10**
   - Download and install Python 3.10 from [here](https://www.python.org/downloads/windows/).

2. **Create a Virtual Environment**
   - Open your terminal or command prompt and navigate to your project directory.
   - Run the following command to create a virtual environment:
     ```bash
     python -m venv .venv
     ```
   - This command creates a new directory named `.venv` in your current working directory.

3. **Activate the Virtual Environment**
   - **Windows:**
     ```bash
     .venv\Scripts\activate.bat
     ```
   - **Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Upgrade pip**
   - Run the following command to upgrade pip:
     ```bash
     python -m pip install --upgrade pip
     ```

5. **Optional: Install JupyterLab for Development and Testing**
   - If you want to use JupyterLab, install it by running:
     ```bash
     pip install ipykernel jupyterlab
     ```

## Step 2: Setup Libraries

Once you have your environment set up and activated, you need to install the necessary libraries. Run the following command to install the required packages:

```bash
pip install streamlit python-dotenv  ibm_watson_machine_learning requests chromadb sentence_transformers
```

IMPORTANT: Be aware of the disk space that will be taken up by documents when they're loaded into
chromadb on your laptop. The size in chroma will likely be the same as .txt file size


## Step 3: Getting API from IBM Cloud

### Obtaining an API Key

To obtain an API key from IBM Cloud, follow these steps:

1. **Sign In**
   - Go to [IBM Cloud](https://cloud.ibm.com) and sign in to your account.

2. **Navigate to Account Settings**
   - Click on your account name in the top right corner of the IBM Cloud dashboard.
   - From the dropdown menu, select "Manage" to go to the Account settings.

3. **Access API Keys**
   - In the left-hand menu, click on “IBM Cloud API keys” under the “Access (IAM)” section.

4. **Create an API Key**
   - On the “API keys” page, click on the “Create an IBM Cloud API key” button.
   - Provide a name and an optional description for your API key.
   - Select the appropriate access policies if needed.
   - Click on the “Create” button to generate the API key.

5. **Save Your API Key**
   - Once the API key is created, a dialog box displaying the API key value will appear.
   - Make sure to copy and save this key as it will not be shown again.

> Note: The steps above are based on the current IBM Cloud interface. They may vary slightly depending on any updates or changes. If you encounter any difficulties or if the steps do not match your IBM Cloud interface, refer to the IBM Cloud documentation or contact IBM support for assistance.

### Retrieving the Project ID for IBM Watsonx

To obtain the Project ID for IBM Watsonx, you will need access to the IBM Watson Machine Learning (WML) service. Follow these steps:

1. **Log In**
   - Log in to the [IBM Cloud Console](https://cloud.ibm.com) using your IBM Cloud credentials.

2. **Navigate to Watson Machine Learning**
   - Go to the Watson Machine Learning service.

3. **Access Service Instance**
   - Click on the service instance associated with your Watsonx project.

4. **Find Service Credentials**
   - In the left-hand menu, click on “Service credentials”.
   - Under the “Credentials” tab, you will find a list of service credentials associated with your Watsonx project.

5. **Retrieve Project ID**
   - Click on the name of the service credential you want to use.
   - In the JSON object, find the “project_id” field. The value of this field is your Project ID.

### Adding Credentials to Your Project

Add the API key and Project ID to the `.env` file in your project directory:

```plaintext
API_KEY=your_api_key
PROJECT_ID=your_project_id
```

This will configure your project to connect to Watsonx.ai using the obtained credentials.

Step 4: Creation of app.py

In the followig section we are going to  invoke Large Language Models (LLMs) deployed in watsonx.ai. Documentation: [here](https://ibm.github.io/watson-machine-learning-sdk/foundation_models.html)
This example shows a Question and Answer use case for a provided web site



