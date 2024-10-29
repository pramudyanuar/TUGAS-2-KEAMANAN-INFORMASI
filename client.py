import socket
import threading
from tkinter import *
from tkinter import scrolledtext, messagebox
from des import encryption_large_text, decryption_large_text

# Variabel untuk menyimpan shared key dan username
shared_key = None
username = None

def connect_to_server():
    global client_socket, username

    username = username_entry.get()
    if not username:
        messagebox.showerror("Error", "Username cannot be empty!")
        return

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 12345))

        # Kirim username ke server
        client_socket.sendall(f"USERNAME:{username}".encode('utf-8'))

        # Masuk ke tampilan chat setelah login berhasil
        login_frame.pack_forget()
        chat_frame.pack(fill=BOTH, expand=True)

        # Mulai thread untuk menerima pesan dari server
        threading.Thread(target=receive_message).start()
    except Exception as e:
        messagebox.showerror("Error", f"Could not connect to server: {e}")

def send_message():
    global shared_key
    if shared_key is None:
        chat_display.insert(END, "Waiting for shared key...\n")
        return
    
    message = message_entry.get()
    if message:
        encrypted_message = encryption_large_text(message, shared_key)
        client_socket.sendall(encrypted_message.encode('utf-8'))
        chat_display.insert(END, f"You: {message}\n")
        message_entry.delete(0, END)

def receive_message():
    global shared_key
    while True:
        try:
            receive = client_socket.recv(1024).decode('utf-8')
            if receive:
                if "Your shared key:" in receive:
                    # Mengambil shared key dari pesan server
                    shared_key = receive.split(": ")[1].strip()
                    chat_display.insert(END, f"Received shared key: {shared_key}\n")
                else:
                    # Memisahkan username dan pesan terenkripsi
                    if ": " in receive:
                        sender, encrypted_message = receive.split(": ", 1)
                        message = decryption_large_text(encrypted_message, shared_key)
                        chat_display.insert(END, f"{sender}: {message}\n")
                    else:
                        chat_display.insert(END, f"Unknown message format: {receive}\n")
            else:
                break
        except Exception as e:
            chat_display.insert(END, f"Error receiving message: {e}\n")
            break

def on_closing():
    client_socket.close()
    root.destroy()

# Inisialisasi GUI
root = Tk()
root.title("Chat App")
root.geometry("400x500")

# Frame untuk login
login_frame = Frame(root)
login_frame.pack(fill=BOTH, expand=True)

Label(login_frame, text="Enter your username:", font=("Arial", 12)).pack(pady=10)
username_entry = Entry(login_frame, font=("Arial", 12))
username_entry.pack(pady=10)

login_button = Button(login_frame, text="Login", command=connect_to_server)
login_button.pack(pady=5)

# Frame untuk chat
chat_frame = Frame(root)

chat_display = scrolledtext.ScrolledText(chat_frame, wrap=WORD, font=("Arial", 12))
chat_display.pack(padx=10, pady=10, fill=BOTH, expand=True)
chat_display.config(state=NORMAL)

message_frame = Frame(chat_frame)
message_frame.pack(fill=X, padx=10, pady=5)

message_entry = Entry(message_frame, font=("Arial", 12))
message_entry.pack(side=LEFT, fill=X, expand=True, padx=(0, 5))
message_entry.bind("<Return>", lambda event: send_message())

send_button = Button(message_frame, text="Send", command=send_message)
send_button.pack(side=RIGHT)

# Tutup koneksi saat aplikasi ditutup
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
