import openai
import os
from flask import Flask, request, render_template, jsonify

# Load OpenAI API key from environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Set up OpenAI API client
openai.api_key = OPENAI_API_KEY

# Set up Flask application
app = Flask(__name__)

# Set up chatbot route
@app.route("/chatbot", methods=["POST"])
def chatbot():
    # Retrieve user input
    user_input = request.form["input"]
    
    # Retrieve response from OpenAI API
    response = get_openai_response(user_input)
    
    # Return response to user
    return jsonify({"response": response})

# Set up index route
@app.route("/")
def index():
    return render_template("index.html")

# Set up function to retrieve response from OpenAI API
def get_openai_response(user_input):
    prompt = f"User: {user_input}\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
