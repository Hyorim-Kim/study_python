# 한글 형태소 분석
# 분석 도구로 KoNLpy 사용
# Kkma, Okt(Open Korean Text), Komoran 사용
from konlpy.tag import Kkma, Okt, Komoran

kkma = Kkma()
print(kkma.sentences('시속 200㎞에 달하는 강풍을 동반한 태풍 키아란이다. 서유럽을 강타하며 최소 7명이 사망했다.'))
print(kkma.pos('시속 200㎞에 달하는 강풍을 동반한 태풍 키아란이다. 서유럽을 강타하며 최소 7명이 사망했다.'))  # 품사 태깅
print(kkma.nouns('시속 200㎞에 달하는 강풍을 동반한 태풍 키아란이다. 서유럽을 강타하며 최소 7명이 사망했다.'))  # 명사
print(kkma.morphs('시속 200㎞에 달하는 강풍을 동반한 태풍 키아란이다. 서유럽을 강타하며 최소 7명이 사망했다.'))  # 모든 품사

print()
okt = Okt()  # 가장 많이 사용되는 parser
print(okt.phrases('시속 200㎞에 달하는 강풍을 동반한 태풍 키아란이다. 서유럽을 강타하며 최소 7명이 사망했다.'))  # 어절
print(okt.pos('시속 200㎞에 달하는 강풍을 동반한 태풍 키아란이다. 서유럽을 강타하며 최소 7명이 사망했다.'))  # 품사 태깅
print(okt.pos('시속 200㎞에 달하는 강풍을 동반한 태풍 키아란이다. 서유럽을 강타하며 최소 7명이 사망했다.', stem=True))  # 어근으로 출력(하는 -> 하다)
print(okt.nouns('시속 200㎞에 달하는 강풍을 동반한 태풍 키아란이다. 서유럽을 강타하며 최소 7명이 사망했다.'))  # 명사
print(okt.morphs('시속 200㎞에 달하는 강풍을 동반한 태풍 키아란이다. 서유럽을 강타하며 최소 7명이 사망했다.'))  # 품사

print()
ko = Komoran()
print(ko.pos('시속 200㎞에 달하는 강풍을 동반한 태풍 키아란이다. 서유럽을 강타하며 최소 7명이 사망했다.'))  # 품사 태깅
print(ko.nouns('시속 200㎞에 달하는 강풍을 동반한 태풍 키아란이다. 서유럽을 강타하며 최소 7명이 사망했다.'))  # 명사
print(ko.morphs('시속 200㎞에 달하는 강풍을 동반한 태풍 키아란이다. 서유럽을 강타하며 최소 7명이 사망했다.'))  # 품사