# AgentChat – AI-Powered TCP Chat Gateway

AgentChat is a Python-based TCP client-server system that enables AI-powered conversational interactions over raw TCP connections.  
It is designed to demonstrate how **AI services can be integrated into low-level, legacy-friendly networking architectures**, which are still widely used in enterprise and internal systems.

This project focuses on **networking fundamentals, modular AI design, scalability awareness, and cloud readiness**, making it suitable as a portfolio project for Cloud / Azure Engineer roles.

---

## Why TCP-Based AI?

Most modern chat applications rely on HTTP or WebSockets. However, many real-world enterprise environments still depend on:

- Legacy systems
- Internal services
- Financial and infrastructure platforms
- Custom protocols built on TCP

These systems cannot easily adopt web-native protocols.

**AgentChat bridges this gap** by providing an AI-powered chatbot that communicates over TCP, while remaining extensible and deployable in cloud environments.

---

## High-Level Architecture
```
TCP Clients (CLI / Web UI)
|
| TCP Socket
v
Multi-Client TCP Server
|
|-- Connection Handler
|-- Session Processor
|-- AI Agent Layer
|
v
Rule-Based AI Agent
(Q&A Knowledge via JSON)
```

## Key Features

- **Multi-Client TCP Server**
  - Handles multiple concurrent clients
  - Each client session is processed independently

- **Modular AI Agent Architecture**
  - Base agent abstraction
  - Rule-based Q&A agent using structured JSON knowledge
  - Designed for easy replacement with LLMs or RAG-based agents

- **Multiple Client Interfaces**
  - Terminal-based TCP client
  - Web-based UI using Flask for a modern chat experience

- **Extensible and Maintainable Design**
  - AI logic is separated from networking logic
  - Knowledge base can be extended without modifying server code

## Project Structure
```
AI-Based-TCP-Chatbot-Server/
├── agents/
│ ├── base_agent.py
│ ├── simple_agent.py
│ └── qa_data.json
├── server.py
├── client.py
├── web/
│ ├── app.py
│ ├── static/
│ │ └── qa_data.json
│ └── templates/
│ └── chat.html
└── README.md
```

## How the System Works

### TCP Server
- Listens for incoming TCP connections
- Uses a threaded model to handle multiple clients concurrently
- Routes incoming messages to the configured AI agent
- Sends AI-generated responses back to clients over TCP

### AI Agent
- Loads structured question-and-answer data from a JSON file
- Matches user input to predefined prompts or keywords
- Returns deterministic and explainable responses
- Can be extended to support:
  - OpenAI / Azure OpenAI
  - Hugging Face models
  - Retrieval-Augmented Generation (RAG)

### Web Interface
- Flask-based web application
- Acts as a TCP client to the backend server
- Provides a modern UI without changing the core TCP server design

## Setup & Usage

### Prerequisites
- Python 3.8+
- Flask

**Install dependencies:**
```bash
pip install flask
```

**Start the TCP Server**
```
python server.py
```

**Start the Terminal Client (in a new terminal)**
```
python client.py
```

**Start the Web Interface**
```
cd web
python app.py
```

**Open your browser at:** http://localhost:5000

### Knowledge Base Customization
Edit the following files to add or modify AI responses:
- agents/qa_data.json
- web/static/qa_data.json

**Example entry:**
```json
{
  "reverse string": {
    "prompt": "How do I reverse a string in Python?",
    "answer": "You can reverse a string using slicing: s[::-1]"
  }
}
```

## Scalability & Design Considerations
- Current implementation uses thread-based concurrency for simplicity and clarity
- The architecture is intentionally designed to support future upgrades such as:
  - Asynchronous I/O (asyncio)
  - External session stores (Redis)
  - Message queues (Kafka / Azure Event Hub)
  - Horizontal scaling behind a load balancer

## Security Considerations (Planned Enhancements)
- TLS-encrypted TCP communication
- Client authentication tokens
- Input size limits and rate limiting
- Secure secret management for AI providers

## Roadmap
- Async TCP server for higher concurrency
- Dockerized deployment
- Azure-ready infrastructure (VM / Container Apps)
- AI provider abstraction (Azure OpenAI, RAG)
- Centralized logging and observability
- Basic authentication and authorization

## Example Use Cases
- AI enablement for legacy TCP-based systems
- Internal enterprise chat or automation tools
- Educational demonstrations of TCP/IP and AI integration
- Cloud-native system design practice
