
import math
import pandas as pd
import json 
import numpy as np
import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt


# In[2]:


def wgs_to_msk(lat, lon, l0, dx, dy):
    H=-20
    #Координаты точки WGS с GARMIN
    B=lat*math.pi/180
    L=lon*math.pi/180
    #данные из таблицы для МСК
    #КОНСТАНТЫ ДЛЯ ПЕРЕСЧЁТА
    po=(180/math.pi)*3600
    const=180/math.pi
    #параметры эллипсоида Крассовского
    a1=6378245
    al1=298.3
    b1=a1-(a1/al1)
    e1=math.sqrt(((a1*a1-b1*b1)/(a1*a1)))
    e12=e1*e1
    #параметры эллипсоида WGS 84
    a2=6378137
    al2=298.257223563
    b2=a2-(a2/al2)
    e2=math.sqrt(((a2*a2-b2*b2)/(a2*a2)))
    e22=e2*e2
    #Параметры трансформации по ГОСТ 32453-2017
    dx1=-23.57
    dy1=140.95
    dz1=79.80
    wx=0
    wy=0.35
    wz=0.79
    dm=0.22/(10**6)
    #Постоянные для перехода из WGS в СК42
    da=a1-a2
    de2=e12-e22
    a=(a1+a2)/2
    e=(e12+e22)/2
    #Поправочные коэффициенты
    G0=#расчёт
    G1=#расчёт
    G2=#расчёт
    G3=#расчёт
    #Расчётные параметры для каждой точки
    N=a/math.sqrt(1-e*(math.sin(B))**2)
    M=#расчёт
    dB=#расчёт согласно ГОСТ
    dL=#расчёт согласно ГОСТ
    #Полученные координаты точки из вычислений
    L1=lon+dL/3600
    B1=lat+dB/3600
    B2=B1*math.pi/180
    L1=(L1-l0)*3600
    #Расчетные параметры, переменные
    X1=#доп переменная для X
    n2=#доп переменная для Y
    N1=#доп переменная для Y
    #КООРДИНАТЫ ТОЧЕК В МСК
    x=#итоговое значение x в МСК
    y=#итоговое значение y в МСК
    return(x, y)
    
    


# In[3]:


wgs_to_msk(46.29640865, 48.01588512, 49.05, -4714743.504, 2300000)


# In[4]:


df_gost = pd.read_excel(open('msk_to_wgs_gost51794.xlsx', 'rb'), sheet_name='msk_to_wgs_gost51794')


# In[5]:


df = pd.read_excel(open('msk_to_wgs.xlsx', 'rb'), sheet_name='msk_to_wgs')


# In[6]:


df


# In[7]:


def get_parameters(df, zone):
    df_zone = df[df['zone']==zone].reset_index(drop=True)
    return(df.l0[0], df.dy[0], df.dx[0])


# In[8]:


df[df['zone'] == 'МСК.6градусная']


# In[9]:


df['zone'][0]


# In[10]:


df[df['zone']=='МСК-01']


# In[11]:


get_parameters(df, 'МСК-01 зона 2')


# In[12]:


lat = 46.29640865
lon = 48.01588512
zone = 'МСК-01 зона 2'
l0, dx, dy = get_parameters(df, zone)


# In[13]:


with open('change.json', 'r', encoding="utf8") as f:
    data = json.load(f)
    df_date = pd.json_normalize(data['republic'])
for republic in df_date['district_name']:
    # Retrieve the boundary polygon
    boundary_gdf = ox.geocode_to_gdf(republic)
    # Save to a GeoJSON
    boundary_gdf.to_file(f"{republic}.geojson", driver='GeoJSON')


# In[15]:


# Load GeoJSON data
gdf = gpd.read_file('Republic.geojson')

# Plot the GeoDataFrame
gdf.plot()

# Show the plot
plt.show()
# In[ ]:

# In[ ]:




