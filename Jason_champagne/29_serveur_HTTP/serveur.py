#coding:utf-8
import http.server

"""
import http.server
import socketserver

port = 80
address = ("",port)

handler = http.server.SimpleHTTPRequestHandler


httpd = socketserver.TCPServer(address, handler)

print(f"Serveur démarré sur le port {port}")

httpd.serve_forever()

"""

port = 80
address = ("",port)

server = http.server.HTTPServer


handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(address, handler)

print(f"serveur démarré sur le port {port} ")

httpd.serve_forever()