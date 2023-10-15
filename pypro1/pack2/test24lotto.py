import random

class LottoBall:
    def __init__(self, num):
        self.num = num  # num 속성을 초기화
        
class LottoMachine:
    def __init__(self):
        self.ballList = []  # set은 순서가 없기 때문에 리스트로 생성
        for i in range(1, 46):
            self.ballList.append(LottoBall(i))  # 포함관계
            # 각 숫자 i에 대해 LottoBall 클래스의 인스턴스를 생성하고, 이를 self.ballList에 추가
    def selectBall(self):
        # 번호 섞기 전
        for a in range(45):
            print(self.ballList[a].num, end=' ')
        print()
        # 번호 섞은 후
        random.shuffle(self.ballList)
        for a in range(45):
            print(self.ballList[a].num, end=' ')
            
        return self.ballList[0:6]  # 앞에서부터 6개를 선택하여 반환

class LottoUI:
    def __init__(self):
        self.machine = LottoMachine()  # 포함관계(로또UI에 로또 머신 들어감)
        # LottoMachine 클래스의 인스턴스를 생성하여 machine 속성에 저장
    def playLotto(self):
        input("로또 볼을 뽑으려면 Enter 키를 누르세요")
        selectedBalls = self.machine.selectBall()  # LottoMachine의 selectBall 메소드를 호출
        for ball in selectedBalls:
            print('%d'%ball.num)

if __name__ == '__main__':  # 프로그램 실행
    LottoUI().playLotto()  # LottoUI 클래스의 인스턴스를 생성하고, playLotto 메소드를 호출
