# 멀티프로세싱을 통한 웹 스크래핑
import requests
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool

# 스크래핑 대상 컨텐 츠 : https://beomi.github.io/beomi.github.io_old/
