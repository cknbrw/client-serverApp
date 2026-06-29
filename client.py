import socket

HOST = '127.0.0.1'
PORT = 65432

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    msg = input("You: ")
    client.sendall(msg.encode())

    data = client.recv(1024)
    print("Server:", data.decode())

    if msg.lower() == "exit":
        break

client.close()