# 단순 클라이언트

from socket import *
clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('127.0.0.1', 8888))
clientsock.send('안녕 반가워'.encode('utf-8', errors='strict'))  # packet 단위에 담아 전송
clientsock.close()
