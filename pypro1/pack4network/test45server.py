# 단순 서버 : 접속 상태 확인용으로 1개의 접속만 처리

from socket import *
serversock = socket(AF_INET, SOCK_STREAM)  # socket(소켓종류, 소켓유형)  # 서버 소켓 객체를 생성
serversock.bind(('127.0.0.1', 8888))  # tuple type의 argument(호스트명, 포트번호), 서버 소켓을 특정 주소와 포트에 바인딩
serversock.listen(1)  # 클라이언트와 동시 연결 정보 수 (1 ~ 5)
print('서버 서비스 중 ...')

conn, addr = serversock.accept()  # 연결 대기(Blocking)
print('client addr : ', addr)
print('from client message : ', conn.recv(1024).decode())  # 1kb가 기본
conn.close()  # client와 통신하는 socket
serversock.close()
