'''
따옴표 세개는
여러 줄 주석
'''
# 한 줄 주석
print('환영합니다. 파이썬 세상 만세');

var1 = '안녕';  # var1 = "안녕";
print(var1)  # 참조형 변수 : 인스턴스의 주소를 기억
var1 = 5; print(var1)

a = 10
b = 20.5
c = b  # 주소를 치환
print(a, b, c)
print('주소 : ', id(a), id(b), id(c))
print(a is b, a == b)  # is : 주소 비교, == : 값 비교
print(b is c, b == c)

print()
a = [1, 2]
b = a
c = [1, 2]
print(a is b, a == b)
print(a is c, a == c)  # a와 c는 값이 같지만 주소가 다름

print()
A = 1; a = 2;  # 변수는 대소문자 구분
print(A, ' ', a)

print()
import keyword  # 설치는 되었으나 메모리에 로딩되지 않은 모듈 로딩하기
print('예약어 목록 : ' , keyword.kwlist)  # 예약어는 사용자 정의 이름이로 사용하면 안됨

print()
print(10, oct(10), hex(10), bin(10))  # 10 0o12 0xa 0b1010
print(10, 0o12, 0xa, 0b1010)

print('자료형 확인')
print(5, type(5))  # int
print(5.1, type(5.1))  # float
print(5+6j, type(5+6j))  # complex
print(True, type(True))  # bool
print('a', type('a'))  # str

print('묶음형 자료형 ---')
print((1,), type((1,)))  # tuple
print([1], type([1]))  # list
print({1}, type({1}))  # set
print({'key':1}, type({'key':1}))  # dict
# tuple과 list의 장단점 알아야함

print("\n연산자 둘러보기 -------------")
v1 = 3  # 치환
v1 = v2 = v3 = 3
print(v1, v2, v3)

print('a', end=',')  # system.out.print
print('b')  # system.out.println

v1 = 1,2,3;  # 묶음형 자료형
print(v1)  # (1, 2, 3)

v1, v2 = 10, 20
print(v1, v2)
v2, v1 = v1, v2
print(v1, v2)

print('값 할당 packing')
*v1, v2 = 1,2,3,4,5
v1, *v2 = 1,2,3,4,5
print(v1, v2)

v1, *v2, v3 = 1,2,3,4,5

# print에 대해 
print(format(1.5678, '10.3f'))
print('나는 나이가 %d 이다.'%23)
print('나는 나이가 %s 이다.'%'스물셋')
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100))
print('이름은 {0}, 나이는 {1}'.format('한국인', 33))
print('이름은 {}, 나이는 {}'.format('신선해', 33))
print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))
