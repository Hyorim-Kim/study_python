# 멀티 채팅 프로그램 : socket, thread 사용
# 서버

import socket
import threading

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('192.168.0.14', 5555))
ss.listen(5)
print('채팅 서버 서비스 중...')
users = []

def chatUser(conn):
    name = conn.recv(1024)
    data = '♥ ♡ ' + name.decode('utf-8') + '님 입장~~~'
    print(data)
    
    try:
        for u in users:
            u.send(data.encode('utf-8'))
        
        # 채팅 수행
        while True:
            msg = conn.recv(1024)
            if not msg:continue
            cdata = name.decode('utf-8') + '님의 메세지 : ' + msg.decode('utf-8')
            print('수신 자료 : ', cdata)
            for u in users:
                u.send(cdata.encode('utf-8'))      
    except:
        users.remove(conn)  # list에서 뺌(채팅방을 나감)
        data = 'ㅠㅠ ' + name.decode('utf-8') + '님 퇴장!'  # client 컴퓨터에 메세지 전송
        print(data)  # server에 출력
        if users:
            for u in users:
                u.send(data.encode('utf-8'))
        else:
            print('exit')
        
while True:
    conn, addr = ss.accept()  # 때문에 멈춤, client가 입장하는 순간 users에 들어옴
    users.append(conn)
    th = threading.Thread(target=chatUser, args=(conn,))  # args는 현재 접속한 클라이언트(conn)
    th.start()
