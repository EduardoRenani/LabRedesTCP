#Import socket module
from socket import *
import sys #In order to terminate the program

if len(sys.argv) is not 2:
    print("Wrong format. Enter: python WebServer.py <port>")
    exit()

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = int(sys.argv[1])

# binds the socket to given port.
serverSocket.bind(('', serverPort))
# starts to listen for SYNACK 
serverSocket.listen(1)

print('The Server is ready to receive')

while 1:
    # Accepts new connections creating connection sockets 
    connectionSocket, addr = serverSocket.accept()
    # reads payload data
    sentence = connectionSocket.recv(4096)
    
    print('packet received')
