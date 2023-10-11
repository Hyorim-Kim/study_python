# python scope rule
# 변수의 생존 범위 : global, local
# Local > Enclosing funcftion > Global > Builtin

player = '국가대표'  # 전역변수 (모듈의 어디서든 공유 가능)

def funcSports():
    name = '신기루'  # 지역변수(함수 내에서만 유효)
    player = '지역대표'  # local 우선순위 먼저
    print(name, player)

funcSports()

print()
a = 1; b = 2; c = 3  # global
print('출력1 -- a:{}, b:{}, c:{}'.format(a,b,c))  # global과 같은레벨
def outerfunc():
    a = 4  # outer 영역
    b = 5
    def innerfunc():
        global c
        nonlocal b  # 사용빈도 낮음
        # c = 6
        print('출력2 -- a:{}, b:{}, c:{}'.format(a,b,c))  # inner > outer(Enclosing funcftion) > global 순서로 a,b,c 찾음 (outer의 b:5참조 - nonlocal)
        c = 6  # cannot access local variable 'c' where it is not associated with a value
        #  출력2에서 c를 찍을 때에는 참조하고 있는 로컬 c 값이 없음 (null point와 비슷한 개념)
        # -> 추가로 21 라인에 글로벌 c 를 선언, 25라인 c 가 전역변수로 바뀜
        #  출력2는 15라인의 c를 참조함, 그 후 c가 25라인으로 인해 6으로 업데이트 됨
        #  따라서 출력3, 4번의 c 값들은 모두 6임(전역변수 값이 6이기 때문에)
        b = 7
    innerfunc()
    print('출력3 -- a:{}, b:{}, c:{}'.format(a,b,c))  # inner 영역 아님 (outer의 b:7참조 - nonlocal)
    
outerfunc()
print('출력4 -- a:{}, b:{}, c:{}'.format(a,b,c))  # 모두 global 참조 (c 값은 후에 업데이트 됨)

print('\n인수와 매개변수 키워드 매칭 --------------------')
def ShowGugu(start, end=5):  # 초기치 부여할 수 있음
    for dan in range(start, end + 1):
        print(str(dan) + '단 출력', end=" ")
    print()  # 가로로 출력

# 매개변수의 유형 3가지 (총 4 종류)
ShowGugu(2, 3)  # 2단, 3단 출력  # 1위치 매개변수(인수와 매개변수가 순서대로 대응함)
# ShowGugu(2)  # error
# ShowGugu(2, 3, 3)  # error
ShowGugu(2)  # 에러없음 (파라미터에 초기치를 부여했기 때문에)  # 2기본값 매개변수(매개변수의 기본값 처리됨)
ShowGugu(start=2, end=3)  # 기본값은 사라지고 2,3단 출력
ShowGugu(end=3, start=2)  # 3키워드 매개변수, 인수와 파라미터의 이름이 같으면 순서가 달라도 매칭됨
ShowGugu(2, end=4)  # 2,3,4단 출력
#ShowGugu(start=2, 4)  # SyntaxError: positional argument follows keyword argument
#0ShowGugu(end=3, 2)  # SyntaxError: positional argument follows keyword argument

print()
# 4 가변 매개변수 : 인수의 개수가 동적
*a, b = [1,2,3,4,5]
def fu1(*ar):  # 별을 주면 64라인 실행 가능
    print(ar)
    for a in ar:
        print('밥 : ' + a)

# fu1('공기밥')
# fu1('공기밥', '주먹밥')  # fu1() takes 1 positional argument but 2 were given
fu1('공기밥', '주먹밥')
fu1('공기밥', '주먹밥', '김밥')

print()
def fu2(bap, *ar):
# def fu2(*ar, bap):  # error
    print(bap)
    print(ar)
    for a in ar:
        print('밥 : ' + a)

fu2('공기밥', '주먹밥')
fu2('공기밥', '주먹밥', '김밥')

print()
def selectCalc(choice, *ar):
    if choice == '+':
        imsi = 0
        for i in ar:
            imsi += i
    elif choice == '*':
        imsi = 1  # 곱셈이니 1줌
        for i in ar:
            imsi *= i
    return imsi

print(selectCalc('+', 1,2,3,4,5))  # tuple 자료  # choice는 연산자, *ar은 숫자(나머지 전부)
print(selectCalc('*', 1,2,3,4,5))

print()
# dict를 인수로 전달
def fu3(w, h, **etc):  # ** : dict로 받음
    print('몸무게:{}, 키:{}'.format(w, h))
    print(etc)
    
fu3(66, 177, irum='홍길동')  #  {'irum': '홍길동'}  dict로 처리됨
fu3(77, 178, irum='고길동', nai=22)  # {'irum': '고길동', 'nai': 22}

print()
def fuFinal(a,b,*c,**d):
    print(a, ' ', b)
    print(c)
    print(d)
    
fuFinal(1, 2)
fuFinal(1, 2, 3, 4, 5)
fuFinal(1, 2, 3, 4, 5, m=6, n=7)
