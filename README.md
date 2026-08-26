# Law-Chatbot-AI

## Overview

**Law Chatbot AI** is a web-based chatbot application designed to assist users with basic legal queries through an interactive conversational interface.

The application allows users to enter legal questions and receive chatbot-generated responses through a simple web interface. It uses a **Flask-based backend** to process user requests and communicate with the frontend using JSON.

The main objective of this project is to demonstrate how chatbot technology can be integrated into a web application to provide accessible and interactive legal information.

## Features

### Legal Chatbot

* Accept legal questions through an interactive chat interface.
* Process user queries through the chatbot backend.
* Generate responses based on submitted questions.
* Display chatbot responses directly within the conversation.
* Provide a simple conversational experience for legal queries.

### Chat Interface

* Display user and chatbot messages separately.
* Provide a clean and organized conversation interface.
* Automatically scroll to the latest message.
* Allow users to interact with the chatbot without refreshing the page.

### Backend Communication

* Process requests using a Flask backend.
* Exchange data between frontend and backend using JSON.
* Handle user messages dynamically.
* Return chatbot-generated responses to the web interface.

## Tech Stack

* **Python** — Backend programming and chatbot logic
* **Flask** — Web application framework
* **HTML5** — Web page structure
* **CSS3** — Application styling
* **JavaScript** — Frontend interaction and asynchronous communication
* **JSON** — Data exchange between frontend and backend

## Project Structure

```text
Law-Chatbot-AI/
│
├── app.py                    # Main Flask application
├── chatbox.py                # Chatbot processing and response logic
│
├── templates/                # HTML templates
│   └── index.html            # Main chatbot interface
│
└── README.md                 # Project documentation
```

## Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/dishamehtani/Law-Chatbot-AI.git
cd Law-Chatbot-AI
```

2. **Create a virtual environment:**

```bash
python -m venv venv
```

3. **Activate the virtual environment:**

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

4. **Install Flask:**

```bash
pip install flask
```

5. **Run the application:**

```bash
python app.py
```

6. **Open the application in your browser:**

```text
http://127.0.0.1:5000/
```

## How It Works

1. The user enters a legal question through the chatbot interface.
2. JavaScript captures the submitted message.
3. The message is sent to the Flask backend.
4. Flask passes the query to the chatbot processing logic.
5. The chatbot processes the user's question and generates a response.
6. The response is returned to the frontend using JSON.
7. The generated response is displayed in the chat interface.
8. The conversation automatically scrolls to display the latest message.

## Application Workflow

```text
User Enters Legal Question
          ↓
JavaScript Processes Input
          ↓
Request Sent to Flask Backend
          ↓
Chatbot Processes Query
          ↓
Response Generated
          ↓
JSON Response Returned
          ↓
Response Displayed in Chat
```

## Use Cases

* Asking basic legal questions through a conversational interface.
* Providing general legal information in an accessible format.
* Demonstrating chatbot-based question-and-answer systems.
* Demonstrating frontend and backend communication using Flask and JavaScript.
* Exploring the application of conversational interfaces in the legal domain.
* Educational demonstration of web-based chatbot development.

## Future Enhancements

* Integrate advanced Natural Language Processing capabilities.
* Improve legal query understanding and response accuracy.
* Add support for multiple legal categories.
* Maintain conversation history.
* Add user authentication and personalized sessions.
* Support multilingual legal queries.
* Integrate verified legal information sources.
* Add document-based legal information retrieval.
* Improve the chatbot interface and accessibility.
* Deploy the application for online access.

## Contribution

Feel free to fork the repository, submit issues, or contribute through pull requests.

## Disclaimer

This project is developed for **educational and informational purposes only**. The chatbot provides general legal information and should not be considered a substitute for advice from a qualified legal professional. Users should consult an appropriate legal professional for advice regarding specific legal matters.
