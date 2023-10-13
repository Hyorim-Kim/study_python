# singleton pattern
# cls : keyword

class SingletonClass:
    inst = None
    
    def __new__(cls):  # 객체의 생성을 담당. init에 의해 초기화됨
        if cls.inst is None:
            cls.inst = object.__new__(cls)
        return cls.inst
    
    def aa(self):
        print('난 메소드야')

class SubClass(SingletonClass):
    pass

s1 = SubClass()
s2 = SubClass()
print(id(s1), id(s2))  # 2619687503184 2619687503184 같은 주소

s1.aa()
s2.aa()

print('--------------------')
# 클래스의 멤버 변수를 고정
class Ani :
    __slots__ = ['name', 'age']
    
    def printData(self):
        print(self.name, self.age)

a = Ani()
a.name = '호랑이'
a.age = 3
# a.eat = '치킨'  # __slot__으로 멤버 변수에 제약을 걸었기 때문에 오류
a.printData()
