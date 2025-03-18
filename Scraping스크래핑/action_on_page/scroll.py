import chromedriver_autoinstaller  # 크롬드라이버 자동 설치 및 업데이트

import requests  # HTTP 요청을 보내 웹페이지의 HTML 가져오기

from bs4 import BeautifulSoup as bs  # HTML을 파싱하여 원하는 데이터 추출

import time  # 코드 실행 간 대기 시간 설정 (예: time.sleep)
from random import randint  # 랜덤한 정수 생성 (예: 요청 간격 조정)
import pandas as pd  # 데이터 분석 및 엑셀, CSV 저장

from selenium import webdriver  # 웹 브라우저 자동화
from selenium.webdriver.common.by import By  # HTML 요소 찾기 (예: By.CSS_SELECTOR)
from selenium.webdriver.common.action_chains import ActionChains  # 마우스/키보드 액션 자동화
from selenium.webdriver.support.ui import WebDriverWait  # 특정 요소가 나타날 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 특정 조건 충족 여부 확인
from selenium.webdriver.common.keys import Keys  # 키보드 입력 자동화 (예: 엔터 키 입력)

def scroll_down(driver):
    """스크롤을 내려서 추가 데이터를 로드하는 함수"""
    last_height = driver.execute_script("return document.body.scrollHeight")  # 현재 문서 높이 가져오기
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 페이지 끝까지 스크롤
        time.sleep(2)  # 로딩 대기
        new_height = driver.execute_script("return document.body.scrollHeight")  # 새로운 높이 확인
        if new_height == last_height:
            break  # 더 이상 로딩할 데이터가 없으면 종료
        last_height = new_height