import csv
import requests
import re
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=12&ncvContSeq=&contSeq=&board_id=&gubun="
res = requests.get(url,headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

domestic_corona_db = "domestic_corona_db.csv"
domestic_corona_file = open(domestic_corona_db,"w",encoding="utf-8",newline="")
writer = csv.writer(domestic_corona_file)

tables = soup.find("table",attrs={"class":"midsize big"})
locations = tables.find_all("tr")


print(locations)