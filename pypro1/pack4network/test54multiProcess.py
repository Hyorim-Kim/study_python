# 멀티프로세싱을 통한 웹 스크래핑
import requests  # web 사이트에 접근 가능하게 해줌
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool  # Pool을 사용했을 때 병렬 처리로 인해 시간이 단축되는지 확인

# 스크래핑 대상 컨텐츠 : https://beomi.github.io/beomi.github.io_old/
def get_links():
    data = requests.get('https://beomi.github.io/beomi.github.io_old/').text  # text : 문자열 읽음
    soup = bs(data, 'html.parser')  # BeautifulSoup 객체로 변환
    print(type(soup))  # BeautifulSoup 객체 확인, <class 'bs4.BeautifulSoup'>
    my_titles = soup.select('h3 > a')  # h3의 하위 element로 h3 있음
    data = []
    
    for title in my_titles:
        data.append(title.get('href'))
        
    return data

def get_content(link):
    abs_link = "https://beomi.github.io" + link
    #print(abs_link)  # 링크 잘 찍힘
    data = requests.get(abs_link).text  # 링크 접속한 후 data 가져옴
    print(data)
    #soup = bs(data, 'html.parser')  # BeautifulSoup 타입 객체 생성
    #print(soup.select('h1')[0].text)
    
if __name__ == '__main__':
    #print(get_links())  # get_links()의 실행 결과 출력
    #print(len(get_links()))  # 개수 출력
    start_time = time.time()  # 현재 시간
    '''
    for link in get_links():  # 직렬
        get_content(link)
    '''
    pool = Pool(processes = 4)  # 병렬
    pool.map(get_content, get_links())  # map(func, parameter)
    
    print("---%s 초"%(time.time() - start_time))
    # 직렬 : 9.718675136566162 초
    # 병렬 : 6.103675842285156 초
