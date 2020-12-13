import os
import pandas as pd
import numpy as np
import seaborn as sns
import pymysql

import matplotlib.pylab as plt
import matplotlib.pyplot as plt


plt.rcParams['figure.figsize'] = [17, 6]

conn = pymysql.Connect(host="localhost", user="root", password="1234", db="db")
curs = conn.cursor()
label = []
data = []
sql1 = "select * from city_daily_db WHERE City_Code = 1"
sql2 = "select * from city_corona_db WHERE City_Code = 1"
curs.execute(sql1)
result1 = curs.fetchall()
for row1 in result1:
    a = row1[1]
    b = row1[2]

curs.execute(sql2)
result2 = curs.fetchall()
for row2 in result2:
    d = row2[1]
    e = row2[2]
    f = row2[3]
    g = row2[4]

label = ['Daily Change Total', 'Daily Change Local', 'Confirmed_Patient', 'Quarantine',
         'Isolation_Release', 'Dead']
print(label)
data = [a, b, d, e, f, g]


plt.barh(label, data)

plt.title('Domestic Status of COVID-19 by city and province', fontsize=15)
plt.xlabel('City', fontsize=3)
plt.ylabel('Confirmed Patient', fontsize=3)
#
plt.savefig("domestic_corona.png")
plt.show()
