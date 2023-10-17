# 지속적으로 클라이언트와 통신을 유지하는 서버
import socket
import sys

HOST = '127.0.0.1'
PORT = 6666

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 서버 소켓 객체를 생성

try:
    serversock.bind((HOST, PORT))  # 서버 소켓을 특정 주소와 포트에 바인딩
    serversock.listen(5)  # 최대 5개의 클라이언트 연결 요청을 대기하도록 설정
    print('서버 서비스 진행 중 ...')
    
    while True:  # 루프
        conn, addr = serversock.accept()  # 클라이언트의 연결을 기다리고, 연결이 수락되면
        print('client info : ', addr[0], addr[1])  # 클라이언트의 정보를 출력하고
        print(conn.recv(1024).decode())  # 메시지를 수신하여 출력
        
        # 메세지 송신 : 수신한 메시지에 대한 응답을 클라이언트에게 전송
        conn.send(('from server : ' + str(addr[1]) + ' 서버가 전송함').encode('utf-8'))
        
except socket.error as err:
    print('err : ', err)
    sys.exit()
finally:    
    pass
