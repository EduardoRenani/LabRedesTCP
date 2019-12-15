#Import socket module
from socket import *
import sys 
import os
import time, datetime
import threading
import csv

PAYLOAD_SIZE = 4096 #bytes
TIME_WINDOW = 2 #seconds
MEGA = 10**6
class PayloadSize:
    def __init__(self, size):
        self.size = size

class Timer (threading.Thread):
    def __init__(self, delay, payloadSize):
        threading.Thread.__init__(self)
        self.delay = delay
        self.payloadSize = payloadSize
      
    def run(self):
        with open('log.csv', 'w') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"')
            try: 
                while 1:
                    initialBufferSize = self.payloadSize.size
                    time.sleep(self.delay)
                    afterBufferSize = self.payloadSize.size

                    amountOfData = afterBufferSize - initialBufferSize
                    megaBitsAmountOfData = (amountOfData*8)/(10**6)
                    transferRate = megaBitsAmountOfData/self.delay

                    writer.writerow([os.getpid(), datetime.datetime.now().isoformat(), transferRate])
                    file.flush()
                    print('Transfer rate: ', transferRate, 'Mbits/s')
            
            except KeyboardInterrupt:
                file.close()
                print("Server stopped")

class ConnectionHandler(threading.Thread):
    def __init__(self, newConnectionSocket, addr):
        threading.Thread.__init__(self)
        self.socket = socket
        self.name = addr

    def run(self):
        payloadSize = PayloadSize(0)
        timer = Timer(TIME_WINDOW, payloadSize)
        timer.start()
        while 1:
            payload = connectionSocket.recv(PAYLOAD_SIZE)
            payloadSize.size = payloadSize.size + sys.getsizeof(payload)



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
serverSocket.listen(10)

print('The Server is ready to receive')

while 1:
    # Accepts new connections creating connection sockets 
    connectionSocket, addr = serverSocket.accept()
    
    # create new thread to handler different connections
    connectionHandler = ConnectionHandler(connectionSocket, addr)
    connectionHandler.start()
