# 다중 상속 연습
class Animal:
    def move(self):  # move를 override 하기를 기대
        pass

class Dog(Animal):  # 단일 상속
    name = "구름"
    
    def move(self):
        print('구름이는 두 달에 한 번씩 미용실에 감')

class Cat(Animal):  # 단일 상속
    name = "냐옹이"
    
    def move(self):
        print('냐옹이는 한 달에 한 번씩 PC방에 감')
        print('밤에 눈빛이 빛남')
        
class Wolf(Dog, Cat):  # 다중 상속
    pass

class Fox(Cat, Dog):  # 다중 상속
    def move(self):
        print('난 여우라고 해')

    def foxMethod(self):
        print('여우 고유 메소드')

dog = Dog()  # 생성자 호출
print(dog.name)
dog.move()
print()
cat = Cat()
print(cat.name)
cat.move()
print('-----------')
wolf = Wolf()
print(wolf.name)
wolf.move()
print()
fox = Fox()
print(fox.name)
fox.move()
fox.foxMethod()
print(Wolf.__mro__)  # __mro__ : 클래스의 탐색 순서를 볼 수 있다.
# (<class '__main__.Wolf'>, <class '__main__.Dog'>, <class '__main__.Cat'>, <class '__main__.Animal'>, <class 'object'>)
print(Fox.__mro__)
# (<class '__main__.Fox'>, <class '__main__.Cat'>, <class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>)

print('-----------')
sbs = wolf
sbs.move()
print()
sbs = fox
sbs.move()

print('-----------')
animals = (dog, cat, wolf, fox)
for a in animals:
    a.move()
    print()
