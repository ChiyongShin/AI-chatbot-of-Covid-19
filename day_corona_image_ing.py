import os
import pandas as pd 
import numpy as np 
import seaborn as sns
import pymysql
import plotly
import plotly.express as px
import matplotlib.pylab as plt
from sqlalchemy import create_engine


conn = pymysql.Connect(host="localhost", user="root", password="wlsdud369", db="db")
curs = conn.cursor()
Confirmed_set = []
sql = "select * from day_corona_db"
try:
    curs.execute(sql)
    results = curs.fetchall()
    discresults = {}
    for row in results:
        Date = row[0]
        Confirmed = row[1]
        # Confirmed_set.append(Confirmed)
        Cure = row[2]
        print(row)
        x = row[0]
        y = row[1]
        z = row[2]
        plt.plot(x,y,'or',label='Confirmed')
        plt.plot(x,z,'ob',label='Cure')
        plt.title("day_corona")
        plt.xlabel("Date")
        plt.ylabel("Number")
        plt.savefig("day_corona.png")
        
except:
    print('ERROR!!')

#큰일났다 여러번 반복된다
plt.legend(loc = 'right') 
plt.show()




# y = np.arange(Confirmed_set[0],Confirmed_set[6])
# for row in results:
#     x = row[0]
#     y = row[1]
#     plt.plot(x,y,'or')
# plt.show()






# df1 = pd.read_sql_table('day_corona_db',conn )
# plt.style.use('ggplot')
# df1.plot(title='확진자',figsize = (16,10))

# plt.figure()
# plt.plot(Date,Confirmed)
# plt.grid('white')
# plt.xlabel('날짜')
# plt.ylabel('확진자')
# plt.title('코로나19 일별 확진 환자 발생 및 완치 현황')
# plt.xticks(Date)
# plt.plot([5]*21,Confirmed, 'r')
# plt.show()