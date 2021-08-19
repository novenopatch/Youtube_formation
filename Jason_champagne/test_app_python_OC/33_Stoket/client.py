#coding:utf-8
import socket

host, port = ('127.0.0.1', 2448)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.connect((host, port))
    print("Client connecté")


    data = "Bonjour à toi, je suis le client !:)"
    data = data.encode("utf8")
    socket.sendall(data)

except ConnectionResetError:
        print("Problème connection au serveur échoué")
finally:
    socket.close()