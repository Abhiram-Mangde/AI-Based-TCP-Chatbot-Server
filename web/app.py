from flask import Flask, render_template, request, jsonify
import socket

app = Flask(__name__)

TCP_HOST = '127.0.0.1'
TCP_PORT = 65432

# Helper to send/receive from TCP server
def chat_with_agent(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((TCP_HOST, TCP_PORT))
        greeting = s.recv(1024).decode('utf-8')
        s.sendall(message.encode('utf-8'))
        response = s.recv(1024).decode('utf-8')
    return greeting, response

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/send', methods=['POST'])
def send():
    user_message = request.json.get('message', '')
    greeting, agent_response = chat_with_agent(user_message)
    return jsonify({'greeting': greeting, 'response': agent_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
