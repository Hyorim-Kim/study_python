# 스레드 간 자원 공유 : 충돌 방지위해 동기화 사용
# g_count가 중복되면 충돌된 것
# 하나의 스레드가 공유자원을 사용중일 때는 나머지 스레드가 공유자원을 쓰지 않아야 함 -> 충돌 발생 방지

# from threading import *
# from time import *

import threading, time

g_count = 0  # 전역변수는 자동으로 스레드의 공유 자원이 됨

lock = threading.Lock()

def threadCount(id, count):
    global g_count
    for i in range(count):  # count 지역변수
        lock.acquire()  # 임의의 스레드가 공유자원 사용 시 다른 스레드는 대기 상태 *******
        print('id %s ==> count:%s, g_count:%s'%(id, i, g_count))
        g_count = g_count + 1
        lock.release()  # 대기 상태를 해제 *******

for i in range(1, 6):
    threading.Thread(target=threadCount, args=(i, 5)).start()

time.sleep(1)  # join 안쓰려고
print('최종 g_count : ', g_count)
print('프로그램 종료')
