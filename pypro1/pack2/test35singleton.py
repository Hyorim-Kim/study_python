# singleton pattern : 객체가 하나만 생성되도록 하는 디자인 패턴
# 여러번 객체를 생성하더라도 항상 동일한 객체를 반환한다.
# cls : keyword

class SingletonClass:
    inst = None  # 클래스 변수
    
    def __new__(cls):  # 객체의 생성을 담당. (__init__ 메소드는 초기화를 담당)
        if cls.inst is None:  # 클래스 변수 inst를 사용해서 이미 객체가 생성되었는지 여부를 확인하고,
            cls.inst = object.__new__(cls)  # 생성되지 않았다면 object.__new__(cls)를 통해 객체를 생성
        return cls.inst  #  그 객체를 반환
    
    def aa(self):
        print('난 메소드야')

class SubClass(SingletonClass):  # SingletonClass를 상속받음, 싱글톤 패턴을 따름
    pass

s1 = SubClass()  # SubClass의 객체를 생성, __new__ 메소드가 호출되어 객체가 생성됨
s2 = SubClass()  # 또 다른 객체를 생성
print(id(s1), id(s2))  # 2619687503184 2619687503184 같은 주소임, 동일한 객체를 가리킴

s1.aa()
s2.aa()

print('--------------------')
# __slots__ 클래스의 멤버 변수를 고정
class Ani :
    __slots__ = ['name', 'age']
    # __slots__ : 클래스가 허용하는 속성을 제한
    # 여기서는 Ani 클래스가 name과 age 속성만을 허용하도록 제한
    
    def printData(self):
        print(self.name, self.age)

a = Ani()  # Ani 클래스의 객체를 생성
a.name = '호랑이'
a.age = 3
# a.eat = '치킨'  # __slot__때문에 추가 속성을 할당하려고 하면 오류가 발생
a.printData()
