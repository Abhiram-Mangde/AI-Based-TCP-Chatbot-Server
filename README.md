# AgentChat: AI-Powered TCP Client-Server Chatbot

## Overview
AgentChat is a Python-based project that demonstrates a modular, industry-style TCP client-server chatbot system powered by a rule-based AI agent. It features:
- A multi-client TCP server using threading
- A simple TCP client for terminal chat
- A Flask web UI for modern chat experience
- An extensible agent architecture with Q&A knowledge loaded from a JSON file

## Features
- **Multi-client TCP Server:** Handles multiple clients concurrently using threads.
- **AI Agent:** Answers Python programming questions using a customizable Q&A file (`qa_data.json`).
- **Terminal Client:** Simple CLI for chatting with the agent.
- **Web UI:** Modern, responsive chat interface with prompt buttons for common questions.
- **Extensible Design:** Easily add new agents or expand Q&A knowledge.

## Folder Structure
```
AI-Based-TCP-Chatbot-Server/
├── agents/
│   ├── base_agent.py
│   ├── simple_agent.py
│   ├── qa_data.json
├── client.py
├── server.py
├── web/
│   ├── app.py
│   ├── static/
│   │   └── qa_data.json
│   ├── templates/
│   │   └── chat.html
└── README.md
```

## How It Works
### 1. TCP Server (`server.py`)
- Listens for incoming TCP connections.
- Each client is handled in a separate thread.
- On connection, sends a greeting and then processes messages using the AI agent.

### 2. TCP Client (`client.py`)
- Connects to the server and allows users to chat via terminal.
- Receives agent responses and displays them.

### 3. AI Agent (`agents/simple_agent.py`)
- Loads Q&A pairs from `qa_data.json`.
- Matches user questions to keywords or prompts and returns the corresponding answer.
- Easily extensible for more advanced logic or external APIs.

### 4. Web UI (`web/app.py`, `web/templates/chat.html`)
- Flask app serves a modern chat interface.
- UI displays prompt buttons for common questions (loaded from `qa_data.json`).
- Users can chat with the agent and open multiple client windows.

## Setup & Usage
### Prerequisites
- Python 3.8+
- Flask (`pip install flask`)

### 1. Start the TCP Server
```bash
python3 server.py
```

### 2. Start the Terminal Client (in a separate terminal)
```bash
python3 client.py
```

### 3. Start the Web UI
```bash
cd web
python3 app.py
```
- Open your browser at `http://localhost:5000`
- Use the prompt buttons or type your own questions

### 4. Add/Edit Q&A Knowledge
- Edit `agents/qa_data.json` and `web/static/qa_data.json` to add new questions and answers.
- Each entry should have a `prompt` (user-friendly question) and `answer` (agent's response).

## Example Q&A
```
"reverse string": {
	"prompt": "How do I reverse a string in Python?",
	"answer": "To reverse a string in Python: s = 'hello'; reversed_s = s[::-1]  # Output: 'olleh'"
}
```

## Extending the Project
- Add new agents in the `agents/` folder for different domains or logic.
- Integrate external APIs for advanced AI (OpenAI, Hugging Face, etc.).
- Improve the web UI with more features (chat history, authentication, etc.).

## License
This project is for educational and demonstration purposes. Feel free to use and modify as needed.
# AI-Based-TCP-Chatbot-Server
A TCP-based client-server chat application where:  Multiple clients (users) connect to a server.  Each client talks to an AI agent.  The agent acts like a helpful assistant (summarizer, translator, or Q&amp;A).  AI logic is built into the server.
