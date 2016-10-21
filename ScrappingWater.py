# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 00:31:26 2016

@author: escriva
"""

import pandas as pd
import datetime as dt


def get_CDEC_data(station_id='mil', sensor_num='15', start_date='1900-01-01', \
    end_date=dt.datetime.today().strftime("%Y-%m-%d"), data_wish='View+Daily+CSV+Data'):

    url = 'http://cdec.water.ca.gov/cgi-progs/getDailyCSV?'+'station_id='+\
    station_id+'&sensor_num='+sensor_num+'&start_date='+start_date+'&end_date='+end_date+'&data_wish='+data_wish

    CDECdata = pd.read_csv(url, header=3, skipfooter=1, engine='python', encoding='utf-8')
    
    return CDECdata



"Change"

"More changes"