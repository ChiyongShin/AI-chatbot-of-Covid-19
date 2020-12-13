import pymysql
import csv
import requests
import re
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=14&ncvContSeq=&contSeq=&board_id=&gubun="
url_en = "http://ncov.mohw.go.kr/en/bdBoardList.do?brdId=16&brdGubun=163&dataGubun=&ncvContSeq=&contSeq=&board_id=&gubun="
res = requests.get(url_en, headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

global_corona_db = "global_corona_db.csv"
global_corona_file = open(global_corona_db, "w", encoding="utf-8", newline="")
writer = csv.writer(global_corona_file)
title = "Country_Code	Country	Confirmed".split("\t")

writer.writerow(title)

countries = soup.find_all("td", attrs={"class": "w_bold"})
co_list_a = []
for country in countries:

    country_name = country.get_text()
    if "Deceased" in country_name:
        continue
    else:
        co_list_a.append(country_name)

res = requests.get(url, headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

countries = soup.find_all("td", attrs={"class": "w_bold"})
j = 0

co_list_b = []
for country in countries:

    co_set = ""
    co = country.find_next("td").get_text()
    for i in range(0, 15):
        if re.match("명", co[i]):
            j = i
            # print(j)
            break
    for a in range(0, j):
        co_set = co_set + co[a]

    if "," in co_set:
        comma = co_set.count(',')
        co_set = re.findall("\\d+", co_set)
        for i in range(1, comma + 1):
            co_set[0] += co_set[i]
        for i in range(0, comma):
            co_set.pop()
        co_set = co_set[0]
    co_list_b.append(co_set)

for i in range(0, 188):
    co_list = []
    co_list.append(i + 1)
    co_list.append(co_list_a[i])
    co_list.append(co_list_b[i])
    #
    conn = pymysql.Connect(host="localhost", user="root", password="1234", db="db")
    curs = conn.cursor()
    db_update = """
    UPDATE global_corona_db SET Confirmed='{}' WHERE Country_Code ='{}'
    """.format(co_list[2], co_list[0])

    curs.execute(db_update)
    conn.commit()
    conn.close()

    writer.writerow(co_list)