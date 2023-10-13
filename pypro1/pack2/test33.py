# 추상
# 객체 이해해야함

from abc import ABCMeta, abstractmethod

class Friend(metaclass=ABCMeta):  # 추상 클래스가 됨
    def __init__(self, name):
        self.name = name  # chris 원형 클래스가 아니라 chris 타입의 주소를 받음 ??
    
    @abstractmethod
    def hobby(self):  # 추상 메소드
        pass

    def printName(self):
        print('이름은 ' + self.name)


class John(Friend):  # friend 상속 받음
    def __init__(self, name, addr):
        Friend.__init__(self, name)  # UnBound call, name은 부모에게 받음
        self.addr = addr

    def hobby(self):
        print(self.addr + ' 거리를 산책함')

    def printAddr(self):
        print('주소는 ' + self.addr)


class Chris(Friend):  # friend 상속 받음
    def __init__(self, name, addr):
        super().__init__(name)
        self.addr = addr

    def hobby(self):
        print(self.addr + ' 동네를 어슬렁 거림')
        print(self.addr + '에 오래 전부터 살고 있다')


john = John('미스터 존', '역삼1동')  # 생성자 호출, john이 아니라 john type의 새로운 객체
john.printName()
john.printAddr()
john.hobby()
print()
chris = Chris('크리스 님', '역삼2동')  # 생성자 호출, chris type의 새로운 instance
chris.printName()
chris.hobby()  # chris 타입의 새로운 객체 호출
print('-----------')
fri = john
fri.hobby()
print()
fri = chris
fri.hobby()
