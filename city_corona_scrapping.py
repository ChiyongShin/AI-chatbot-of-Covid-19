import pymysql
import csv
import requests
import re
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="
res = requests.get(url, headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

# # 시 도별 확진 환자 수 csv 파일로 변환

# city_corona_db = "city_corona_db.csv"
# city_corona_file = open(city_corona_db, "w", encoding="utf-8", newline="")
# writer = csv.writer(city_corona_file)
# title1 = "City_Name	Confirmed_Patient	Quarantine	Isolation_Release	Dead	Incident_rate	City_Code".split("\t")
# writer.writerow(title1)
city_daily_db = "city_daily_db.csv"
city_daily_file = open(city_daily_db, "w", encoding="utf-8", newline="")
writer = csv.writer(city_daily_file)
title2 = "City_Code	Daily_Change_Total	Daily_Change_Local	Daily_Change_Imported".split("\t")
writer.writerow(title2)


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
        x[0] = "Lazaretto"


city_code = 1
data_rows = soup.find("table", attrs={"class": "midsize"}).find("tbody").find_all("tr")
for row in data_rows:
    data_set = []
    citys = row.find_all("th")
    city_name = [city.get_text() for city in citys]

    match_city(city_name)

    columns = row.find_all("td")

    for column in columns:
        data = column.get_text()
        if "," in data:
            comma = data.count(',')
            data = re.findall("\\d+", data)
            for i in range(1, comma + 1):
                data[0] += data[i]
            for i in range(0, comma):
                data.pop()
            data = data[0]
        if "-" in data:
            data = '0'
        data_set.append(data)
    city_name.extend(data_set)
    city_name.append(city_code)
    city_code += 1

    city_corona = []
    city_daily = []
    city_corona.append(city_name[0])
    city_daily.append(city_name[9])
    for i in range(4, 10):
        city_corona.append(city_name[i])
    for j in range(1, 4):
        city_daily.append(city_name[j])

    conn = pymysql.Connect(host="localhost", user="root", password="1234", db="db")
    curs = conn.cursor()
    # city_corona_db_update = """
    # UPDATE city_corona_db SET City_Name='{}', Confirmed_Patient='{}',Quarantine='{}',Isolation_Release='{}',
    # Dead='{}',Incident_rate='{}' WHERE City_Code='{}'
    # """.format(city_corona[0], city_corona[1], city_corona[2], city_corona[3], city_corona[4], city_corona[5],
    #            city_corona[6])

    city_daily_corona_db_update = """
    UPDATE city_daily_db SET Daily_Change_Total='{}', Daily_Change_Local='{}', Daily_Change_Imported='{}'
    WHERE City_Code='{}'
    """.format(city_daily[1], city_daily[2], city_daily[3], city_daily[0])
    # curs.execute(city_corona_db_update)
    curs.execute(city_daily_corona_db_update)
    conn.commit()

    conn.close()
    # writer.writerow(city_corona)
    writer.writerow(city_daily)

