# python에서 thread는 GIL(Global Interpreter Lock) 정책을 따른다.
# 그러므로 병렬식 처리가 불가해 하나의 스레드에서 일정 시간 작동할 때, 다른 스레드는 작동이 멈추게 된다.
# 즉, thread의 성능이 제대로 발휘되지 않는다.
# 그래서 python은 multiprocessing 모듈로 threading 모듈과 유사한 API를 사용해 process를 지원하게 된다.
# multiprocessing은 비동기적이고 부분 작업 활동이 비결정적(무작위, 예측 불가)인 경우에 효과적이다.
# 주로 네트워크 작업에서 많이 사용된다.
# multiprocessing은 대표적으로 Pool(주로 사용)과 Process를 이용하여 하나 이상의 자식 process를 생성한 후 병렬 구조로 처리한다.

# Pool 클래스는 입력값에 대해 process를 건너건너 분배하여 함수 실행을 병렬화 한다.
from multiprocessing import Pool, Process
import time
import os

def func(x):
    print('값', x, '에 대한 작업 pid = ', os.getpid())
    time.sleep(1)
    return x * x

# print(func(5))

if __name__ == '__main__':
    '''
    startTime = int(time.time())
    # 실습 1 : 일반적인 방법으로 함수를 호출
    for i in range(0, 10):
        print(func(i))  # 값 0에 대한 작업 pid = 15380 직렬 처리
    endTime = int(time.time())
    print('총 작업 시간 : ', (endTime - startTime))
   '''
    # 실습 2 : Pool 클래스로 함수 호출 --> 속도가 빨라짐, 자원을 많이 소모
    startTime = int(time.time())
    
    p = Pool(processes=3)  # Pool(process의 개수)  3 ~ 5개가 적당
    print(p.map(func, range(0, 10)))  # mapping(0-func, 1-func, ...)  # 병렬 처리
          
    endTime = int(time.time())
    print('총 작업 시간 : ', (endTime - startTime))
