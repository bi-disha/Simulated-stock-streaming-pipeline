# Use an official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run the FastAPI server
CMD ["uvicorn", "stock_api:app", "--host", "0.0.0.0", "--port", "8000"]
