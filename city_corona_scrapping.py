import csv
import requests
import re
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="
res = requests.get(url,headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

# # 시 도별 확진 환자 수 csv 파일로 변환

city_corona_db = "city_corona_db.csv"
city_corona_file = open(city_corona_db,"w",encoding="utf-8",newline="")
writer = csv.writer(city_corona_file)
title = "City_Name	Total	Domestic_Occurrence	Foreign_Inflow	Confirmed_Patient	Quarantine	Isolation_Release	Dead	Incident_rate".split("\t")

writer.writerow(title)

def match_city(x):
    if "합계" in x:
        x[0] = "Total"
    elif "서울" in x:
        x[0] = "Seoul"
    elif "부산" in x:
        x[0] = "Busan"
    elif "대구" in x:
        x[0] = "Daegu"
    elif "인천" in x:
        x[0] = "Incheon"
    elif "광주" in x:
        x[0] = "Gwangju"
    elif "대전" in x:
        x[0] = "Daejeon"
    elif "울산" in x:
        x[0] = "Ulsan"
    elif "세종" in x:
        x[0] = "Sejong"
    elif "경기" in x:
        x[0] = "Gyeonggi" 
    elif "강원" in x:
        x[0] = "Gangwon"
    elif "충북" in x:
        x[0] = "ChungBuk"
    elif "충남" in x:
        x[0] = "ChungNam"
    elif "전북" in x:
        x[0] = "JeonBuk"
    elif "전남" in x:
        x[0] = "JeonNam"
    elif "경북" in x:
        x[0] = "GyeongBuk"
    elif "경남" in x:
        x[0] = "GyeongNam"
    elif "제주" in x:
        x[0] = "Jeju"
    elif "검역" in x:
        x[0] = "Quarantine"
    

data_rows = soup.find("table",attrs={"class":"midsize"}).find("tbody").find_all("tr")
for row in data_rows:
    citys = row.find_all("th")
    city_name = [city.get_text() for city in citys]
    match_city(city_name)
    columns = row.find_all("td")
    data = [column.get_text() for column in columns]
    data = city_name + data
    writer.writerow(data)