# Thread를 사용하여 간단한 멀티태스킹을 구현
# from subprocess import *

# Popen('calc.exe')  # 응용 프로그램 독립적으로 실행
# call('calc.exe')
# print('계속')
# print('종료')


# Thread(light weight process라고도 함) 처리, 멀티태스킹처럼 사용
# 시작, 실행, 종료의 세 단계로 구성됨
import threading, time

def run(id):  # 주어진 id에 대해 1부터 10까지 숫자를 출력하고, 각 출력 사이에 0.5초의 딜레이를 줌
    for i in range(1, 11):
        print('id={}--->{}'.format(id, i))
        time.sleep(0.5)  # 0.5초마다 한번씩 비활성화 <--> timeout    # wait() <--> notify()

# 사용자 정의 thread를 사용하지 않은 경우 : 순차적으로 실행됨
# run(1)
# run(2)

# 사용자 정의 thread를 사용한 경우 : 비순차적으로 실행됨
# threading.Thread를 사용하여 두 개의 스레드(th1과 th2)를 생성,
# 각각에게 run 함수를 실행할 대상으로 지정
th1 = threading.Thread(target=run, args=('일'))
th2 = threading.Thread(target=run, args=('둘'))
th1.start()  # 각 스레드를 실행
th2.start()

th1.join()  # 해당 스레드가 진행되는 동안 메인 스레드는 대기 요청
th2.join()
print('프로그램 종료(메인 모듈은 자동으로 지원된 메인 스레드에 의해 실행)')
# 메인 포함 총 3개의 스레드 존재함
# th1과 th2 스레드가 병렬로 실행되며, 메인 스레드는 두 스레드가 종료될 때까지 대기한 후에 종료
