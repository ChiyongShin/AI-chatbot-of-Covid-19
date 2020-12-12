import os
import pandas as pd 
from pandas import Series, DataFrame
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
Country_set = []
count = 0
sql = "select * from global_corona_db WHERE Country != 'Others'"
try:
    curs.execute(sql)
    results = curs.fetchall()
    discresults = {}
    for row in results:
        Country = row[0]
        Confirmed = row[1]
        # print(row)
        x = row[0]
        y = row[1]

        if Confirmed > 1000000:
            count += 1
            Country_set.append(Country)
            Confirmed_set.append(Confirmed)

except:
    print('ERROR!!')


# for i in results:
#     rowlist[i] = row[1]
# print(rowlist)
labels = [Country_set[i] for i in range(0,count-1)]
ratio = [Confirmed_set[i] for i in range(0,count-1)]
# plt.legend(loc = 'right') 
# print(Confirmed_set)
# explode = [0.02, 0.02, 0.02]
wedgeprops={'width': 0.6, 'edgecolor': 'w', 'linewidth': 0.5}

# plt.pie(ratio, labels=labels, autopct='%.1f%%', counterclock=False, colors=colors, wedgeprops=wedgeprops)

plt.pie(ratio,labels=labels, autopct='%.1f%%')
plt.title('Global Status of COVID-19')
plt.savefig("global_corona.png")
plt.show()

