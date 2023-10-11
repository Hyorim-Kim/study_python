# 독립적인 실행보다는 다른 모듈에서 호출될 사용자 정의 모듈
# 자원의 재활용을 목적으로 함
score = 90

def listHap(*ar):
    print(ar)
    if __name__ == '__main__':
        print('메인 모듈이야')  # 메인 모듈 아님

def kbs():
    print('공영방송')

def mbc():
    print('만나면 좋은 친구 11')
