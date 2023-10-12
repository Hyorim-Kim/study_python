# class : 멤버로 변수와 메소드를 포함한 집합체. 객체 중심의 독립적인 프로그래밍이 가능함
# 그림 그리고 말하면서 설명할 줄 알아야함

class Car:
    handle = 0  # 멤버변수
    speed = 0  # 멤버변수

    def __init__(self, name, speed):
        self.name = name  # 원형 클래스에는 없음, car1객체
        self.speed = speed

    def showData(self):  # 메소드 자체는 공유하지만 메소드가 실행될 때 멤버들은 각 객체의 멤버를 사용한다.
        km = '킬로미터'
        msg = '속도 : ' + str(self.speed) + km  # speed 8 라인 찾아감, km은 11라인
        return msg

print(Car.handle)
# Car.showData()  # TypeError: Car.showData() missing 1 required positional argument: 'self'

car1 = Car('tom', 80)  # car1이라는 객체변수가 괄호 안 톰 앞(self)으로 들어감
print('car1 : ', car1.handle, car1.name, car1.speed)  # car1 :  0 tom 80  #  handle은 원형클래스에서 찾음
car1.color = '보라'  # car1 객체에 color 변수 추가  #  color는 tom만의 멤버임
print('car1 : ', car1.color)  # car1 :  보라
print()
car2 = Car('james', 100)  # car2의 주소가 self로 들어감
print('car2 : ', car1.handle, car1.name, car1.speed)  # handle이 car2에 없기 때문에 원형 클래스 공유멤버인 handle을 만남
print()
print(Car.handle, car1.handle, car2.handle)  # 0 0 0  # 같은 값이지만 과정은 다름  # car1, car2는 handle이 없어 Car에서 찾음
print(Car.speed, car1.speed, car2.speed)  # 0 80 100
print(car1.color)  # color는 car1만의 멤버
# print(car2.color)  # 'Car' object has no attribute 'color'
# print(Car.color)  # 'Car' has no attribute 'color'
print(Car, car1, car2)
print(id(Car), id(car1), id(car2))  # 객체가 3개이기 때문에 주소가 다 다름
print(car1.__dict__)  # 각 객체의 멤버를 확인
print(car2.__dict__)

print('메소드 ---------------')
print('car1 : ', car1.showData())  # bound method call, car1객체의 주소가 괄호 안에 담김 -> def showData(self) self로 들어감
print('car2 : ', car2.showData())  # car2에서 100을 가져옴

car1.speed = 55
car2.speed = 88
print('car1 : ', car1.showData())
print('car2 : ', car2.showData())

print()
Car.handle = 1  # 원형 클래스(프로토타입)의 멤버값을 업데이트
# 공유 메소드는 원형 클래스 메소드의 이름으로 업데이트 하면 된다.
print('car1 : ', car1.handle, car1.name, car1.speed)
print('car2 : ', car2.handle, car2.name, car2.speed)
