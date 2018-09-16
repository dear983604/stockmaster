#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 19:28:36 2018

@author: cheating
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import json
#import Imgur
import datetime

###############################################################################
#                              股票機器人 標準差分析                            #
###############################################################################
today = datetime.date.today()


# 股票搜尋
def searchstock(stocknumber):
    url = 'http://invest.wessiorfinance.com/Stock_api/Notation_cal?Stock=' + stocknumber + '.TW&Odate=' + str(today) + '&Period=3.5&is_log=0&is_adjclose=0'
    list_req = requests.get(url)
    soup = BeautifulSoup(list_req.content, "html.parser")
    getjson=json.loads(soup.text)
    if len(getjson)>10:
        url = 'http://invest.wessiorfinance.com/Stock_api/Notation_cal?Stock=' + stocknumber + '&Odate=' + str(today) + '&Period=3.5&is_log=0&is_adjclose=0'
        list_req = requests.get(url)
        soup = BeautifulSoup(list_req.content, "html.parser")
    getjson=json.loads(soup.text)
    if len(getjson)>10:
        time = getjson[str(len(getjson))]['theDate_O']
        print('時間 = ' + time)

        theClose = getjson[str(len(getjson))]['theClose']
        print('收盤價 = ' + str(theClose))

        TL = getjson[str(len(getjson))]['TL']
        print('TL = ' + str(TL))

        STD = getjson[str(len(getjson))]['STD']
        print('STD = ' + str(STD))
    
        low="很貴不要買"
        if (TL - STD*2) >= theClose:
            low ="非常便宜趕快買"
        elif (TL - STD) >= theClose:
            low ="蠻便宜了"
    
        return('收盤價 = ' + str(theClose) + '\n中間價 = ' + str(TL) + '\n線距 = ' + str(STD) + '\n' + low)
    else:
        return('沒有這個股票')

    