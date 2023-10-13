# 클래스의 포함관계 연습문제 : 커피 자판기 프로그램

class CoinIn:
    def calc(self, cupCount):
        #coin
        if self.coin < 200:
            print("금액이 부족합니다")
        elif cupCount * 200  > self.coin:
            print("금액이 부족합니다")
        else:
            #change
            self.change = self.coin - (cupCount * 200)
            print("커피 {}잔과 잔돈 {}원".format(cupCount, self.change))
    
class Machine:
    #cupCount = 1  # 선언할 필요 없음
    def __init__(self):
        self.coinIn = CoinIn()  # 클래스의 포함관계

    def showData(self):
        self.coinIn.coin = int(input('동전을 입력하세요 : '))  # TypeError: '<' not supported between instances of 'str' and 'int' -> int로 감싸기
        self.coinIn.cupCount = int(input('몇 잔을 원하세요? : '))
        print(self.coinIn.calc(self.coinIn.cupCount))

if __name__ == '__main__':
    Machine().showData()
