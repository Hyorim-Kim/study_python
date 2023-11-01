# Selenium 툴을 이용해 브라우저를 통제, 웹 크롤링 가능
# 뭐하는 녀석인지만 알아둘 것
from selenium import webdriver
import time

# browser = webdriver.Chrome()
# browser.implicitly_wait(5)
# browser.get('https://daum.net')
# browser.quit()

# browser = webdriver.Chrome()
# browser.get('http://www.google.com/xhtml');
# search_box = browser.find_element("name", "q")
# search_box.send_keys('파이썬')
# search_box.submit()
# time.sleep(5)
# browser.quit()

# 실습 예 : 화면 캡처
try:
    url = "https://www.daum.net"
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.get(url);
    browser.save_screenshot("daum_img.png")
    browser.quit()
    print('성공')
except Exception:
    print('에러')
