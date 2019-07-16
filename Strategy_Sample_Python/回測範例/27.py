# -*- coding: UTF-8 -*-

#載入相關套件及函數
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

#取得成交資訊
I020 = [ line.strip('\n').split(",") for line in open('/Volumes/DataStore/python_future_trading/TickData/Futures_20170815_I020.csv')][1:]
#取得轉換時間字串至時間格式
Time = [ datetime.datetime.strptime(line[0],"%H%M%S%f") for line in I020 ]
#將datetime時間格式轉換為繪圖專用的時間格式，透過mdates.date2num函數
Time1 = [ mdates.date2num(line) for line in Time ]
#價格由字串轉數值
Price = [ int(line[4]) for line in I020 ]

#定義圖表物件
ax = plt.figure(1) 		#第一張圖片              
ax = plt.subplot(111)	#該張圖片僅一個圖案
#以上兩行，可簡寫如下一行
#fig,ax = plt.subplots()

#定義title
plt.title('Price Line')
plt.xlabel('Time')
plt.ylabel('Price')

#繪製圖案
#plot_date(X軸物件, Y軸物件, 線風格)
ax.plot_date(Time1, Price, 'k-')

#定義x軸
hfmt = mdates.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_formatter(hfmt)

#顯示繪製圖表
plt.show()