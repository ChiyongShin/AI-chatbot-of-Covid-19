import csv
import requests
import re
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
url = "http://ncov.mohw.go.kr/"
res = requests.get(url,headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

# # 시 도별 확진 환자 수 csv 파일로 변환

city_corona_db = "city_corona_db.csv"
city_corona_file = open(city_corona_db,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(city_corona_file)

citys = soup.find_all("button",attrs={"data-city":re.compile("^map_city")})
for city in citys:
    city_name = city.find("span",attrs={"class":"name"}).get_text()
    city_cnt = city.find("span", attrs={"class":"num"}).get_text()

    if "," in city_cnt:
        comma = city_cnt.count(',')
        city_cnt = re.findall("\\d+",city_cnt)
        for i in range(1,comma+1):
            city_cnt[0] += city_cnt[i]
        for i in range(0,comma):
            city_cnt.pop()
        city_cnt = city_cnt[0]

    city_info = [city_name,city_cnt]
    writer.writerow(city_info)


# # 누적 확진자 수 csv 파일로 변환

cumulative_corona_db = "cumulative_corona_db.csv"
cumulative_corona_file = open(cumulative_corona_db,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(cumulative_corona_file)

cityinfo = soup.find("ul",attrs={"class":"cityinfo"})
for count in cityinfo:
    count_tit = count.find("span",attrs={"class":re.compile("tit$")})
    count_tit = count_tit.get_text()
    
    count_num = count.find("span",attrs={"class":re.compile("num$")})
    count_num = count_num.get_text()
    if "(" in count_num:
        count_num = count_num[1:-1]
        if "+" in count_num:
            count_num = count_num[1:]

    if "," in count_num:
        comma = count_num.count(',')
        count_num = re.findall("\\d+",count_num)
        for i in range(1,comma+1):
            count_num[0] += count_num[i]
        for i in range(0,comma):
            count_num.pop()
        count_num = count_num[0]
   
    cumulative_info = [count_tit,count_num]
    writer.writerow(cumulative_info)

# # # 일별 확진 환자 수 csv 파일로 변환

day_corona_db = "day_corona_db.csv"
day_corona_file = open(day_corona_db,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(day_corona_file)

info_week = soup.find("div",attrs={"class":"info_week"})
day = info_week.find_all("th",attrs={"scope":"row"})
day_table = info_week.find_all("td")

for i in range(1,8):
    day_complete = day_table[(i-1)*4].get_text()
    day_comfirm = day_table[(i-1)*4+2].get_text()

    if "," in day_complete:
        comma = day_complete.count(',')
        day_complete = re.findall("\\d+",day_complete)
        for i in range(1,comma+1):
            day_complete[0] += day_complete[i]
        for i in range(0,comma):
            day_complete.pop()
        day_complete = day_complete[0]

    if "," in day_comfirm:
        comma = day_comfirm.count(',')
        day_comfirm = re.findall("\\d+",day_comfirm)
        for i in range(1,comma+1):
            day_comfirm[0] += day_comfirm[i]
        for i in range(0,comma):
            day_comfirm.pop()
        day_comfirm = day_comfirm[0]
    
    day_info = [day[i-1].get_text(),day_comfirm,day_complete]
    writer.writerow(day_info)


# # # 검사 현황 csv 파일로 변환

inspection_corona_db = "inspection_corona_db.csv"
inspection_corona_file = open(inspection_corona_db,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(inspection_corona_file)

inspection = soup.find("ul",attrs={"class":"suminfo"})
# inspecion_data : inspection에서 li 속성만 추출
inspection_li_data = inspection.find_all("li")
for i in range(0,3):
    cumulative_inspection_tit = inspection_li_data[i].find("span",attrs={"class":"tit"}).get_text()
    cumulative_inspection = inspection_li_data[i].find("span",attrs={"class":"num"}).get_text()[:-2]
    # print(cumulative_inspection_tit,":",cumulative_inspection)
    if "," in cumulative_inspection:
        comma = cumulative_inspection.count(',')
        cumulative_inspection = re.findall("\\d+",cumulative_inspection)
        for i in range(1,comma+1):
            cumulative_inspection[0] += cumulative_inspection[i]
        for i in range(0,comma):
            cumulative_inspection.pop()
        cumulative_inspection = cumulative_inspection[0]
    
    inspection_info = [cumulative_inspection_tit,cumulative_inspection]
    writer.writerow(inspection_info)
   

# # # 검사 결과 csv 파일로 변환 

inspection_result_corona_db = "inspection_result_corona_db.csv"
inspection_result_corona_file = open(inspection_result_corona_db,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(inspection_result_corona_file)

inspection_result_data_data = soup.find_all("p",attrs={"class":re.compile("^numinfo")})
for inspection_result_data in inspection_result_data_data:
    # inspection_result_tit, inspection_result_num, inspection_result_percentage
    inspection_rt_data = inspection_result_data.find("span",attrs={"class":re.compile("tit$")})
    inspection_rn_data = inspection_result_data.find("span",attrs={"class":re.compile("rnum$")})
    inspection_rp_data = inspection_result_data.find("span",attrs={"class":re.compile("percentage$")})
    inspection_rt = inspection_rt_data.get_text()
    inspection_rn = inspection_rn_data.get_text()
    inspection_rp = inspection_rp_data.get_text()
    if "," in inspection_rn:
        comma = inspection_rn.count(',')
        inspection_rn = re.findall("\\d+",inspection_rn)
        for i in range(1,comma+1):
            inspection_rn[0] += inspection_rn[i]
        for i in range(0,comma):
            inspection_rn.pop()
        inspection_rn = inspection_rn[0]
    
    inspection_result_info = [inspection_rt,inspection_rn,inspection_rp[:-1]]
    writer.writerow(inspection_result_info)

