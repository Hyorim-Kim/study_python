# 함수 : 반복소스의 단순화를 목표로, 여러 개의 수행문을 하나의 이름으로 묶은 실행단위
# 내장함수
print(sum([3,4,5]))
print(bin(8))  # binary로 출력
print(int(1.5), float(3), str(5) + '오')
print(round(1.3), round(1.6))

import math
print(math.ceil(1.3), math.ceil(1.6))  # 올림
print(math.floor(1.3), math.floor(1.6))  # 버림

x = [10,20,30]
y = ['a', 'b']
for i in zip(x, y):  # 두개의 집합형 자료들을 묶어주는 함수 zip
    print(i)
# ...

print('---' * 10)
# 사용자 정의 함수
# def 함수명(parameter, ...):
#     ...
#     [return <반환값>]

def func1():
    print('func1 수행')  
    # return 생략 가능

func1()
print(func1)  # 주소
print('딴 짓 하다가')
imsi = func1()
print(imsi)  # None

print()
def func2(para1, para2):  # 매개변수 parameter
    result = para1 + para2
    aa = func3(result)
    return aa

def func3(result):
    if result % 2 == 1:
        return 
    else:
        return result  

print(func2(3, 4))  # 인수 argument
print(func2(3, 5))
print(func2, id(func2))  # <function func2 at 0x000001B34DAA8AE0> : 절대주소 1869613796064 : 해시코드 주소

print()
def swap(a, b):
    #return (b, a)  # 튜플형태 : 리턴값 하나
    return b, a  # 위와 같은 뜻

a = 10; b = 20
print(swap(a, b))

def func4():
    print('func4 처리')
    def func5():
        print('내부 함수 처리')
    func5()
    
func4()

# if 조건식 안에 함수 사용
def isodd(para):
    return para % 2 == 1

mydict = {x:x*x for x in range(11) if isodd(x)}
# if 만족할때 key : x, value : x*x
print(mydict)
