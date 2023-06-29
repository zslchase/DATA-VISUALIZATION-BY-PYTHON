import csv
import matplotlib.pyplot as plt
from datetime import datetime
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
filename='D:\python\data  visualization\data\sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header=next(reader)
    print(header)
    highs=[]
    lows=[]
    dates=[]
    for row in reader:
        current_date=datetime.strptime(row[2],'%Y-%m-%d')
        high=int(row[5])
        low=int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)


    fig,ax=plt.subplots()
    ax.plot(dates,highs,c='red')
    ax.plot(dates,lows,c='blue')
    ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
    ax.set_title('2018年7月每日最高温度')
    ax.set_xlabel('日期')
    fig.autofmt_xdate()
    ax.set_ylabel('温度')
    plt.show()
