import os
import pandas as pd
import numpy as np
import seaborn as sns
import pymysql
import matplotlib.pylab as plt


conn = pymysql.Connect(host="localhost", user="root", password="1234", db="db")
curs = conn.cursor()
Confirmed_set = []
sql = "select * from day_corona_db"
try:
    curs.execute(sql)
    results = curs.fetchall()
    discresults = {}
    for row in results:
        NumberOrder = row[0]
        Date = row[1]
        Confirmed = row[2]
        # Confirmed_set.append(Confirmed)
        Cure = row[3]
        x = row[1]
        y = row[2]
        z = row[3]
        plt.plot(x, y, 'or', label='Confirmed')
        plt.plot(x, z, 'ob', label='Cure')
        plt.title("Day COVID-19 Confirmed Patients & Recovered Patients")
        plt.xlabel("Date")
        plt.ylabel("Number")
        plt.savefig("day_corona.png")

except:
    print('ERROR!!')

# 큰일났다 여러번 반복된다
plt.legend(loc='right')
plt.show()



