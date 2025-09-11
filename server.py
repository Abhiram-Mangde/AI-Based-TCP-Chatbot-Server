import socket
import threading
from agents.simple_agent import SimpleAgent

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Non-privileged port

class ClientThread(threading.Thread):
    def __init__(self, conn, addr, agent):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.agent = agent

    def run(self):
        print(f"Connected by {self.addr}")
        try:
            # Send greeting to client
            greeting = "Hello! I am AgentChat. How can I help you today?"
            self.conn.sendall(greeting.encode('utf-8'))
            while True:
                data = self.conn.recv(1024)
                if not data:
                    print(f"No data received from {self.addr}. Closing connection.")
                    break
                message = data.decode('utf-8').strip()
                if not message:
                    print(f"Empty message from {self.addr}. Ignoring.")
                    continue
                print(f"Received from {self.addr}: {message}")
                response = self.agent.process(message)
                self.conn.sendall(response.encode('utf-8'))
        except Exception as e:
            print(f"Error with client {self.addr}: {e}")
        finally:
            self.conn.close()
            print(f"Connection closed: {self.addr}")

def start_server():
    agent = SimpleAgent()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            thread = ClientThread(conn, addr, agent)
            thread.start()

if __name__ == "__main__":
    start_server()
