# python은 일급객체를 지원하는 일급함수를 사용
# 일급함수 : 함수안에 함수 선언 가능, 인자로 함수 전달, 반환값이 함수인 경우 
# 일급객체를 지원하는 함수

def func1(a, b):
    return a + b

func2 = func1  # 주소치환
print(func1(3, 4))
print(func2(3, 4))

print()
def myFunc(func):  # 인자로 함수, func1 주소를 func로 줌
    def func4():  # 함수 안에 함수 선언
        print('난 내부 함수야~~~')
    func4()
    return func  # 반환값이 함수

mbc = myFunc(func1)  # 인자로 함수, func1의 주소를 들고감
print(mbc(3, 4))

print('\n축약 함수(Lambda : 이름이 없는 한 줄 짜리 함수)')
# lambda 인자,,, :표현식
# def를 사용해야 될 정도로 함수의 내용이 복잡하지 않거나, def를 사용할 수 없는 상황일 때 람다를 적용

def hap(x, y):
    return x + y
print(hap(1, 2))

print((lambda x, y:x + y)(1, 2))  # return 생략

jtbc = lambda x,y:x*y
print(jtbc)  # <function <lambda> at 0x000002E57AEADA80> : 람다함수의 주소
print(jtbc(3, 4))

mbc = lambda:print('단순한 람다')  # parameter X
mbc()

# 람다도 가변인수 가능
kbs = lambda a, su=10:a + su
print(kbs(5))
print(kbs(6))

sbs = lambda a, *tu, **di:print(a, tu, di)
sbs(1,2,3,x=4,y=5)

print()
# 리스트에 복수 람다를 저장
li = [lambda a,b:a+b, lambda a,b:a*b]
print(li[0](3, 4))
print(li[1](3, 4))

# 함수 내에 멤버로 람다 사용
# filter(조건 함수, 순회 가능한 데이터)
# filter() 함수는 두 번째 인자로 넘어온 데이터 중에서 첫 번째 인자로 넘어온 조건 함수를 만족하는 데이터만 찾아서 반환해줍니다.
print(list(filter(lambda a:a<5, range(10))))  # filter의 결과를 리스트에 담아서 출력, 필터 조건 : 0 ~ 9 중 5미만
print(list(filter(lambda a:a%2, range(10))))  # 홀수(나머지가 1이면 true, 0이면 false이고 false값은 출력하지 않음)

print()
# Q) 1 ~ 100 사의 정수 중 5의 배수이거나 7의 배수만 걸러 보기 (filter, lambda 이용)
print(list(filter(lambda a:a%5==0 or a%7==0, range(1, 101))))

print()
print('함수 장식자 : @함수명 -- meta 기능을 갖음')  # 뭔지만 알아두기
# 장식자는 다른 함수를 감싼 함수다. 주 함수가 호출되면 그 반환 값이 장식자에게 건네진다.
# 그러면 장식자는 포함된 함수로 교체하여 함수를 반환한다.

def make2(fn):
    return lambda : "안녕 " + fn()  #  fn() : make1 실행

def make1(fn):
    return lambda : "반가워 " + fn()  #  fn() : hello 실행

def hello():
    return "한국인"

hi = make2(make1(hello))
print(hi())  # 안녕 반가워 한국인

# decorator
@make2  # make2가 make1을 감싼다.
@make1  # make1이 hello2를 감싼다.
def hello2():
    return "신기해"

print(hello2())  # 안녕 반가워 신기해

print('재귀함수(recursive function) : 함수가 자기자신을 호출 --- 반복처리에 사용')
# 연산량이 많아지면 역효과가 날 수 있기 때문에 간단한 반복처리에만 사용한다.
def countDown(su):
    if su == 0:
        print('완료')  # 반복 종료
    else:
        print(su, end = ' ')
        countDown(su - 1)  # 재귀(반복)

countDown(5)

print('1 ~ 10 까지의 정수의 합')
def funcHap(n):
    if n == 1:
        print('탈출')
        return True  # or 1
    return n + funcHap(n - 1)

result = funcHap(10)
print('10 까지의 정수의 합', result)

print('계승(factorial : 1부터 어떤 양의 정수 n 까지의 수를 모두 곱한 것) 처리를 위한 재귀 함수')
def myFact(a):
    if a == 1: return True  # 빠짐
    print(a)
    return a * myFact(a - 1)  # recursive function

print('5!은 ', myFact(5))  # 5!은  120
