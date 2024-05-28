# Use a lightweight Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables to prevent Python from writing pyc files to disk and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    python -m spacy download en_core_web_md
# Create the cache directory and set permissions
RUN mkdir -p /app/.cache && \
    chmod -R 777 /app && \
    chmod -R 777 /app/.cache
ENV TRANSFORMERS_CACHE=/app/.cache
ENV HF_HOME=/app/.cache
    # Copy the rest of the application code
COPY app.py /app/app.py
COPY webchat.py /app/webchat.py
COPY utils.py /app/utils.py
COPY .streamlit/config.toml /app/.streamlit/config.toml
COPY styles.css /app/styles.css

# Expose port 8501 for Streamlit
EXPOSE 8501

# Health check to ensure the container is healthy
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Run the application
#ENTRYPOINT ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
ENTRYPOINT ["streamlit", "run", "app.py"]  
