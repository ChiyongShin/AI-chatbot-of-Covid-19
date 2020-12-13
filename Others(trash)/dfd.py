import pymysql
import csv
import requests
import re
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
url = "http://ncov.mohw.go.kr/en/bdBoardList.do?brdId=16&brdGubun=163&dataGubun=&ncvContSeq=&contSeq=&board_id=&gubun="
res = requests.get(url,headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

countries = soup.find_all("td",attrs={"class":"w_bold"})

f = open("text.txt", "w")
for i in range(0,188):

    f.write("co_list[{}]".format(i))
f.close()

# for country in countries:
#     co_text = country.get_text()
#     if " " in co_text:
#         re.sub(r"\s+","",co_text)
#         print(co_text)
    # print(co_text)
    # print(type(co_text))
    # co_text = '"'+co_text + '"' 
    # f.write(co_text)

# f.close()