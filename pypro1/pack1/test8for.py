# 반복문 for
# for target in object: ...

for i in [1,2,3,4,5]:  # list
    print(i, end = ' ')

print()
for i in {1,2,3,4,5}:  # set, 순서 없음
    print(i, end = ' ')
    
print()
for i in (1,2,3,4,5):  # tuple
    print(i, end = ' ')
    
print()
soft = {'java':'웹용언어','python':'만능언어','js':'웹용스크립트'}
for i in soft.items():
    # print(i)  # ('java', '웹용언어')
    print(i[0] + '^^;' + i[1])

for k, v in soft.items():
    print(k)
    print(v)

print()
for aa in soft.keys():
    print(aa, end = ' ')

print()
for bb in soft.values():
    print(bb, end = ' ')

print()
# numbers = {1,3,5,7,9}
numbers = {-3,4,5,7,12}
tot = 0
for a in numbers:
    tot += a
    
print('합은 ' + str(tot) + ', 평균은 ' + str(tot / len(numbers)))

print()
li = ['a', 'b', 'c']
for k, d in enumerate(li):  # 나열형, 묶음형 자료를 넣으면 됨
    print(k, d)

print()
for n in [2, 3]:
    print('---{}단---'.format(n))
    for i in [1,2,3,4,5,6,7,8,9]:
        print('{} * {} = {}'.format(n, i, n * i), end = ' ')
    print()

print()
datas = {1,2,3,4,5}
for i in datas:
    if i == 2: continue
    if i == 4: break
    print(i, end=' ')
else:
    print('for 정상 종료')  # break 지우면 찍힘

print()
jumsu = [95, 70, 60, 55, 100]  # 70점 이상만 합격 처리
num = 0
for jum in jumsu:
    num += 1;
    if jum < 70:continue
    print('%d번째 합격!' %num)

print('for + 정규 표현식 연습 -----------')
import re
ss = """정부는 10일 국무회의에서 고용노동부 소관 법령인 ‘국민 평생 직업능력 개발법’ 개정안을 심의·의결하고, 정기 국회에 제출할 예정이라고 밝혔습니다.
이번 개정은 기업훈련 규제를 완화하는 특례제도를 도입하고, #%%&!@#*고용노동부 장관의 권한 중 기능대학의 설립 추천권을 시·도지사에게 이양하여 기타 제도 운용상 나타난 일부 미비점을 개선·보완하게 됩니다.
이번 개정안의 주요 내용은 다음과 같습니다.
먼저 직업능력개발훈련계획서의 승인으로 기업 훈련과정에 대한 자율성을 부여합니다.
그간 기업이 정부가 지원하는 훈련 사업에 참여하려면 개별 훈련과정 하나하나에 대해 복잡한 심사절차를 거쳐야 했습니다.
이에 따라 기업은 적시성 있는 훈련이 어려워 참여를 포기하거나 훈련을 경직적으로 실시하는 문제점이 있었습니다.
이에 따라 기업은 적시성 있는 훈련이 어려워 참여를 포기하거나 훈련을 경직적으로 실시하는 문제점이 있었습니다. 
참여를 포기하거나 훈련을 경직적으로 참여를 포기하거나 훈련을 경직적으로 참여를 포기하거나 훈련을 경직적으로 
참여를 포기하거나 훈련을 경직적으로 실시하는 문제점이 있었습니다."""
print(type(ss))
ss2 = re.sub(r'[^가-힣\s]', '', ss)
print(ss2)
ss3 = ss2.split(' ')
print(ss3)  # ['정부는', '일', '국무회의에서',  ...

cou = {}  # 단어의 발생 횟수를 dict로 저장
for i in ss3:
    if i in cou:
        cou[i] += 1
    else:
        cou[i] = 1
print(cou)

print()
for ss in ['111-1234', '일이삼-이이이이', '234-6789']:
    if re.match(r'^\d{3,4}-\d{4}$', ss):
        print(ss, '전화번호 맞아요')
    else:
        print(ss, '전화번호 아닌 듯')

print()
# 리스트 컴프리헨션은 직관적으로 리스트를 생성하는 방법입니다.
# 대괄호 "[", "]"로 감싸고 내부에 for문과 if 문을 사용하여 반복하며 조건에 만족하는 것만 리스트로 생성할 수 있습니다.
a = 1,2,3,4,5,6,7,8,9,10
li = []
for i in a:
    if i % 2 == 0:
        li.append(i)
print(li)

print(list(i for i in a if i % 2 == 0))  # comprehension

print()
i1 = [3,4,5]
i2 = [0.5, 1, 2]
result = []
for a in i1:
    for b in i2:
        result.append(a + b)
print(result)

datas = [a + b for a in i1 for b in i2]  # comprehension
print(datas)

print("리스트 컴프리헨션 살펴보기----------------")
temp = [1,2,3]
for i in temp:
    print(i, end=' ')

print()
print([i for i in temp])
print({i for i in temp})

print()
datas = [1,2,'a',True,3]
li = [i * i for i in datas if type(i) == int]
print(li)

datas = {1,1,2,2,3,2,1}
imsi = {i * i for i in datas}
print(imsi)  # set이기 때문에 중복X

print()
id_name = {1:'tom', 2:'oscar'}
print(id_name)
name_id = {val:key for key, val in id_name.items()}
print(name_id)

print()
aa = [(1,2),(3,4),(5,6)]
for a, b in aa:
    print(a + b)
    
# sum([1,2,3])
print('과일 값 계산 ---')
price = {'사과':5000, '감':500, '배':1000}  # 오늘 과일 가격
guest = {'사과':3, '감':2}
bill = sum(price[f] * guest[f] for f in guest)  # guest로부터 하나씩 빼냄
print('고객이 구매한 과일 총액은 {}원'.format(bill))

print('----------range 함수 : 수열 생성------------')
print(list(range(1, 11, 2)))
print(list(range(-10, -100, -20)))
print(set(range(1, 11, 2)))
print(tuple(range(1, 11, 2)))

print()
for i in range(6):  # 0 이상 6 미만 증가치 1
    print(i, end=' ')

print()
tot = 0
for su in range(1, 11):
    tot += su
print('결과 : ' + str(tot))
print('내장함수 : ' + str(sum(range(1, 11))))

for _ in range(6):  # 변수 사용 싫으면 _이용
    print('돌자')

for i in range(1, 10):
    print('{0} X {1} = {2}'.format(2, i, 2*i))

print()
# for와 range를 사용하여 문제 풀기
# 문1 : 2 ~ 5 단 출력
for i in range(2, 6):
    for j in range(1, 10):
        print('{0} X {1} = {2}'.format(i, j, i*j))

# 문2 : 1 ~ 100 사이의 정수 중 3의 배수이면서 5의 배수의 합 출력
print()
tot = 0
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        tot += i
        print(i)
print(tot)

# 문3 : 주사위를 두 번 던져 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
# 1 3
# 2 4
# ...
print()
for i in range(1, 7):
    for j in range(1, 7):
        if (i + j) % 4 == 0:
            print(i, j, i+j)

