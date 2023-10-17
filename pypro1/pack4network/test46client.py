from socket import *
clientsock = socket(AF_INET, SOCK_STREAM)  # 클라이언트 소켓 객체를 생성
clientsock.connect(('127.0.0.1', 6666))  # 서버에 연결을 시도
clientsock.send('안녕 반가워'.encode('utf-8'))  # 서버에 메시지를 전송
re_msg = clientsock.recv(1024).decode()  # 서버로부터의 응답을 받아
print('수신 자료 : ' + re_msg)  # 출력
clientsock.close()