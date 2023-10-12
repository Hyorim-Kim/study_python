import random

class LottoBall:
    def __init__(self, num):
        self.num = num
        
class LottoMachine:
    def __init__(self):
        self.ballList = []  # set으로 만들면 순서가 없기 때문에 리스트로
        for i in range(1, 46):
            self.ballList.append(LottoBall(i))  # 포함관계
        
    def selectBall(self):
        # 번호 섞기 전
        for a in range(45):
            print(self.ballList[a].num, end=' ')
        print()
        # 번호 섞은 후
        random.shuffle(self.ballList)
        for a in range(45):
            print(self.ballList[a].num, end=' ')
            
        return self.ballList[0:6]

class LottoUI:
    def __init__(self):
        self.machine = LottoMachine()  # 포함관계(로또UI에 로또 머신 들어감)
        
    def playLotto(self):
        input("로또 볼을 뽑으려면 Enter 키를 누르세요")
        selectedBalls = self.machine.selectBall()
        for ball in selectedBalls:
            print('%d'%ball.num)

if __name__ == '__main__':
    LottoUI().playLotto()
