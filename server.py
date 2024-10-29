import socket
import threading
import random
import string

def generate_random_key(length=8):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def handle_client(client_socket, client_id, shared_key, clients, usernames):
    # Terima dan simpan username
    username = client_socket.recv(1024).decode('utf-8').split("USERNAME:")[1]
    usernames[client_socket] = username
    client_socket.sendall(f"Your shared key: {shared_key}\n".encode('utf-8'))
    print(f"[INFO] Sent shared key to {username} (Client {client_id}): {shared_key}")
    
    while True:
        try:
            # Terima pesan dari klien
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"[RECEIVED] Message from {username} (Client {client_id}): {message}")
                
                # Broadcast pesan ke klien lain
                full_message = f"{usernames[client_socket]}: {message}"
                for other_client in clients:
                    if other_client != client_socket:
                        other_client.sendall(full_message.encode('utf-8'))
                        print(f"[SENT] Message to {usernames[other_client]}: {full_message}")
            else:
                print(f"[INFO] {username} (Client {client_id}) disconnected.")
                break
        except Exception as e:
            print(f"[ERROR] Error handling {username} (Client {client_id}): {e}")
            break

    client_socket.close()
    clients.remove(client_socket)
    del usernames[client_socket]
    print(f"[INFO] Connection with {username} (Client {client_id}) closed and removed from list.")

def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(2)
    print("[START] Server is listening for connections...")

    clients = []
    usernames = {}  # Dictionary untuk menyimpan username

    while len(clients) < 2:
        client_socket, client_address = server_socket.accept()
        print(f"[CONNECTED] New client connected from {client_address}")
        clients.append(client_socket)
    
    shared_key = generate_random_key()
    print(f"[KEY] Generated shared key: {shared_key}")

    for i, client_socket in enumerate(clients):
        threading.Thread(target=handle_client, args=(client_socket, i + 1, shared_key, clients, usernames)).start()

if __name__ == "__main__":
    server_program()
