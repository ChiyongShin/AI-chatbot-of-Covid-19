import os
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import pymysql
import folium
from folium import plugins
from folium.plugins import HeatMap
print(folium.__version__)

conn = pymysql.Connect(host="localhost", user="root", password="wlsdud369", db="db")
curs = conn.cursor()

sql = "select * from city_corona_db"
try:
    curs.execute(sql)
    results = curs.fetchall()
    discresults = {}
    for row in results:
        City_name = row[0]
        Total = row[1]
        Domestic_Occurrence = row[2]
        Foreign_Inflow = row[3]
        Confirmed_Ratient = row[4]
        Quarantine = row[5]
        Isolation_Release = row[6]
        Dead = row[7]
        Incident_rate = row[8]

except:
    print('ERROR!!')


# m = folium.Map(location=[48, -102], zoom_start = 3)


conn.close()

m 