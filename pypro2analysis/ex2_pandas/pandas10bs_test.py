# 이름, 가격 정보, 가격의 평균과 표준편차, 최고가격 최저가격
import urllib.request as req
from bs4 import BeautifulSoup
import urllib

print('교촌 치킨 자료 읽기')
url = "https://www.kyochon.com/menu/chicken.asp"
chicken = req.urlopen(url)

soup = BeautifulSoup(chicken, 'lxml')

name = soup.select("dl.txt > dt")
price = soup.select("p.money > strong")

name = [name.string.strip() for name in name]  # 이름에서 <dt>제거
prices = [int(price.get_text().replace(',', '').strip()) for price in price]  # 가격 콤마 제거
#print(name, price)  # 출력 확인

for name,price in zip(name, prices):
    print(f'이름: {name}, 가격: {price}원')


# 평균, 표준편차 계산
# 데이터 프레임에 넣어서 하기
import numpy as np
std = np.std(prices)
mean = np.mean(prices)
max = np.max(prices)
min = np.min(prices)
print(f'가격 평균: {round(mean, 2)}원, 표준편차: {round(std, 2)}')
print(f'최고가격: {max}원, 최저가격: {min}원')
