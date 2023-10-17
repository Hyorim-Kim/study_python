# 멀티 채팅 프로그램 : socket, thread 사용
# 클라이언트

import socket
import threading
import sys

# 파이썬의 표준 출력은 자동으로 버퍼링이 됨
def handleMessage(socket):
    while True:
        data = socket.recv(1024)
        if not data:continue
        print(data.decode('utf-8'))
        #print(data.decode('utf-8'), flush = True)
    
sys.stdout.flush()  # 현재 버퍼에 저장된 내용을 출력장치로 내보내고 버퍼를 비움

name = input('채팅 이름 입력: ')
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(('192.168.0.14', 5555))
cs.send(name.encode('utf-8'))  # 채팅의 이름이 먼저 넘어감

th = threading.Thread(target=handleMessage, args=(cs,))
th.start()

while True:
    msg = input()
    sys.stdout.flush()
    if not msg:continue  # 메세지를 입력하지 않으면 계속 올라감
    cs.send(msg.encode('utf-8'))

cs.close()
