import socket
import threading
import random
import string

def generate_random_key(length=8):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def handle_client(client_socket, client_id, shared_key, clients):
    client_socket.sendall(f"Your shared key: {shared_key}\n".encode('utf-8'))
    print(f"Sent shared key to Client {client_id}: {shared_key}")
    
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received from Client {client_id}: {message}")
                for other_client in clients:
                    if other_client != client_socket:
                        print(f"Sending to Client {client_id}'s message to other client: {message}")
                        other_client.sendall(f"Client {client_id} : {message}".encode('utf-8'))
            else:
                print(f"Client {client_id} disconnected.")
                break
        except Exception as e:
            print(f"Error handling client {client_id}: {e}")
            break

    client_socket.close()
    clients.remove(client_socket)

def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(2)
    print("Server is listening for connections...")

    clients = []
    while len(clients) < 2:
        client_socket, client_address = server_socket.accept()
        print(f"Connected with {client_address}")
        clients.append(client_socket)
    
    shared_key = generate_random_key()
    print(f"Generated shared key: {shared_key}")

    for i, client_socket in enumerate(clients):
        threading.Thread(target=handle_client, args=(client_socket, i + 1, shared_key, clients)).start()

if __name__ == "__main__":
    server_program()
