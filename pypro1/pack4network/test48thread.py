# Thread를 이용해 날짜 및 시간 출력
import time

now = time.localtime()
# print(now)
print('오늘은 {0}년 {1}월 {2}일 {3}요일'.format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_wday))  # 월:0 ~ 일:6
print('현재 {0}시 {1}분 {2}초'.format(now.tm_hour, now.tm_min, now.tm_sec))

print('---------------')
import threading

def calendar_show():  # 현재 날짜 및 시간을 출력
    now = time.localtime()
    print('오늘은 {0}년 {1}월 {2}일 {3}요일'.format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_wday))
    print('현재 {0}시 {1}분 {2}초'.format(now.tm_hour, now.tm_min, now.tm_sec))

def myRun():  # calendar_show 함수를 계속해서 실행하는 무한 루프를 포함
    while True:
        now2 = time.localtime()
        if now2.tm_min == 48:break  # 루프를 탈출
        calendar_show()
        time.sleep(1)

#th = threading.Thread(target=calendar_show)
th = threading.Thread(target=myRun)  # myRun 함수를 실행할 대상으로 지정한 스레드 th를 생성
th.start()  # 스레드를 실행

th.join()  # 메인 스레드는 th 스레드가 종료될 때까지 대기
print('프로그램 종료')
