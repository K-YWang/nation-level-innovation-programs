import socket
from tkinter import Tk
from tkinter.filedialog import askdirectory
import os

Tk().withdraw()  # 不显示Tkinter的主窗口
directory_path = askdirectory()  # 弹出对话框让用户选择文件夹

if not directory_path:
    print("No directory selected. Exiting...")
    exit()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8899))

# 接收文件名和文件大小
# 初始化一个空字符串来收集接收到的信息
received_info = ''
while True:
    part = client_socket.recv(4096).decode()
    received_info += part
    if received_info.endswith('\n'):
        break

file_name, file_size = received_info[:-1].split('|')  # 去掉最后的换行符再分割


# 在指定的目录下创建文件
file_path = os.path.join(directory_path, file_name)
with open(file_path, 'wb') as file:
    remaining = int(file_size)
    while remaining:
        data = client_socket.recv(min(4096, remaining))
        if not data: break
        file.write(data)
        remaining -= len(data)

print("File has been received and saved successfully.")
client_socket.close()
