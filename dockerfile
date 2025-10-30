# Use official Python base image
FROM python:3.11-slim

# Set environment variables for Streamlit
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_PORT=8080
ENV STREAMLIT_BROWSER_SERVER_ADDRESS=0.0.0.0
#
# Set workdir
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8080

# Run Streamlit
CMD ["streamlit", "run", "app.py"]