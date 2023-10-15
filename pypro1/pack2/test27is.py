# 상속 연습
print('클래스는 모듈의 멤버')

class Person:
    say = '난 사람이야~'  # public
    nai = '20'
    __my = 'private 멤버'  # private(__변수명), 현재 클래스 내에서만 사용 가능
    
    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai
    
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai, self.say))

    def hello(self):
        print('안녕')
        print(self.__my)
    
    # 참고
    @staticmethod  # 장식자, static : 독립적으로 수행
    def kbs(tel):
        print('kbs_static method(클래스 소속) : ', tel)
        
print(Person.say, Person.nai)
# Person.printInfo()
p = Person('25')  # 생성자 호출
print(p.say, p.nai)
p.printInfo()  # bound method call, 객체변수 p가 인수로 괄호에 담겨서 parameter로 전달됨

p.hello()
p.kbs('111-1234')
Person.kbs('111-1234')  # 권장, 객체변수의 이름보다 클래스명으로 부르는게 좋음

print('***' * 20)
class Employee(Person):
    subject = '근로자'
    
    def __init__(self):
        print('Employee 생성자')
    
    def printInfo(self):  # method overriding(다형성 구사)
        print('Employee의 오버라이딩 된 printInfo')
        
    def eprintInfo(self):
        print(self.say, super().say)  # self는 자식에서 찾고 없으면 부모로 올라가는 반면, super는 처음부터 부모 클래스에서 찾음
        self.hello()
        self.printInfo()  # Employee에 없으면 부모 클래스에서 찾음
        super().printInfo()  # 무조건 부모 클래스

e = Employee()
print(e.say, e.subject)
e.eprintInfo()

print('***' * 20)
class Worker(Person):
    say = 'worker의 say'
    
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai)  # Bound method call,    def __init__(self, nai)의 self도 Person 생성자로 넘어감
    
    def printInfo(self):  # method overriding
        print('Worker에 선언된 printInfo')
    
    def wprintInfo(self):
        self.printInfo()  # 바로 위의 printInfo 호출
        super().printInfo()  # Person의 메소드 호출

w = Worker('30')
print(w.say, w.nai)  # say, nai를 worker에서 찾지만 없기 때문에 person에서 찾음  -> worker에 say 추가, worker에서 찾음(부모 숨어버림, 은닉화)
w.wprintInfo()

print("^^^" * 20)
class Programmer(Worker):  # Worker의 자식
    def __init__(self, nai):  # worker -> person 생성자에 끌고가기 위해 nai(age) 인수 필요
        print('Programmer 생성자')
        # super().__init__(nai)  # Bound call, self가 자동으로 들어감
        Worker.__init__(self, nai)  # UnBound call

    def pprintInfo(self):
        self.wprintInfo()  # wprintInfo를 통해 person까지 연결됨
        
    def hello2(self):
        print('안녕')
        # print(self.__my)  # error : private member이므로
        
pr = Programmer(33)
print(pr.say, pr.nai)  # worker의 say, programmer 인스턴스의 nai 출력
pr.pprintInfo()
pr.hello2()
pr.kbs('111-1234')  # static멤버 : 자유롭게 어디서든 부를 수 있다.
Programmer.kbs('111-1234')  # 권장
# 여기까지 8개의 객체임(원형클래스 4, 각각의 클래스의 인스턴스 4), 그림 그리면서 이해하기

print('클래스 타입 확인 ---')
print(type(1.2))
print(type(pr))
print(Programmer.__bases__)  # 부모확인 : Worker, 다중상속이 가능하기 때문에 집합형으로 표현됨
print(Worker.__bases__)  # Person
print(Person.__bases__)  # object, 모든 클래스의 최상위 부모 클래스
