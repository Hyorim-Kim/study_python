# class 멤버 호출 관련

kor = 100  # 모듈의 멤버로서 class MyClass 전체와 동급이다.  파이썬은 함수 지향적 언어로, 클래스는 모듈의 멤버이다.

def abc():
    print('모듈의 멤버 함수')

class MyClass:
    kor = 90
    
    # 생성자 생략
       
    def abc(self):
        print('abc 메소드')
        
    def show(self):
        # kor = 80
        # print(self.kor)  # 전역 변수 kor 찾음
        print(kor)  # show 메소드에 있는 지역변수 kor = 80을 찾음, 없으면 모듈 변수를 찾음  # 변수 호출 순서 : 지역변수 > 모듈변수
        self.abc()  # method를 호출
        abc()  # 함수를 호출 (class 안에서 function 호출 가능)

my = MyClass()
my.show()

from pack2.test20other import Our
print(Our.a)
print('our1 -------')
our1 = Our()  # 생성자 호출
print(our1.a)
our1.a = 2  # 고유 인스턴스의 a 선언
print(our1.a)
print('our2 -------')
our2 = Our()
print(our2.a)
# our1의 값을 업데이트 하더라도 our2에는 영향을 끼치지 않음(our2는 공유멤버의 a를 참조하기 때문)
