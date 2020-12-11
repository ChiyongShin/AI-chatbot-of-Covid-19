import csv
import pymysql
import requests
import re
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
url = "http://ncov.mohw.go.kr/"
res = requests.get(url,headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

day_corona_db = "day_corona_db.csv"
day_corona_file = open(day_corona_db,"w",encoding="utf-8",newline="")
writer = csv.writer(day_corona_file)

title = "Order	Date	Confirmed	Cure".split("\t")

writer.writerow(title)


info_week = soup.find("div",attrs={"class":"info_week"})
day = info_week.find_all("th",attrs={"scope":"row"})
day_table = info_week.find_all("td")
order = 1

for i in range(1,8):
    day_complete = day_table[(i-1)*4].get_text()
    day_confirm = day_table[(i-1)*4+2].get_text()
    if "," in day_complete:
        comma = day_complete.count(',')
        day_complete = re.findall("\\d+",day_complete)
        for i in range(1,comma+1):
            day_complete[0] += day_complete[i]
        for i in range(0,comma):
            day_complete.pop()
        day_complete = day_complete[0]

    if "," in day_confirm:
        comma = day_confirm.count(',')
        day_confirm = re.findall("\\d+",day_confirm)
        for i in range(1,comma+1):
            day_confirm[0] += day_confirm[i]
        for i in range(0,comma):
            day_confirm.pop()
        day_confirm = day_confirm[0]
    
    day_text = day[i-1].get_text()
    if "월" in day_text:
        day_text = re.findall("\\d+",day_text)
        day_text[0] = day_text[0] + '.' + day_text[1]
        day_text = day_text[0]
    day_info = [order,day_text,day_confirm,day_complete]
    

    conn = pymysql.Connect(host="localhost", user="root", password="root", db="db")
    curs = conn.cursor()
    db_update = """
    UPDATE day_corona_db SET Date='{}', Confirmed='{}', Cure='{}' WHERE Order='{}'
    """.format(day_info[0],day_info[1],day_info[2],order)
    order += 1
    curs.execute(db_update)
    conn.commit()
    rows = curs.fetchall()
    for row in rows:
        print(row)
    conn.close()

    writer.writerow(day_info)