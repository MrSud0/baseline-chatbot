FROM python:3.9-slim-buster

# Set up working directory
WORKDIR /app

# Copy files into container
COPY requirements.txt /app
COPY chatbot.py /app
COPY templates/index.html /app/templates/index.html
COPY static/styles.css /app/static/styles.css

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set up OpenAI API credentials
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

# Expose port for chatbot
EXPOSE 5000

# Start chatbot application
CMD [ "python", "chatbot.py" ]
