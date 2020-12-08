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
city_corona_file = open(city_corona_db,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(city_corona_file)
title = "합계	국내발생	해외유입	확진환자	격리중	격리해제	사망자	발생률".split("\t")

writer.writerow(title)

data_rows = soup.find("table",attrs={"class":"midsize"}).find("tbody").find_all("tr")
for row in data_rows:
    columns = row.find_all("td")
    data = [column.get_text() for column in columns]
    writer.writerow(data)
