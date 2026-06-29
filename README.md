# client-serverApp
# Simple Client-Server Application
This project implements a simple client-server communication system using Python sockets. The application runs on localhost (127.0.0.1) and demonstrates how two processes communicate using TCP (Inter-Process Communication - IPC).

# System Architecture
The system follows a layered architecture:
 Presentation Layer: Handles user input/output via the terminal
 Application Layer: Processes messages and generates responses
 Transport Layer: Uses TCP sockets to enable communication
 
#  Technologies Used
 Python
 Socket Programming (TCP)
 Localhost (127.0.0.1)

# How to Run

 1. Start the Server
python server.py

 2. Start the Client (in a new terminal)
python client.py

# Example Communication
Client sends:
Hello server
Server responds:
Message received: Hello server

#  Testing
The application was tested by:
  Running both client and server locally
 Sending multiple messages
 Verifying responses from the server

#  Proof of Communication
Screenshots of successful communication between client and server are included in this repository.

# Features
 Real-time message exchange
 TCP-based communication
 Simple and easy to understand implementation

# conclusion

This project demonstrates a working client-server model using socket-based IPC, showing successful communication between two processes on a local machine.
