# thread의 활성화, 비활성화
# 생산자(Maker)와 소비자(Consumer) 간의 빵 공급과 소비를 스레드를 통해 구현
import threading

bread_plate = 0  # 빵 접시 : 빵이 담겨있는 공유 자원
lock = threading.Condition()  # Lock을 위한 조건변수 생성

class Maker(threading.Thread):  # threading.Thread를 상속받아 스레드를 생성하는 클래스
    def run(self):  # 빵 생산
        global bread_plate
        for _ in range(30):
            lock.acquire()  # Critical Section을 보호
            while bread_plate >= 10:
                print('빵 생산 초과로 대기')
                lock.wait()  # 스레드의 비활성화
                
            bread_plate += 1  # bread_plate 위에 올라간 빵
            print('빵 생산 수 : ', bread_plate)
            lock.notify()  # 스레드의 활성화
            lock.release()  # Critical Section을 보호

class Consumer(threading.Thread):  # threading.Thread를 상속받아 스레드를 생성하는 클래스
    def run(self):  # 빵 소비
        global bread_plate
        for _ in range(30):
            lock.acquire()  # Critical Section을 보호
            while bread_plate < 1:
                print('빵이 없어 기다림...')
                lock.wait()  # 스레드의 비활성화
                
            bread_plate -= 1  # bread_plate 위에 올라간 빵
            print('빵 소비 후 남은 수 : ', bread_plate)
            lock.notify()  # 스레드의 활성화
            lock.release()  # Critical Section을 보호

# Maker와 Consumer의 인스턴스를 리스트에 추가하고,
mak = []; con = []
for i in range(5):
    mak.append(Maker())
for i in range(5):
    con.append(Consumer())
    
# 각각을 실행하여 빵 생산과 소비를 동시에 진행
for th1 in mak:
    th1.start()
for th2 in con:
    th2.start()

# 각 스레드가 종료될 때까지 기다린 후 메인 스레드 종료
for th1 in mak:
    th1.join()
for th2 in con:
    th2.join()
    
print('프로그램 종료')
