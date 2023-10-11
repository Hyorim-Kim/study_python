# Module : 소스 코드의 재사용을 가능하게 하며, 소스 코드를 하나의 이름 공간으로 관리하며 저장하면 .py로 저장된다.
# module은 package 내에 있어야 한다.
# 표준 모듈, 사용자 정의 모듈, 제3자(third party) 모듈로 구분할 수 있다. (분석과 관련된 외부 모듈이 잘 되어있음)
# 모듈은 또 다른 모듈을 포함할 수 있다. 여러 개의 모듈 중 응용 프로그램의 메인 모듈을 명시하는 것이 좋다.

# 표준 모듈
# 내장된 모듈은 별도의 작업 없이 사용
print('모듈의 멤버 : 명령문, 함수, 클래스, 모듈')
# 설치는 되었으나 loading 되지 않은 모듈(외부 모듈)은 import 키워드로 loading 후 사용한다.
import sys
print(sys.path)
#sys.exit()  # 프로그램의 강제 종료
#print('프로그램 종료')

print(sum([1,2,3]))

import math
print(math.e, ' ', math.pi)
print(math.sin(math.radians(30)))

import calendar
calendar.setfirstweekday(6)  # 일요일을 첫 요일로 지정
calendar.prmonth(2023, 10)

import numpy  # 데이터분석과 관련된 중요한 모듈
print(numpy.abs(-3))

import random  # import를 하면
print(random.random())  # 모듈명.함수명()
print(random.randrange(1, 10))

# 위와 같은 의미
from random import random
# from random import * # 권장되지 않음, 패키지 내의 모든 것을 가져오기 때문에 메모리 낭비
print(random())  # 모듈명 내의 멤버만 적어줌
