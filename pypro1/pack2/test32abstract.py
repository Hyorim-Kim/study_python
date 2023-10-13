# 추상 클래스 : 추상 메소드를 한 개라도 갖고 있다면 추상 클래스
# 추상은 다형성 때문에 존재함 -> 다형성 override -> override 강요
# 상속 -> 오버라이딩 -> 추상 흐름 알기
# 다이어그램 그리면서 정리하기

from abc import abstractmethod, ABCMeta

class AbstractClass(metaclass=ABCMeta): # 추상 클래스 - 객체 생성 불가
    @abstractmethod  # decorator, metaclass 적어줘야함
    def abcMethod(self):  # 추상 메소드
        pass

    def normalMethod(self):
        print('추상 클래스 내의 일반 메소드')

# parent = AbstractClass()  # error, 추상클래스는 부모로서의 의미만 있다.
# TypeError: Can't instantiate abstract class AbstractClass with abstract method abcMethod

# class Child1(AbstractClass):
#     pass
#
# c1 = Child1()  # error, 객체 생성 불가
# TypeError: Can't instantiate abstract class Child1 with abstract method abcMethod

class Child1(AbstractClass):  # override 안하면 에러 떨어짐
    name = '난 Child1'
    
    def abcMethod(self):
        print('Child1에서 추상 메소드를 오버라이드 함 : 순전히 강요 때문에')

c1 = Child1()
print(c1.name)
c1.abcMethod()
c1.normalMethod()  # Child1에서 찾지만 없어서 부모에게 올라감

print()
class Child2(AbstractClass):
    def abcMethod(self):  # override 강요
        print('Child2에서 추상 메소드를 재정의함')
        print('추상의 마법에서 벗어남')

    def normalMethod(self):  # override 선택
        print('추상 클래스의 일반 메소드를 재정의 함')
        
c2 = Child2()
c2.abcMethod()
c2.normalMethod()

print('\n다형성 -----')
good = c1
good.abcMethod()
good.normalMethod()
print()
good = c2
good.abcMethod()
good.normalMethod()
