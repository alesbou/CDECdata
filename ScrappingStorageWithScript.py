# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:27:24 2016

@author: escriva
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 18:14:48 2016

@author: escriva
"""

"""
SELECTED CDEC SENSOR NUMBERS (these are not be available for all sites):
    1    river stage [ft]
    2    precipitation, accumulated [in]
    3    SWE [in]
    4    air temperature [F]
    5    EC [ms/cm]
    6    reservoir elevation [ft]
    7    reservoir scheduled release [cfs]
    8    full natural flow [cfs]
    15   reservoir storage [af]
    20   flow -- river discharge [cfs]
    22   reservoir storage change [af]
    23   reservoir outflow [cfs]
    24   Evapotranspiration [in]
    25   water temperature [F]
    27   water turbidity [ntu]
    28   chlorophyll [ug/l]
    41   flow -- mean daily [cfs]
    45   precipitation, incremental [in]
    46   runoff volume [af]
    61   water dissolved oxygen [mg/l]
    62   water pH value [pH]
    64   pan evaporation (incremental) [in]
    65   full natural flow [af]
    66   flow -- monthly volume [af]
    67   accretions (estimated) [af]
    71   spillway discharge [cfs]
    74   lake evaporation (computed) [cfs]
    76   reservoir inflow [cfs]
    85   control regulating discharge [cfs]
    94   top conservation storage (reservoir) [af]
    100  water EC [us/cm]
    CDEC DURATION CODES:
    E    event
    H    hourly
    D    daily
    M    monthly
"""
import ScrappingWater as sw
import pandas as pd

list = ['ISB', 'SCC', 'TRM', 'PNF', 'MIL', 'BUC', 'MAR', 'BAR', 'EXC', 'DNP', 'NML', 'NHG', 'CMN']

results=[]

for reservoir in list:
    df = sw.get_CDEC_data(station_id=reservoir)
    dfsum = df[['01']]
    dfsum = dfsum.convert_objects(convert_numeric=True)
    df['Storage'] = dfsum.mean(axis=1)
    df['Year']=df.iloc[:,2]
    df['Month']=df.iloc[:,3]
    df['Date']=pd.to_datetime(df.Year*10000+df.Month*100+1,format='%Y%m%d')    
    df['Reservoir']=df.iloc[:,0]
    del dfsum
    dfshort = df[['Date','Storage', 'Reservoir']]
    results.append(dfshort)
    del df
    
for i in range(13):
    results[i].to_csv("ReservoirStorage"+list[i]+".csv")
    results[i] = results[i].rename(columns={'Storage':'Stor'+list[i], 'Reservoir' : 'Reservoir'+list[i]})
"""    
a = results[0].merge(results[1],on='Date').merge(results[2],on='Date').merge(results[3],on='Date').merge(results[4],on='Date').merge(results[5],on='Date').merge(results[6],on='Date').merge(results[7],on='Date').merge(results[8],on='Date')
a.to_csv("ReservoirResultsMerged.csv")
"""