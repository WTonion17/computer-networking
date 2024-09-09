from socket import *
serverName = '192.168.34.92'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print ('From Server:', modifiedSentence.decode())
clientSocket.close()

# import socket

# # Server information (use the same IP and port as the server)
# HOST = '10.10.30.132'  # Server's IP address (localhost for local testing)
# PORT = 12000        # Server's listening port

# # Create a TCP/IP socket
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
#     # Connect to the server
#     client_socket.connect((HOST, PORT))
    
#     # Send a message to the server
#     message = "Hello, Server! This is the client."
#     print(f"Sending to server: {message}")
#     client_socket.sendall(message.encode('utf-8'))  # Send message as bytes
    
#     # Receive a response from the server
#     data = client_socket.recv(1024)
#     print(f"Received from server: {data.decode('utf-8')}")