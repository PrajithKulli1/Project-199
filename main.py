import socket
from threading import Thread
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port=8000
server.bind((ip_address, port))
server.listen()
list_of_clients = []
print("server has started")

def clientThread(conn,addr):
    conn.send("Welcome to the chat room".encode("utf-8"))
    while True:
        try:
            message=conn.recv(2048).decode("utf-8")
            if message:
                broadCast(message,conn)
            else:
                remove(conn)
        except:
            continue

def broadCast(message,connection):
    for client in list_of_clients:
        if client != connection:
            try:
                client.send(message.encode("utf-8"))
            except:
                remove(client)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    conn,addr=server.accept()
    list_of_clients.append(conn)
    print(addr[0]+ "connected")
    new_thread = Thread(target=clientThread,args=(conn,addr))
    new_thread.start()