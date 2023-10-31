# BeautifulSoup : HTML 및 XML(마크업 언어만) 파일에서 데이터를 가져오는 Python 라이브러리
# 문서 내의 element(tag, 요소) 및 attribute(속성) 찾기 함수 : find(), find_all(), select_one(), select()

import requests  
from bs4 import BeautifulSoup

def go():
    base_url = "http://www.naver.com:80/index.html"
    
    #storing all the information including headers in the variable source code
    source_code = requests.get(base_url)
    print(source_code)  # <Response [200]>
    
    #sort source code and store only the plaintext
    plain_text = source_code.text
    print(type(plain_text))  # <class 'str'> 문자열이기 때문에 접근 못함
    
    #converting plain_text to Beautiful Soup object so the library can sort thru it
    convert_data = BeautifulSoup(plain_text, 'lxml') 
    print(type(convert_data))  # <class 'bs4.BeautifulSoup'> 형변환이 이루어짐
    
    for link in convert_data.findAll('a'):  # a 태그를 몽땅 잡아옴
        href = link.get('href')  #Building a clickable url   hrel 속성값만 빼옴
        print(href)                          #displaying href

go()