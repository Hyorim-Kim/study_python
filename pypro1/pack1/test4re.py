# 정규 표현식 : 특정한 규칙을 가진 문자열의 집합을 표현하기 위해 쓰이는 형식언어
import re

ss = "1234 abc 가나다abcABC_123555_6python is fun"
print(ss)
print(re.findall(r'123', ss))  # 소문자 r 선행
print(re.findall(r'가나', ss))

print(re.findall(r'[1,2,5]', ss))
print(re.findall(r'[1,2,5]+', ss))  # 반복 관련 메타문자   +:1회 이상
# print(re.findall(r'[1,2,5]*', ss))  # 반복 관련 메타문자   +:0회 이상
print(re.findall(r'[0-9]+', ss))  # 문자 집합 [], 숫자만 1개 이상
print(re.findall(r'[^0-9]+', ss))  # 문자 집합 [^] 부정
print(re.findall(r'\d+', ss))  # 특수문자 \d,  숫자만 1개 이상
print(re.findall(r'\D+', ss))  # 특수문자 \D  문자만 1개 이상
print(re.findall(r'[0-9]{2}', ss))  # {n} n회
print(re.findall(r'[0-9]{2,3}', ss))
print(re.findall(r'[가-힣, a-z, A-Z]+', ss))
print(re.findall(r'^1234', ss))  # 패턴의 제일 앞에 오면 문자열 시작의 의미
print(re.findall(r'fun$', ss))  # 문자열 끝

print()
ss = '''
<a href="abc1.html">abc1</a>
<a href="abc2.html">abc2</a>
<a href="abc3.html">abc3</a>
'''
print(ss)
result = re.findall(r'href="(.*)"', ss)  # " ' " " ' "
print(result)

print()
# 정규표현식 패턴을 객체로 만들기
p = re.compile('the', re.IGNORECASE)  # flag 사용하기, 대소문자 상관없이 값 출력
print(p.findall('The dog the dog'))

s = """My name is tom
I am happy"""
print(s)
p = re.compile('^.+', re.MULTILINE)  # 처음이 한글자 이상, 여러개일 때/ 하나의 문자열을 나눠서 처리
print(p.findall(s))

