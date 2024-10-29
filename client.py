import socket
import threading
from des import encryption_large_text, decryption_large_text

# Variabel untuk menyimpan shared key
shared_key = None

def send_message(client_socket):
    global shared_key
    while True:
        try:
            # Tunggu hingga shared_key diterima
            if shared_key is None:
                continue
            
            inp = input("")
            message = encryption_large_text(inp, shared_key)
            client_socket.sendall(message.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            client_socket.close()
            break

def receive_message(client_socket):
    global shared_key
    while True:
        try:
            receive = client_socket.recv(1024).decode('utf-8')
            if receive:
                if "Your shared key:" in receive:
                    # Mengambil shared key dari pesan server
                    shared_key = receive.split(": ")[1].strip()
                    print(f"Received shared key: {shared_key}")
                else:
                    # Memisahkan username dan pesan terenkripsi
                    if ": " in receive:
                        sender, encrypted_message = receive.split(": ", 1)
                        message = decryption_large_text(encrypted_message, shared_key)
                        print(f"{sender}: {message}")
                    else:
                        print("Format pesan tidak dikenal:", receive)
            else:
                break
        except Exception as e:
            print(f"Error receiving message: {e}")
            break


def client_program():
    username = input("Enter your username: ")  # Minta username dari pengguna

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    # Kirim username ke server
    client_socket.sendall(f"USERNAME:{username}".encode('utf-8'))

    # Mulai thread untuk menerima pesan dari server
    threading.Thread(target=receive_message, args=(client_socket,)).start()
    # Mulai thread untuk mengirim pesan ke server
    threading.Thread(target=send_message, args=(client_socket,)).start()

# Menjalankan client
if __name__ == "__main__":
    client_program()
