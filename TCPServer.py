from socket import *
serverPort = 12000
severSocket = socket(AF_INET,SOCK_STREAM)
severSocket.bind(('',serverPort))
severSocket.listen(1)
print ('the server is ready to receive')
while True:
    connectionSocket, addr = severSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encoder())
    connectionSocket.close()