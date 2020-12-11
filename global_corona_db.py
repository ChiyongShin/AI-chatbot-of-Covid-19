import pymysql
import csv
import requests
import re
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=14&ncvContSeq=&contSeq=&board_id=&gubun="
res = requests.get(url,headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

global_corona_db = "global_corona_db.csv"
global_corona_file = open(global_corona_db,"w",encoding="utf-8",newline="")
writer = csv.writer(global_corona_file)
# title = "City_Name	Increasing_Total_Ctp	Increasing_Domestic_Occurrence_Ctp	Increasing_Foreign_Inflow_Ctp	Confirmed_Patient	Quarantine	Isolation_Release	Dead	Incident_rate".split("\t")
title = "China	Hong Kong	Taiwan	Macau	Japan	Singapore	Thailand	Malaysia	Vietnam	India	Philippines	Cambodia	Nepal	Sri Lanka	Afghanistan	Pakistan	Indonesia	Bhutan	Maldives	Bangladesh	Brunei	Mongolia	Kazakhstan	Uzbekistan	Kyrgyzstan	East Timor	Myanmar	Laos	Tajikistan	Iran	Bahrain	Egypt	Iraq	Jordan	Kuwait	Lebanon	Libya	Morocco	Oman	Qatar	Saudi Arabia	Syria	Tunisia	Israel	United Arab Emirates	Algeria	Yemen	United States of America	Canada	Mexico	Panama	Honduras	Guatemala	Costa Rica	Elsalvador	Belize	Nicaragua	Dominican Republic	Cuba	Jamaica	Trinidad and Tobago	Haiti	Bahamas	Barbados	Antigua and Barbuda	Grenada	Saint Lucia	Saint Vincent and the Grenadines	Commonwealth of Dominica	Saint Kitts and Nevis	Brazil	Peru	Ecuador	Chile	Columbia	Argentina	Bolivia	Uruguay	Paraguay	Venezuela	Guyana	Suriname	Italy	Germany	France	United Kingdom	Spain	Austria	Croatia	Finland	Sweden	Switzerland	Belgium	Denmark	Estonia	Georgia	Greece	North Macedonia	Norway	Romania	Netherlands	Belarus	Lithuania	San Marino	Azerbaijan	Iceland	Monaco	Luxemburg	Armenia	Ireland	Czech Republic	Portugal	Latvia	Andorra	Poland	Ukraine	Hungary	Bosnia and Herzegovina	Slovenia	Liechtenstein	Serbia	Slovakia	Bulgaria	Malta	Moldova	Albania	Cyprus	Turkey	Montegro	Kosovo	Russia	Australia	New Zealand	Fiji	Papua New Guinea	Marshall Islands	Solomon Islands	Vanuatu	Nigeria	Senegal	Cameroon	Republic of South Africa	Togo	Burkina Faso	DRCongo	Cote dIvoire	Sudan	Ethiopia	Gabon	Ghana	Guinea	Kenya	Namibia	Central African Republic	Congo	Equatorial Guinea	Swatini	Mauritania	Rwanda	Seychelles	Benin	Liberia	Tanzania	Djibouti	Gambia	Zambia	Mauritius	Chad	Niger	Cape Verde	Zimbabwe	Somalia	Madagascar	Angola	Eritrea	Uganda	Mozambique	Guinea Bissau	Mali	Botswana	Brundi	Sierra Leone	Malawi	South Sudan	Sao Tome and Principe	Comoros	Lesotho	Others".split("\t")
# title = ["China""Hong Kong","Taiwan","Macau","Japan","Singapore","Thailand","Malaysia","Vietnam","India","Philippines","Cambodia","Nepal","Sri Lanka","Afghanistan","Pakistan","Indonesia","Bhutan","Maldives","Bangladesh","Brunei","Mongolia","Kazakhstan","Uzbekistan","Kyrgyzstan","East Timor","Myanmar","Laos","Tajikistan","Iran","Bahrain","Egypt","Iraq","Jordan","Kuwait","Lebanon","Libya","Morocco","Oman","Qatar","Saudi Arabia","Syria","Tunisia","Israel","United Arab Emirates","Algeria","Yemen","United States of America","Canada","Mexico","Panama","Honduras","Guatemala","Costa Rica","Elsalvador","Belize","Nicaragua","Dominican Republic","Cuba","Jamaica","Trinidad and Tobago","Haiti","Bahamas","Barbados","Antigua and Barbuda","Grenada","Saint Lucia","Saint Vincent and the Grenadines","Commonwealth of Dominica","Saint Kitts and Nevis","Brazil","Peru","Ecuador","Chile","Columbia","Argentina","Bolivia","Uruguay","Paraguay","Venezuela","Guyana","Suriname","Italy","Germany","France","United Kingdom","Spain","Austria","Croatia","Finland","Sweden","Switzerland","Belgium","Denmark","Estonia","Georgia","Greece","North Macedonia","Norway","Romania","Netherlands","Belarus","Lithuania","San Marino","Azerbaijan","Iceland","Monaco","Luxemburg","Armenia","Ireland","Czech Republic","Portugal","Latvia","Andorra","Poland","Ukraine","Hungary","Bosnia and Herzegovina","Slovenia","Liechtenstein","Serbia","Slovakia","Bulgaria","Malta","Moldova","Albania","Cyprus","Turkey","Montegro","Kosovo","Russia","Australia","New Zealand","Fiji","Papua New Guinea","Marshall Islands","Solomon Islands","Vanuatu","Nigeria","Senegal","Cameroon","Republic of South Africa","Togo","Burkina Faso","DRCongo","Cote d��Ivoire","Sudan","Ethiopia","Gabon","Ghana","Guinea","Kenya","Namibia","Central African Republic","Congo","Equatorial Guinea","Swatini","Mauritania","Rwanda","Seychelles","Benin","Liberia","Tanzania","Djibouti","Gambia","Zambia","Mauritius","Chad","Niger","Cape Verde","Zimbabwe","Somalia","Madagascar","Angola","Eritrea","Uganda","Mozambique","Guinea Bissau","Mali","Botswana","Brundi","Sierra Leone","Malawi","South Sudan","Sao Tome and Principe","Comoros","Lesotho","Others"]
# title = ["China""Hong Kong""Taiwan""Macau""Japan""Singapore""Thailand""Malaysia""Vietnam""India""Philippines""Cambodia""Nepal""Sri Lanka""Afghanistan""Pakistan""Indonesia""Bhutan""Maldives""Bangladesh""Brunei""Mongolia""Kazakhstan""Uzbekistan""Kyrgyzstan""East Timor""Myanmar""Laos""Tajikistan""Iran""Bahrain""Egypt""Iraq""Jordan""Kuwait""Lebanon""Libya""Morocco""Oman""Qatar""Saudi Arabia""Syria""Tunisia""Israel""United Arab Emirates""Algeria""Yemen""United States of America""Canada""Mexico""Panama""Honduras""Guatemala""Costa Rica""Elsalvador""Belize""Nicaragua""Dominican Republic""Cuba""Jamaica""Trinidad and Tobago""Haiti""Bahamas""Barbados""Antigua and Barbuda""Grenada""Saint Lucia""Saint Vincent and the Grenadines""Commonwealth of Dominica""Saint Kitts and Nevis""Brazil""Peru""Ecuador""Chile""Columbia""Argentina""Bolivia""Uruguay""Paraguay""Venezuela""Guyana""Suriname""Italy""Germany""France""United Kingdom""Spain""Austria""Croatia""Finland""Sweden""Switzerland""Belgium""Denmark""Estonia""Georgia""Greece""North Macedonia""Norway""Romania""Netherlands""Belarus""Lithuania""San Marino""Azerbaijan""Iceland""Monaco""Luxemburg""Armenia""Ireland""Czech Republic""Portugal""Latvia""Andorra""Poland""Ukraine""Hungary""Bosnia and Herzegovina""Slovenia""Liechtenstein""Serbia""Slovakia""Bulgaria""Malta""Moldova""Albania""Cyprus""Turkey""Montegro""Kosovo""Russia""Australia""New Zealand""Fiji""Papua New Guinea""Marshall Islands""Solomon Islands""Vanuatu""Nigeria""Senegal""Cameroon""Republic of South Africa""Togo""Burkina Faso""DRCongo""Cote d��Ivoire""Sudan""Ethiopia""Gabon""Ghana""Guinea""Kenya""Namibia""Central African Republic""Congo""Equatorial Guinea""Swatini""Mauritania""Rwanda""Seychelles""Benin""Liberia""Tanzania""Djibouti""Gambia""Zambia""Mauritius""Chad""Niger""Cape Verde""Zimbabwe""Somalia""Madagascar""Angola""Eritrea""Uganda""Mozambique""Guinea Bissau""Mali""Botswana""Brundi""Sierra Leone""Malawi""South Sudan""Sao Tome and Principe""Comoros""Lesotho""Others"]

writer.writerow(title)

countries = soup.find_all("td",attrs={"class":"w_bold"})
j=0
co_list = []
for country in countries:
    co_set =""
    co = country.find_next("td").get_text()
    for i in range(0,15):
        if re.match("명",co[i]):
            j= i
            # print(j)
            break
    for a in range(0,j):
        co_set = co_set + co[a]
    
    if "," in co_set:
            comma = co_set.count(',')
            co_set = re.findall("\\d+",co_set)
            for i in range(1,comma+1):
                co_set[0] += co_set[i]
            for i in range(0, comma):
                co_set.pop()
            co_set = co_set[0]
    co_list.append(co_set)
# print(co_list)
writer.writerow(co_list)
    # print(co_set)
    
    # if " " in co:
        # print(2)
    # f.write(co)
    #
    # coc = re.findall("\\d+",co)
    # print(coc)
    # print(coc)
    # if "," in co:
    #     co1 = co.replace("\t"," ")
    #     print(co)
# f.close()