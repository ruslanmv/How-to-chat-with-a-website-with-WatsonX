# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app.py /app/app.py
COPY webchat.py /app/webchat.py
COPY .streamlit/config.toml  /app/.streamlit/config.toml
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_md

# Expose port 8501 for Streamlit
EXPOSE 8501

# Run the application
ENTRYPOINT ["streamlit", "run", "app.py","--server.port","8501","--server.address","0.0.0.0"]
