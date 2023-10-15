# 다중 상속 연습
class Animal:
    def move(self):  # 추상 메소드, move를 override 하기를 기대
        pass

class Dog(Animal):  # Animal 클래스를 상속, 단일 상속
    name = "구름"
    
    def move(self):  # move 메소드를 오버라이딩
        print('구름이는 두 달에 한 번씩 미용실에 감')

class Cat(Animal):  # 단일 상속
    name = "냐옹이"
    
    def move(self):  # move 메소드를 오버라이딩
        print('냐옹이는 한 달에 한 번씩 PC방에 감')
        print('밤에 눈빛이 빛남')
        
class Wolf(Dog, Cat):  # Dog와 Cat 클래스를 다중 상속받음
    pass  # 별도의 구현이 없어 첫 번째로 상속한 Dog 클래스의 메소드를 사용

class Fox(Cat, Dog):  # Cat과 Dog 클래스를 다중 상속받음
    def move(self):  # move 메소드를 오버라이딩
        print('난 여우라고 해')

    def foxMethod(self):
        print('여우 고유 메소드')

dog = Dog()  # 인스턴스를 생성
print(dog.name)
dog.move()
print()
cat = Cat()
print(cat.name)
cat.move()
print('-----------')
wolf = Wolf()
print(wolf.name)
wolf.move()  # 첫 번째로 상속한 Dog 클래스의 메소드를 사용
print()
fox = Fox()
print(fox.name)
fox.move()
fox.foxMethod()
print(Wolf.__mro__)  # __mro__ : 클래스의 탐색 순서를 볼 수 있다.
# (<class '__main__.Wolf'>, <class '__main__.Dog'>, <class '__main__.Cat'>, <class '__main__.Animal'>, <class 'object'>)
print(Fox.__mro__)
# (<class '__main__.Fox'>, <class '__main__.Cat'>, <class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>)

print('-----------')  # 다형성 활용
sbs = wolf
sbs.move()
print()
sbs = fox
sbs.move()

print('-----------')  # 반복문을 통한 다형성 활용
animals = (dog, cat, wolf, fox)
for a in animals:
    a.move()
    print()
