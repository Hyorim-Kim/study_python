# 추상 클래스를 이용한 상속 연습 문제 (4번)
# super class
from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai
        
    @abstractmethod
    def pay(self):
        pass
    
    @abstractmethod
    def data_print(self):
        pass
    
    def irumnai_print(self):
        print('이름 : ' + self.irum + ', 나이 : ' + str(self.nai), end=' ')
    