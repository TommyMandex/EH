import socket as socket

host = "localhost" # or you can use "127.0.0.0"
port = 7777

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host, port))

