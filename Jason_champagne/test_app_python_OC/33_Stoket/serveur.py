#coding:utf-8
import socket
import threading

Class Threadforclient(threading.Thread):
    def__init__(self,conn):
        threading.Thread.__init__(self)
        self.conn = Conn
    def run(self):
        data = self.conn.recv(1024)
        data = data.decode("utf8")
        print(data)
#------------------------------------------------------------


host, port = ('', 2448)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind((host, port))
print("Le serveur est démarré.......")

while True:
    socket.listen()#<nom d échec accepté>
    conn, address = socket.accept()#address de connetion
    print("Un client vient de se connecter..............")

    #data = conn.recv(1024)
    #data = data.decode("utf8")
    
    my_thread = Threadforclient(conn)
    my_thread.start()
   

conn.close()
socket.close()