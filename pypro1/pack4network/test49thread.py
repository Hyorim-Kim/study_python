# Thread 클래스 상속

import threading, time, sys

# threading.Thread 클래스를 상속하여 사용자 정의 스레드 클래스인 MyThread 생성
class MyThread(threading.Thread):
    def run(self):  # 스레드가 실행될 때 수행되는 메서드
        for i in range(1, 11):
            print('id={}--->{}'.format(threading.current_thread().name, i))
            time.sleep(0.2)

ths = []  # ths 리스트에 MyThread 클래스의 인스턴스를 생성하고, 각각의 스레드를 실행
for i in range(2):
    th = MyThread()
    th.start()
    ths.append(th)
    
for t in ths:  # 메인 스레드는 각 스레드가 종료될 때까지 대기
    t.join()
    
print('exit')
