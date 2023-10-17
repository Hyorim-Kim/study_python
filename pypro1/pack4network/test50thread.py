# 스레드 간 자원 공유 : 충돌 방지 위해 threading.Lock(동기화)을 사용
# 공유 자원인 g_count가 중복되면 충돌한 것
# 하나의 스레드가 공유자원을 사용중일 때는 나머지 스레드가 공유자원을 쓰지 않아야 함 -> 충돌 방지

# from threading import *
# from time import *

import threading, time

g_count = 0  # 전역변수는 자동으로 스레드의 공유 자원이 됨

lock = threading.Lock()  # Lock 객체를 생성

def threadCount(id, count):
    global g_count
    for i in range(count):  # count 지역변수
        lock.acquire()  # 임의의 스레드가 공유자원 사용 시 다른 스레드는 대기 상태 *******
        print('id %s ==> count:%s, g_count:%s'%(id, i, g_count))
        g_count = g_count + 1
        lock.release()  # 대기 상태를 해제 *******

for i in range(1, 6):  # 5개의 스레드를 생성
    threading.Thread(target=threadCount, args=(i, 5)).start()
# threadCount 함수를 실행할 대상으로 지정, 인자로 스레드의 id와 반복 횟수를 전달

time.sleep(1)  # join 안쓰려고, 메인 스레드가 1초 동안 대기(메인 스레드 종료 방지)
print('최종 g_count : ', g_count)
print('프로그램 종료')
# Lock을 사용하면 여러 스레드 간에 공유 자원을 안전하게 사용할 수 있다.
