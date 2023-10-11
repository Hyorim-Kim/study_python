# 사용자 정의 모듈 call
print('뭔가를 하다가... 다른 모듈 호출')

# 같은 패키지 내의 모듈 읽기
import pack2.test14other  # 패키지명.모듈명, 패키지명 생략 불가

print('score : ', pack2.test14other.score)
print(pack2.test14other.__file__)  # __ : 시스템에서 지원하는 키워드, import 한 경로를 출력
print(pack2.test14other.__name__)  # pack2.test14other : 모듈명 출력

list1 = [1,2]
list2 = [3,4]
pack2.test14other.listHap(list1, list2)  # ([1, 2], [3, 4])를 들고 test14other의 listHap으로 감

def abc():
    if __name__ == '__main__':
        print('메인 모듈이야 라고 외치다')  # 메인이기 때문에 출력됨 (내가 실행하는 곳이 메인 모듈)
abc()

print()
pack2.test14other.kbs()  # 방법1
from pack2.test14other import kbs, mbc, score  # 방법2
kbs()
mbc()
print(score)

# 다른 패키지 내의 모듈 읽기(접근 지정자가 없기 때문에 패키지가 같던 다르던 방법은 같음)
import moduletest.test14etc  # 패키지명.모듈명
moduletest.test14etc.Hap(5, 3)

from moduletest.test14etc import Cha
Cha(5, 3)

# C:\anaconda3\Lib에 test13etc2.py 복붙함
import test14etc2  # 패키지명 생략하고 모듈명만 써도 됨
test14etc2.Gop(5, 3)
from test14etc2 import Nanugi
Nanugi(5, 3)

# 다운받은 third party 모듈은 python interpreters / libraries에 들어감 (preferences에서 확인가능)
