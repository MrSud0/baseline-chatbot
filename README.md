# Python-based Chatbot Platform with OpenAI's GPT-3 API

This is a simple chatbot platform written in Python that uses OpenAI's GPT-3 API for natural language processing. The chatbot can be accessed via a simple frontend that allows users to enter messages and receive responses from the chatbot.

## Installation

To install the chatbot platform using Docker, follow these steps:

1. Clone this repository to your local machine: `git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git`
2. Navigate to the root directory of the project: `cd YOUR_REPOSITORY`
3. Build the Docker image: `docker build -t chatbot .`
4. Run the Docker container: `docker run -p 5000:5000 -e OPENAI_API_KEY=YOUR_API_KEY chatbot`. 
5. You can also create an .env file and add the key there, then run the container as `docker run -p 5000:5000 chatbot`. 

## Usage

To use the chatbot platform, follow these steps:

1. Navigate to `http://localhost:5000` in your web browser
2. Enter a message in the input field and click the "Send" button to receive a response from the chatbot

## Configuration

The following configuration options are available for the chatbot platform:

- `OPENAI_API_KEY`: Your OpenAI API key, which can be obtained from the OpenAI website

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork this repository to your own GitHub account
2. Create a new branch: `git checkout -b YOUR_BRANCH_NAME`
3. Make your changes and commit them: `git commit -m "YOUR_COMMIT_MESSAGE"`
4. Push your changes to your fork: `git push origin YOUR_BRANCH_NAME`
5. Open a pull request to the `main` branch of this repository

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Credits

This chatbot platform was created by MrSudo. The project was inspired by OpenAI's GPT-3 API and the Flask framework.

