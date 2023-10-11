# 클로저 : scope에 제약을 받지 않는 변수들을 포함하고 있는 코드 블럭이다.
# 함수 내에서 선언한 지역변수를 함수 밖에서 사용하기 위한 방법

def funcTimes(a, b):
    c = a * b
    print(c)
    return c  # 주소 리턴
    
funcTimes(2, 3)
# print(c)  # NameError: name 'c' is not defined

imsi = funcTimes(2, 3)
print(imsi)  # c가 참조하는 값을 imsi도 같이 참조, 7번 라인

print('closure test : 클로저를 사용하지 않은 경우-----------------')
def out():
    count = 0
    def inn():
        nonlocal count
        count += 1  # 값이 없는 상태에서 +1 할 수 없음 --> 18 line에 nonlocal count 선언
        return count
    print(inn())  # count값 호출

out()
# print(out + 1)  # error
print()
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner  # <== 요게 클로저 : 내부함수의 주소를 반환, 괄호없음(inner function의 주소)

var1 = outer()
print(var1)  # 주소 출력됨
print(var1())  # 1
print(var1())  # 2
print(var1())  # 3
var2 = outer()
print(var2())  # var1과 같은 outer type이지만 다른 객체이다.
print(var2())
print(id(var1), ' ', id(var2))  # 주소 다름

print('--- 수량 * 단가 * 세금(분기별로 동적)을 출력하는 함수 작성')
def outer2(tax):  # tax : 지역변수(outer2 내에서만 유효)
    def inner2(su, dan):
        amount = su * dan * tax
        return amount
    return inner2  # ==> closure, 내부함수의 주소를 리턴함

# 1분기에는 tax : 0.1
q1 = outer2(0.1)  # q1는 inner2를 리턴하는 outer2의 주소를 갖는다
print(q1)  # <function outer2.<locals>.inner2 at 0x000001F30D32E160>
result1 = q1(5, 50000)  # 함수 내의 함수 주소를 넘겨 받았기 때문에 지역변수인 tax를 사용할 수 있음
print('result1 : ', result1)
result2 = q1(2, 10000)
print('result2 : ', result2)

print()
q2 = outer2(0.05)  # 2분기
result3 = q2(5, 50000)
print('result3 : ', result3)
result4 = q2(2, 10000)
print('result4 : ', result4)
# closure를 이용해서 받아옴
