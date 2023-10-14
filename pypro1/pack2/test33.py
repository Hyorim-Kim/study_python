# 추상 클래스는 하위 클래스에서 반드시 구현해야 하는 메소드를 지정하는 역할
# 객체 개념 이해해야함

from abc import ABCMeta, abstractmethod

class Friend(metaclass=ABCMeta):  # 추상 클래스
    def __init__(self, name):  # 모든 Friend 객체가 가져야 할 공통 속성인 name을 초기화
        self.name = name
    
    @abstractmethod
    def hobby(self):  # 추상 메소드
        pass

    def printName(self):
        print('이름은 ' + self.name)


class John(Friend):  # Friend 클래스를 상속받는 클래스
    def __init__(self, name, addr):
        Friend.__init__(self, name)  # Friend 클래스의 __init__ 메소드를 호출, UnBound call
        self.addr = addr  # 추가로 addr 속성을 초기화

    def hobby(self):
        print(self.addr + ' 거리를 산책함')

    def printAddr(self):
        print('주소는 ' + self.addr)


class Chris(Friend):  # Friend 클래스를 상속받는 클래스
    def __init__(self, name, addr):
        super().__init__(name)  # 부모 클래스의 초기화 메소드를 호출
        self.addr = addr  # addr 속성을 초기화

    def hobby(self):
        print(self.addr + ' 동네를 어슬렁 거림')
        print(self.addr + '에 오래 전부터 살고 있다')


john = John('미스터 존', '역삼1동')  # 생성자 호출, John 클래스 type의 새로운 객체 생성
john.printName()  # 객체의 메소드를 호출하여 동작을 확인
john.printAddr()
john.hobby()
print()
chris = Chris('크리스 님', '역삼2동')  # 생성자 호출, Chris 클래스 type의 새로운 instance 생성
chris.printName()
chris.hobby()
print('-----------')
fri = john  # fri 변수가 John 객체와 Chris 객체를 참조
fri.hobby()  # 어떤 클래스의 hobby 메소드가 호출되는지는 변수 fri가 현재 참조하는 객체의 타입에 따라 달라짐
print()
fri = chris
fri.hobby()
