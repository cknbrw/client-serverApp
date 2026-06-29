import socket

HOST = '127.0.0.1'
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server started... Waiting for connection")

conn, addr = server.accept()
print("Connected by:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break

    message = data.decode()
    print("Client:", message)

    reply = "Message received: " + message
    conn.sendall(reply.encode())

    if message.lower() == "exit":
        break

conn.close()
server.close()