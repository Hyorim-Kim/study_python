# 자료형
# int, float, boolean, complex : 객체 값 하나를 참조, Immutable 객체(수정 불가)
# str, list, tuple, set, dict : 묶음형 객체 값 참조

# str : 문자열 자료형 : 순서O - 인덱싱과 슬라이싱 가능, 변경X
# 하나만 뽑아내면 인덱싱, 여러개면 슬라이싱
s = 'sequence'
# 문자열 관련 함수
print(len(s))
print('포함 횟수 : ', s.count('e'))
print('검색 위치 : ', s.find('e'), s.find('e', 3), s.rfind('e'))
# ...

ss = 'mbc'
print('mbc', ss, id(ss))  # id는 해시코드
ss = 'abc'
print('mbc', ss, id(ss))  # 주소 객체를 바꾼 것 (변경X, immutable 객체)

print(s, s[0], s[-7])  # indexing
print(s, s[0:5], s[-7:-5], s[5:], s[:5], s[::2], s[0:7:3])  # slicing, ::2 두칸걸러 출력
#     sequence seque eq nce seque sqec suc
print(s[0:5] + 'good')
print()
sss = '  mbc kbs sbs   '
print(sss)
print(ss.strip())  # 좌우공백제거
print(ss.lstrip())  # 좌 공백제거
print(ss.rstrip())  # 우 공백제거
ssss = sss.split(sep=' ')
print(ssss)
s5 = sss.replace('kbs', '공영방송')
print(s5)

print("\n\nList -------------------------------------")
# list : 배열과 유사, 중복 자료 허용, 여러 종류의 값 기억, 순서O, 변경O
a = [1, 2, 3]
print(a, type(a))  # [1, 2, 3] <class 'list'>
b = [10, a, 12.3, 'good', False]
print(b)
c = list();
print(c, type(c))
print()
family = ['준수', '예진', '정혜']
family.append('준호')  # 추가
family.insert(0, '민규') # 삽입
family.extend(['tom', 'oscar'])
family += ['지원', '국인']
family.remove('tom')
# family.clear()  # 전체 삭제
print(family, len(family), family[0])

print()
aa = [1, 2, 3, ['a', 'b', 'kbs'], 4, 5]  # 중첩리스트
print(aa, aa[0], aa[0:3])
print(aa[3], ' ', aa[3][2])  # ['a', 'b', 'kbs']   kbs

aa.remove(2)  # 값에 의한 삭제
del aa[3]  # 순서에 의한 삭제
print(aa)

print()
bb = aa  # 주소 치환 : 같은 객체를 참조, 얕은 복사
print(aa, ' ', bb, ' ', id(aa), id(bb))  # 주소 같음
bb[0] = 'nice'
print(aa, '', bb)

import copy
cc = copy.deepcopy(aa)  # 주소 치환 : 새로운 공간이 확보, 깊은 복사
print(aa, ' ', cc, ' ', id(aa), id(cc))  # 내용은 같으나 주소 다름
print(aa == cc, aa is cc)  # True False
cc[0] = '쉬고할까'
print(aa, ' ', cc)

print('자료구조 : stack, queue')
sbs = [10, 20, 30]
sbs.append(40)
print(sbs)
sbs.pop()  # 마지막부터 제거
print(sbs)
sbs.pop()  # stack구조, LiFo 처리
print(sbs)

print('\n')
sbs = [10, 20, 30]
sbs.append(40)
print(sbs)
sbs.pop(0)  # 첫번째부터 제거
print(sbs)
sbs.pop(0)  # queue 구조로 FiFo 처리
print(sbs)
