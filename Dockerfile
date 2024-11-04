# Use a lightweight Python image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the environment variables (replace placeholders with your actual values)
ENV BOT_TOKEN "your_bot_token"
ENV API_ID "your_api_id"
ENV API_HASH "your_api_hash"
# ... other environment variables as needed

# Define the command to run the application
CMD ["python", "bot.py"]
