# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app.py /app/app.py
COPY webchat.py /app/webchat.py
COPY .streamlit/config.toml  /app/.streamlit/config.toml
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_md

# Expose port 8501 for Streamlit
EXPOSE 8501

# Make sure the script is executable
RUN chmod +x run.py

# Run the application
ENTRYPOINT ["streamlit", "run", "app.py"]
