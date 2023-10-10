# 반복문 관련 continue, break

a = 0
while a < 10:
    a += 1
    if a == 5: continue  # 5 skip
    if a == 6: break  # 강제종료되면 else를 수행하지 않는다.
    print(a)
else:
    print('while 정상 작동')

print('while 수행 후 a는 %d'%a)

while 1:  # : True  무한루프에 빠짐
    a = int(input('확인 할 숫자: '))
    if a == 0:
        print('반복수행 종료')
        break
    elif a % 2 == 0:
        print('%d는 짝수'%a)
    elif a % 2 == 1:
        print('%d는 홀수'%a)

# 난수 (pseudo random : 의사 난수) - 난수표를 사용
import random
# random.seed(1)  # 난수의 순서를 고정

friend = ['준수', '예진', '혜정']
print(random.choice(friend))  # 1개만 랜덤 추출
print(random.sample(friend, k=2))  # 2개 추출
random.shuffle(friend)  # 원본을 섞음
print(friend)

# 컴이 가진 임의의 정수 알아 맞히기
num = random.randint(1, 10)
while True:
    print('1 ~ 10 사이의 컴이 가진 숫자를 예상하시오')
    su = int(input())
    if num == su:
        print('성공' * 10)
        break
    elif su < num:
        print('더 큰 수를 입력')
    elif su > num:
        print('더 작은 수를 입력')
