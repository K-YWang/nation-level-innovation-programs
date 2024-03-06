import socket
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()  # 不显示Tkinter的主窗口
file_path = askopenfilename()  # 弹出对话框让用户选择文件

if not file_path:
    print("No file selected. Exiting...")
    exit()

file_name = os.path.basename(file_path)
file_size = os.path.getsize(file_path)

server_address = ('localhost', 8899)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)

print("Waiting for connection...")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# 先发送文件名和文件大小
conn.sendall(f"{file_name}|{file_size}\n".encode())

# 然后发送文件内容
with open(file_path, 'rb') as file:
    while True:
        data = file.read(4096)
        if not data:
            break
        conn.sendall(data)

print("File has been sent successfully.")
conn.close()
