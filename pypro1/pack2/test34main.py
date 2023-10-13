# 소스코드 한줄한줄 의미 알아야함

from pack2.test34etc import Employee

class Temporary(Employee):  # temporary type의 객체에 넣음 / temporary에 넣는거 XXX
    def __init__(self, irum, nai, ilsu, ildang):
        super().__init__(irum, nai)
        self.ilsu = ilsu
        self.ildang = ildang
        
    def pay(self):
        return self.ilsu * self.ildang
    
    def data_print(self):
        self.irumnai_print()
        print(', 월급 : ' + str(self.pay()))  # TypeError: can only concatenate str (not "int") to str


class Regular(Employee):  # regular class type의 객체로 들어감
    def __init__(self, irum, nai, salary):
        super().__init__(irum, nai)
        self.salary = salary
        
    def pay(self):
        return self.salary

    def data_print(self):
        self.irumnai_print()
        print(', 급여 : ' + str(self.pay()))


class Salesman(Regular):
    def __init__(self, irum, nai, salary, sales, commission):
        super().__init__(irum, nai, salary)
        self.sales = sales
        self.commission = commission
        
    def pay(self):
        return self.salary + (self.sales * self.commission)  # self.salary ? super().pay() ? 
        
    def data_print(self):
        self.irumnai_print()
        print(', 수령액 : ' + str(self.pay()))

t = Temporary('홍길동', 25, 20, 15000)
r = Regular('한국인', 27, 3500000)
s = Salesman('손오공',29,1200000,5000000,0.25)

# 새로운 객체 t, r, s / 각 객체에 정보 저장됨
t.data_print()
r.data_print()
s.data_print()
