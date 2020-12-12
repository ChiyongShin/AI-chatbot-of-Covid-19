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
plt.rcParams['figure.figsize'] = [10, 6]




conn = pymysql.Connect(host="localhost", user="root", password="wlsdud369", db="db")
curs = conn.cursor()
Confirmed_set = []
sql = "select * from city_corona_db WHERE City_Name != 'total'"
try:
    curs.execute(sql)
    results = curs.fetchall()
    discresults = {}
    ll = []
    y_set = []
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
        # print(row)
        #비율
        x = row[0] #도시이름
        y = row[4] #확진환자 합계 
        z = row[1] #확진확자 증감
        confirmed_patient = row[4]
        label = [row[0]]
        
        plt.barh(label, confirmed_patient)
        # for i, v in enumerate(ll):
        plt.text(row[4], row[0], row[4],                 # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
            fontsize = 9, 
            color='blue',
            horizontalalignment='left',  # horizontalalignment (left, center, right)
            verticalalignment='center')    # verticalalignment (top, center, bottom)


        
except:
    print('ERROR!!')

index = np.arange(len(ll))

# plt.xticks(index, ll, fontsize=5)
plt.title('Status of COVID-19 by city and province', fontsize=15)
plt.xlabel('City', fontsize=8)
plt.ylabel('Confirmed Patient', fontsize=8)
# plt.xticks(index, label, fontsize=15)
# print(type(x),type(y))
plt.savefig("city_corona.png")
plt.show()
# plt.show()