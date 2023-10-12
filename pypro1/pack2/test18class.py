# 모듈의 멤버 중 클래스
# 클래스는 새로운 이름 공간을 지원하는 단위로 메소드와 변수라는 멤버를 지닌다.
# 클래스는 이름 공간과 클래스가 생성하는 인스턴스 이름공간을 각각 갖는다.
# 접근지정자는 없다. 메소드 오버로딩도 없다.

class TestClass:  # header이며 이하 소스는 body 영역이 된다.
    aa = 1  # 멤버변수는 클래스 내에서 전역
    
    def __init__(self):  # 메소드의 첫 파라미터는 self(this와 비슷한 개념)
        print('생성자')  # 클래스가 진행되기 전에 클래스의 초기화를 하는 역할 / 생략 가능
        
    def __del__(self):
        print('소멸자')  # 클래스 종료 전 마무리 작업을 하는 역할(GC가 있기 때문에 자주 사용하지는 않는다) / 생략 가능
        
    def printMsg(self):  # 멤버 메소드
        name = '한국인'  # 지역변수
        print(name)
        print(self.aa)  # 전역변수 aa 이용하기 위해 self 사용(자바의 this와 비슷)

test = TestClass()  # 생성자를 호출 후 인스턴스가 만들어짐(new와 비슷), 만들어진 인스턴스를 object(객체)라 부름 (eg.객체변수 test)
print(test.aa)
# method call
test.printMsg()  # 방법1 : Bound method call  # 객체변수가 자동으로 괄호 안으로 들어감
TestClass.printMsg(test)  #방법2 : UnBound method call(클래스 메소드의 이름으로 부름)
print()

print(isinstance(test, TestClass))  # True
print(type(1))
print(type(test))
print(id(test), id(TestClass))  # 2683131463248 2683132847424

del test  # 인스턴스 삭제
