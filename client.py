import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

def receive_messages(client_socket, text_area, label):
    client_id = None
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                if message.startswith("Your shared key:"):
                    text_area.config(state='normal')
                    text_area.insert(tk.END, message + '\n')
                    text_area.config(state='disabled')
                elif message.startswith("You are Client"):
                    client_id = message.split()[-1]
                    label.config(text=f"You are Client {client_id}")
                else:
                    text_area.config(state='normal')
                    text_area.insert(tk.END, message + '\n')
                    text_area.config(state='disabled')
                    text_area.yview(tk.END)
            else:
                break
        except:
            break

def send_message(event=None):
    message = message_entry.get()
    if message:
        text_area.config(state='normal')
        text_area.insert(tk.END, f"You: {message}\n")
        text_area.config(state='disabled')
        text_area.yview(tk.END)
        
        client_socket.sendall(message.encode('utf-8'))
        
        message_entry.delete(0, tk.END)

def client_program():
    global client_socket, message_entry, text_area
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    window = tk.Tk()
    window.title("Chat Client")

    client_label = tk.Label(window, text="Connecting...")
    client_label.pack()

    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, state='disabled', width=50, height=20)
    text_area.pack(padx=10, pady=10)

    message_entry = tk.Entry(window, width=50)
    message_entry.pack(padx=10, pady=10)
    message_entry.bind("<Return>", send_message)

    threading.Thread(target=receive_messages, args=(client_socket, text_area, client_label), daemon=True).start()

    window.protocol("WM_DELETE_WINDOW", lambda: (client_socket.close(), window.destroy()))
    window.mainloop()

if __name__ == "__main__":
    client_program()
