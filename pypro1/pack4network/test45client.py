# 단순 클라이언트

from socket import *
clientsock = socket(AF_INET, SOCK_STREAM)  # 클라이언트 소켓 객체를 생성
clientsock.connect(('127.0.0.1', 8888))  # 서버에 연결을 시도
clientsock.send('안녕 반가워'.encode('utf-8', errors='strict'))  # 서버에 메시지를 packet 단위에 담아 전송
clientsock.close()  # 연결을 종료
