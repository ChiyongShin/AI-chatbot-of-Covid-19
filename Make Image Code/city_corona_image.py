import os
import pandas as pd
import numpy as np

import pymysql

import matplotlib.pylab as plt
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [10, 6]

conn = pymysql.Connect(host="localhost", user="root", password="1234", db="db")
curs = conn.cursor()
Confirmed_set = []
sql = "select * from city_corona_db WHERE City_Name != 'total'"
try:
    curs.execute(sql)
    results = curs.fetchall()
    y_set = []
    for row in results:
        x = row[0]  # 도시이름
        y = row[1]  # 확진환자 합계
        confirmed_patient = row[1]
        label = [row[0]]
        plt.barh(label, confirmed_patient)
        plt.text(row[1], row[0], row[1],  # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
                 fontsize=9,
                 color='blue',
                 horizontalalignment='left',  # horizontalalignment (left, center, right)
                 verticalalignment='center')  # verticalalignment (top, center, bottom)



except:
    print('ERROR!!')

plt.title('Domestic Status of COVID-19 by city and province', fontsize=15)
plt.xlabel('Confirmed Patient', fontsize=8)
plt.ylabel('City', fontsize=8)

plt.savefig("city_corona.png")
plt.show()
