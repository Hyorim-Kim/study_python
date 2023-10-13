# 클래스의 상속
class Animal:  # 부모 클래스
    def __init__(self):
        print('Animal 생성자')
        
    def move(self):
        print('움직이는 생물')

class Dog(Animal):  # 자식 클래스, 괄호안에 부모클래스를 작성하여 상속받음
    def __init__(self):
        print('댕댕이 생성자')
        
    def my(self):
        print('난 댕댕이야~')

dog1 = Dog()  # Dog의 생성자를 호출, 자식의 생성자가 없으면 부모의 생성자를 부름
dog1.my()
dog1.move()

print()
class Horse(Animal):
    pass

horse1 = Horse()
horse1.move()
