# 클래스의 포함관계 연습문제 : 커피 자판기 프로그램

class CoinIn:
    def calc(self, cupCount):
        #coin
        if self.coin < 200:
            return("금액이 부족합니다")  # print가 아니라 return으로 해야 None 출력안됨
        elif cupCount * 200  > self.coin:
            return("금액이 부족합니다")
        else:
            #change
            self.change = self.coin - (cupCount * 200)
            return("커피 {}잔과 잔돈 {}원".format(cupCount, self.change))
    
class Machine:
    #cupCount = 1  # 선언할 필요 없음
    def __init__(self):
        self.coinIn = CoinIn()  # 클래스의 포함관계, Machine 클래스가 CoinIn 클래스의 기능을 내부적으로 사용
        # Machine 클래스의 인스턴스가 생성될 때마다 CoinIn 클래스의 인스턴스를 생성하여 self.coinIn 속성에 할당

    def showData(self):  # 동전과 잔 수를 입력받은 후 CoinIn 클래스의 calc 메소드를 호출하여 결과를 출력
        self.coinIn.coin = int(input('동전을 입력하세요 : '))  # 사용자로부터 동전을 입력받아 CoinIn 클래스의 인스턴스인 self.coinIn의 coin 속성에 값을 할당
        self.coinIn.cupCount = int(input('몇 잔을 원하세요? : '))
        print(self.coinIn.calc(self.coinIn.cupCount))  # 인자로 self.coinIn.cupCount가 전달

if __name__ == '__main__':  # 프로그램 실행
    Machine().showData()  # Machine 클래스의 인스턴스를 생성하고, showData 메소드를 호출
