# 단순 서버 : 접속 상태 확인용으로 1개의 접속만 처리

from socket import *
serversock = socket(AF_INET, SOCK_STREAM)  # 서버 소켓 객체를 생성  # socket(소켓종류, 소켓유형)
serversock.bind(('127.0.0.1', 8888))  #  서버 소켓을 특정 주소와 포트에 바인딩  # tuple type의 argument(호스트명, 포트번호)
serversock.listen(1)  # 클라이언트와 동시에 처리할 수 있는 연결 수 (1 ~ 5)
print('서버 서비스 중 ...')

conn, addr = serversock.accept()  # 클라이언트의 연결 요청을 기다리고, accept()를 호출하여 클라이언트와 연결을 수락
print('client addr : ', addr)
print('from client message : ', conn.recv(1024).decode())  # 클라이언트로부터 메시지를 수신  # 1kb(1024)가 기본
conn.close()  # client와 통신하는 socket 종료
serversock.close()
