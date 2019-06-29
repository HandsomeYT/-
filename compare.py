import pandas as pd
from datetime import datetime
from pylab import *
import matplotlib.dates as mdates
import dateutil, pylab, random
from pylab import *
 
 
import matplotlib.pyplot as plt
 
data=pd.DataFrame(pd.read_excel('sentiment.xlsx'))
data2=pd.DataFrame(pd.read_excel('price.xlsx'))
data2=data2.fillna(method='pad')
data2.columns=['date','price']
data2['date']=pd.to_datetime(data2['date'])
data.columns=['date','positive','confidence','sentiments']
newdata=data.groupby('date').agg(lambda x:list(x))## 相同日期的聚一起
 
times=[]
sentiment=[0.5,0.5,0.5,0.5,0.5,0.5]
for i in range(1,newdata.shape[0]):
    p=newdata.positive[i]
    d=newdata.index[i]
    sum=0
    for z in p:
        sum+=z
    average=sum/len(p)
    #print(type(d))
    print(datetime.datetime.strptime(d,"%Y-%m-%d").weekday())
    if(datetime.datetime.strptime(d,"%Y-%m-%d").weekday()!=6 and datetime.datetime.strptime(d,"%Y-%m-%d").weekday()!=5):
        sentiment.append(average)
        times.append(d)
times = pd.to_datetime(times)
print(len(sentiment))
print(len(times))
print(len(data2.price))
x=data2.date
y1=sentiment
y2=data2.price
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(x, y1)
ax1.set_ylabel('sitiment')
ax1.set_title("Sentiment")
ax1.legend(loc='upper right')
 
ax2 = ax1.twinx()#设置双y轴
ax2.plot(x, y2, 'r')
ax2.set_ylabel('stock price')
ax2.set_xlabel('date')
ax2.legend(loc='upper left')
plt.show()
#print(times)
'''
pylab.plot_date(pylab.date2num(times), sentiment, linestyle='-')
pylab.plot_date(pylab.date2num(data2.date),data2.price, linestyle='-')
xtext = xlabel('time')
ytext = ylabel('sentiments')
ttext = title('sentiments')
grid(True)
setp(ttext, size='large', color='r')
 
 
show()
'''