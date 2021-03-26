import threading
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip = "IP"
port = 4444

b = input("Enter ip of b:")
b_port = 3333

s.bind((ip,port))

def send():
    while True:
        message = input()
        s.sendto(message.encode(),(b,b_port))

def receive():
    while True:
        message = s.recvfrom(1024) 
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"+message[0].decode())

thread1 = threading.Thread(target=send)
thread2 = threading.Thread(target=receive)

thread1.start()
thread2.start()

