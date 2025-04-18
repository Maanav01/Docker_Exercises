# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir streamlit psycopg2

# Expose Streamlit port
EXPOSE 8501

# Start Streamlit app
CMD ["python", "-m", "streamlit", "run", "stream.py", "--server.port=8501", "--server.address=0.0.0.0"]
