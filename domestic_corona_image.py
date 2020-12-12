import os
import pandas as pd 
import numpy as np 
import seaborn as sns
import pymysql
import plotly
import plotly.express as px
import matplotlib.pylab as plt
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
plt.rcParams['figure.figsize'] = [17, 6]




conn = pymysql.Connect(host="localhost", user="root", password="wlsdud369", db="db")
curs = conn.cursor()
label = []
data = []
sql = "select * from city_corona_db WHERE City_Name = 'total'"
try:
    curs.execute(sql)
    results = curs.fetchall()
    discresults = {}

    for row in results:
        City_Name = row[0] #도시이름
        Increasing_Total_Ctp = row[1] #전일대비확진환자 증감 합계
        Increasing_Domestic_Occurrence_Ctp = row[2] #전일대비확진환자 증감 국내 발생
        Increasing_Foreign_Inflow_Ctp = row[3] #전일대비확진환자 증감 해외유입
        Confirmed_Patient = row[4] #확진환자
        Quarantine = row[5] #확진환자 격리중
        Isolation_Release = row[6] #확진환자 격리해제
        Dead = row[7] #확진환자 사망자
        Incident_rate = row[8] #확진환자 발생률
        a = row[1] 
        b = row[2] 
        # c = row[3] 
        d = row[4]
        e = row[5]
        f = row[6]
        g = row[7]
        h = row[8]
        label = ['Increasing_Total_Ctp','Increasing_Domestic_Occurrence_Ctp','Confirmed_Patient','Quarantine','Isolation_Release','Dead']
        print(label)
        data = [a,b,d,e,f,g]
 


        
except:
    print('ERROR!!')

# for i in range(0,7):
#     data[i] = row[i+1]
# print(data) 

plt.barh(label, data)
# plt.text(label[], data[], data,                 # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
#     fontsize = 9, 
#     color='blue',
#     horizontalalignment='left',  # horizontalalignment (left, center, right)
#     verticalalignment='center')    # verticalalignment (top, center, bottom)
# plt.xticks(index, ll, fontsize=5)
plt.title('Domestic Status of COVID-19 by city and province', fontsize=15)
plt.xlabel('City', fontsize=3)
plt.ylabel('Confirmed Patient', fontsize=3)
# plt.xticks(index, label, fontsize=15)
# print(type(x),type(y))
plt.savefig("domestic_corona.png")
plt.show()
# plt.show()