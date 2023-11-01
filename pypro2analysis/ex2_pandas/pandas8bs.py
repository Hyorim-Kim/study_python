# BeautifulSoup의 find, select 연습
from bs4 import BeautifulSoup
htmlData = """
<html>
<body>
<h1>제목 태그</h1>
<p>문단 1</p>
<p>문단 2</p>
</body>
</html>
"""
print(type(htmlData))  # <class 'str'>
soup = BeautifulSoup(htmlData, 'html.parser')  # BeautifulSoup 객체 생성 - BeautifulSoup 모듈 지원 명령 사용 가능
print(type(soup))  # <class 'bs4.BeautifulSoup'>
h1 = soup.html.body.h1  # 순서대로 타고 들어서 최초의 h1을 만남
print('h1 : ', h1.text, ' ', h1.string)
p1 = soup.html.body.p  # 최초의 p 태그를 만남
print('p1 : ', p1.text)
p2 = p1.next_sibling.next_sibling
print('p2 : ', p2.text)
# ------------------------------------위 방법 사용 안함

print('\nfind함수 : 반환값이 단수 사용')
htmlData2 = """
<html>
<body>
<h1 id="title">제목 태그</h1>
<p>문단 1</p>
<p id="my" class="our">문단 2</p>
</body>
</html>
"""
soup2 = BeautifulSoup(htmlData2, 'html.parser')  # BeautifulSoup 객체 생성
print(soup2.p, ' ', soup2.p.string)
print(soup2.find('p').string)
print(soup2.find('p', id='my').string)  # option
print(soup2.find(id="title").string)
print(soup2.find(id="my").string)
print(soup2.find(class_="our").string)
print(soup2.find(attrs={'class':'our'}).string)  # attribute
print(soup2.find(attrs={'id':'my'}).string)
# id를 제외하고는 모두 복수를 반환하지만 find를 사용했기 때문에 복수를 처리할 수 없다. 


print('\nfind_all(), findall() : 반환값이 복수 사용')
htmlData3 = """
<html>
<body>
<h1 id="title">제목 태그</h1>
<p>문단 1</p>
<p id="my" class="our">문단 2</p>
<div>
     <a href="https://www.naver.com">네이버</a><br/>
     <a href="https://www.daum.net">다음</a><br/>
</div>
</body>
</html>
"""
soup3 = BeautifulSoup(htmlData3, 'lxml')
print(soup3.find_all("a"))
print(soup3.find_all(["a", "p"]))
print(soup3.findAll(["a"]))
print()
links = soup3.findAll(["a"])
print(links)
for i in links:
    href = i.attrs['href']
    text = i.string  # or text
    print(href, ' ', text)

print('\n정규 표현식 사용')
import re
links2 = soup3.find_all(href=re.compile(r'^https'))
for j in links2:
    print(j.attrs['href'])

"""
print('\n벅스 뮤직 사이트에서 곡 제목 읽기')
from urllib.request import urlopen
url = urlopen("https://music.bugs.co.kr/chart")
soup = BeautifulSoup(url.read(), 'html.parser')  # html.parser / lxml : parser
# print(soup)  # 읽었음, beautiful soup 객체
musics = soup.find_all('td', class_='check')  # class가 check인 td 엘리먼트 찾음
# print(musics)  # 들어온거 확인
for i, music in enumerate(musics):  # enumerate를 사용하면 인덱스 확인가능
    print("{}위 : {}".format(i+1, music.input['title']))  # i는 0부터 출발하니까 +1
"""

print('\nselect_one, select : css의 selector를 사용')
htmlData4 = """
<html>
<body>
<div id="hello">
     <a href="https://www.naver.com">네이버</a><br/>
     <span>
         <a href="https://www.daum.net">다음</a><br/>
     </span>
     <ul class="world">
          <li>안녕</li>
          <li>반갑다</li>
     </ul>
</div>
<div id="hi" class="good">
     두번째 디브 태그
</div>
</body>
</html>
"""
soup4 = BeautifulSoup(htmlData4, 'lxml')
kbs = soup4.select_one("div#hello > a")  # 단수 선택, id hello의 div 태그 안의 a 태그
print('kbs : ', kbs, ' ', kbs.string)
kbs2 = soup4.select_one("div.good")  # class good의 div 태그
print('kbs2 : ', kbs2, ' ', kbs2.string)
print()
mbc = soup4.select("div#hello ul.world > li")  # 복수 선택, hello>ul : 직계, hello ul : 자손(손자도 잡힘)
print('mbc : ', mbc)
for a in mbc:
    print(a.string, ' ')

print()
msg = list()
for a in mbc:
    msg.append(a.string)

import pandas as pd
df = pd.DataFrame(msg, columns=['자료'])
print(df)
print(df.to_json())
