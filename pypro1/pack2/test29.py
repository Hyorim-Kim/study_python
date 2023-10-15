# 다중 상속
class Tiger:
    data = "호랑이 세상"
    
    def cry(self):
        print('호랑이가 소리를 ...')
        
    def eat(self):
        print('맹수는 고기를 무척 좋아함')

class Lion:
    def cry(self):
        print('사자의 울부짖음')
    
    def hobby(self):
        print('백수의 왕은 채팅을 즐김')

class Liger1(Tiger, Lion):  # 다중 상속
    pass

obj1 = Liger1()  # 인스턴스 생성
obj1.cry()  # 먼저 적어준 Tiger의 멤버가 수행됨
obj1.eat()
obj1.hobby()
print(obj1.data)

print('------------------------')
def hobby():
    print('모듈의 멤버인 함수')
    
class Liger2(Lion, Tiger):  # 다중 상속
    data = '라이거 만세'
    
    def play(self):
        print('라이거 고유 메소드')

    def hobby(self):
        print('라이거는 운동을 좋아함')

    def showHobby(self):
        self.hobby()  # 라이거는 운동을 좋아함
        super().hobby()  # 백수의 왕은 채팅을 즐김, Lion의 메소드
        hobby()  # 모듈의 멤버인 함수
        print(self.data + ", " + super().data)  # 라이거 만세, 호랑이 세상

obj2 = Liger2()  # 인스턴스 생성
obj2.cry()  # 먼저 적어준 Lion의 멤버가 수행됨
obj2.showHobby()
