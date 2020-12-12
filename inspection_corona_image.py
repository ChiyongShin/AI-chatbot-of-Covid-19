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


conn = pymysql.Connect(host="localhost", user="root", password="wlsdud369", db="db")
curs = conn.cursor()
Confirmed_set = []
sql = "select * from inspection_corona_db"
try:
    curs.execute(sql)
    results = curs.fetchall()
    discresults = {}
    for row in results:
        Cumulative_Inspection_Count = row[0] #누적검사수
        Cumulative_Complete_Inspection = row[1] #누적검사완료수
        Cumulative_Confirmed_Rate = row[2] #누적확진율
        Testing_Count = row[3] #검사중
        Testing_Count_Rate = row[4] #검사중 비율
        Result_Positive = row[5] #결과양성
        Result_Positive_Rate = row[6] #결과양성비율
        Result_Negative = row[7] #결과음성
        Result_Negative_Rate = row[8] #결과음성비율
        print(row)
        #비율
        x = row[4]
        y = row[6]
        z = row[8]
        ratio = [x,y,z]
        print(ratio)

       
        
except:
    print('ERROR!!')


# plt.legend(loc = 'right') 
labels = ['Testing','Positive','Negative']
# explode = [0.02, 0.02, 0.02]
colors = ['#ffc000', '#d395d0', 'skyblue']
wedgeprops={'width': 0.6, 'edgecolor': 'w', 'linewidth': 0.5}
plt.pie(ratio, labels=labels, autopct='%.1f%%', counterclock=False, colors=colors, wedgeprops=wedgeprops)
plt.title('Inspection COVID-19')
plt.savefig("inspection_corona.png")
plt.show()
