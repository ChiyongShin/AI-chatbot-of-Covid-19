import csv
import requests
import re
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
url = "http://ncov.mohw.go.kr/"
res = requests.get(url,headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

inspection_corona_db = "inspection_corona_db.csv"
inspection_corona_file = open(inspection_corona_db,"w",encoding="utf-8",newline="")
writer = csv.writer(inspection_corona_file)

title = "Cumulative_Inspection_Count	Cumulative_Complete_Inspection	Cumulative_Confirmed_Rate	Testing_Count	Testing_Count_Rate	Result_Positive	Result_Positive_Rate	Result_Negative	Result_Negative_Rate".split("\t")
writer.writerow(title)

inspection = soup.find("ul",attrs={"class":"suminfo"})
inspection_li_data = inspection.find_all("span",attrs={"class":"num"})
inspection_info = []
for inspection_data in inspection_li_data:
    inspection_text = inspection_data.get_text()    
    if " " in inspection_text:
        inspection_text = inspection_text[:-2]
        if "," in inspection_text:
            comma = inspection_text.count(',')
            inspection_text = re.findall("\\d+",inspection_text)
            for i in range(1,comma+1):
                inspection_text[0] += inspection_text[i]
            for i in range(0,comma):
                inspection_text.pop()
            inspection_text = inspection_text[0]
        
    inspection_info.append(inspection_text)

inspection_result_data_data = soup.find_all("p",attrs={"class":re.compile("^numinfo")})
for inspection_result_data in inspection_result_data_data:
    inspection_rn_data = inspection_result_data.find("span",attrs={"class":re.compile("rnum$")})
    inspection_rp_data = inspection_result_data.find("span",attrs={"class":re.compile("percentage$")})
    inspection_rn = inspection_rn_data.get_text()
    inspection_rp = inspection_rp_data.get_text()
    print(inspection_rn,inspection_rp)
    if "%" in inspection_rp:
        inspection_rp = inspection_rp[:-2]

    if "," in inspection_rn:
        comma = inspection_rn.count(',')
        inspection_rn = re.findall("\\d+",inspection_rn)
        for i in range(1,comma+1):
            inspection_rn[0] += inspection_rn[i]
        for i in range(0,comma):
            inspection_rn.pop()
        inspection_rn = inspection_rn[0]
        inspection_info.append(inspection_rn)
        inspection_info.append(inspection_rp)
writer.writerow(inspection_info)