# 추상 클래스는 일종의 설계 도구로, 하위 클래스에게 어떤 메소드를 반드시 구현해야 하는지 알려주는 역할을 함

from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):  # 추상 클래스, 하위 클래스에서 반드시 구현해야 하는 메소드를 갖는다.
    def __init__(self, irum, nai):  # 모든 하위 클래스에서 공통적으로 사용되는 초기화 메소드
        self.irum = irum
        self.nai = nai
        
    @abstractmethod
    def pay(self):  # 추상 메소드, 하위 클래스에서 구현되어야 함
        pass
    
    @abstractmethod
    def data_print(self):  # 추상 메소드
        pass
    
    def irumnai_print(self):
        print('이름 : ' + self.irum + ', 나이 : ' + str(self.nai), end=' ')
    