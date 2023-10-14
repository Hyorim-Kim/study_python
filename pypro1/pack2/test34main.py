# 추상 클래스를 이용한 상속 연습 문제 (4번)
# 소스코드 한줄한줄 의미 알아야함

from pack2.test34etc import Employee

class Temporary(Employee):  # Employee 클래스를 상속받음
    def __init__(self, irum, nai, ilsu, ildang):
        super().__init__(irum, nai)  # 상위 클래스의 __init__ 메소드를 호출
        self.ilsu = ilsu  # 추가로 ilsu와 ildang 속성을 초기화
        self.ildang = ildang
        
    def pay(self):  # 임금 계산
        return self.ilsu * self.ildang  # 반환
    
    def data_print(self):
        self.irumnai_print()
        print(', 월급 : ' + str(self.pay()))  # TypeError: can only concatenate str (not "int") to str
        # self.pay()는 해당 객체의 pay 메소드를 호출


class Regular(Employee):  # Employee 클래스를 상속받음
    def __init__(self, irum, nai, salary):
        super().__init__(irum, nai)  # 상위 클래스의 __init__ 메소드를 호출
        self.salary = salary
        
    def pay(self):
        return self.salary

    def data_print(self):
        self.irumnai_print()
        print(', 급여 : ' + str(self.pay()))


class Salesman(Regular):  # Regular 클래스를 상속받음
    def __init__(self, irum, nai, salary, sales, commission):
        super().__init__(irum, nai, salary)
        self.sales = sales
        self.commission = commission
        
    def pay(self):
        return self.salary + (self.sales * self.commission)
        
    def data_print(self):
        self.irumnai_print()
        print(', 수령액 : ' + str(self.pay()))

# 객체를 생성
t = Temporary('홍길동', 25, 20, 15000)  # Temporary 클래스 타입의 객체에 넣음 / Temporary 넣는거 XXX
r = Regular('한국인', 27, 3500000)  # Regular 클래스 타입의 객체로 들어감
s = Salesman('손오공',29,1200000,5000000,0.25)

# 각각의 정보를 출력
t.data_print()
r.data_print()
s.data_print()
