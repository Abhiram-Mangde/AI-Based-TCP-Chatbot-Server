import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

if __name__ == "__main__":
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("==============================")
            print("   Welcome to AgentChat UI")
            print("==============================")
            # Receive greeting from server
            greeting = s.recv(1024).decode('utf-8')
            print(f"Agent: {greeting}")
            print("Type your message and press Enter (type 'exit' to quit):")
            while True:
                message = input('You: ').strip()
                if not message:
                    print("Please enter a non-empty message.")
                    continue
                if message.lower() == 'exit':
                    break
                s.sendall(message.encode('utf-8'))
                data = s.recv(1024)
                if not data:
                    print("Server closed the connection.")
                    break
                print(f"Agent: {data.decode('utf-8')}")
            print("Disconnected.")
    except Exception as e:
        print(f"Error: {e}")
