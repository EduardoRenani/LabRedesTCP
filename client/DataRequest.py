from socket import *
import time

PAYLOAD_SIZE = 4096
MEGA = 10**6

if len(sys.argv) is not 3:
    print("Wrong format. Enter: python DataRequest.py <ip> <port>")
    exit()

serverName = sys.argv[1]
serverPort = int(sys.argv[2])

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))


payload = bytearray(PAYLOAD_SIZE)

while 1:
    # time when the signal is sent
    t1 = time.time()
    # send data
    clientSocket.send(payload)
    # time when ACK from server is received
    t2 = time.time()

    rtt = t2-t1
    oneWayTripTime = (rtt/2)

    megaBitsPayloadSize = PAYLOAD_SIZE*8/MEGA

    print("Transfer Rate: ", megaBitsPayloadSize/oneWayTripTime, "Mbits/s")

clientSocket.close()