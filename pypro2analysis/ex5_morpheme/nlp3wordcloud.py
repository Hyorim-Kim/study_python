# 웹 문서에서 검색 자료를 읽어 형태소 분석 후 명사만 추출한 다음 워드클라우드 차트 그리기

# pip install pygame, pip install simplejson, pip install pytagcloud
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote

# keyword = input('검색어 : ')
keyword = '단풍'
print(quote(keyword))

# 신문사 검색 기능을 이용
targetUrl = "https://www.donga.com/news/search?query=" + quote(keyword)
print(targetUrl)

source = urllib.request.urlopen(targetUrl)

soup = BeautifulSoup(source, 'lxml')
# print(soup)
msg =""
for title in soup.select('div.rightList > span.tit'):
    title_link = title.find('a')
    # print(title_link)  # 링크 잡아와야함
    articleUrl = title_link['href']
    # print(articleUrl)
    try:
        sourceArticle = urllib.request.urlopen(articleUrl)  # 실제 기사 내용 페이지 읽기
        soup = BeautifulSoup(sourceArticle, 'lxml', from_encoding='utf-8')
        contents = soup.select('div.article_txt')
        
        for imsi in contents:
            item = str(imsi.find_all(string = True))
            # print(item)
            msg = msg + item
        
    except Exception as e:
        pass  # error 무시

print(msg)

from konlpy.tag import Okt
from collections import Counter

okt = Okt()
nouns = okt.nouns(msg)  # 명사별로 자르기
print(nouns)

result = []
for imsi in nouns:
    if len(imsi) > 1:
        result.append(imsi)
        
print(result)

count = Counter(result)
print(count)
tag = count.most_common(60)  # 상위 50개 참여
print(tag)  # [('한국', 24), ('코스', 16), ... pytagcloud를 사용하기 위해 튜플타입으로 생성 


import pytagcloud
taglist = pytagcloud.make_tags(tag, maxsize=100)
print(taglist)  # [{'color': (24, 178, 175), 'size': 115, 'tag': '한국'}, ...

pytagcloud.create_tag_image(taglist, output='word.png', size=(1000,600), background=(254,225,232), fontname="Korean", rectangular=True)

# 저장된 이미지 읽기
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('word.png')
plt.imshow(img)
plt.show()

import webbrowser
webbrowser.open('word.png')
