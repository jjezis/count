import pandas as pd 
import matplotlib.pyplot as plt 

stonks=pd.read_csv("C:\\Users\\DistantEngouh\\OneDrive\\Desktop\\code\\data\\Google Stock Market Data - google_stock_data.csv")
#clean up data
nanstonks=stonks[stonks.isna().any(axis=1)]
nanstonks=stonks.dropna(how='all')
#puttig nw stuff
months=range(1,2519)
resluts=stonks.groupby('Date').sum()
stonks['Months']=stonks['Date'].str[0:2].str.replace('/',' ')
#plt stuff
plt.bar(months,resluts['Open'],color='pink')

stonks['Sales']=stonks['High']-stonks['Low']

def day(Date):
    return Date.split('/')[1]
stonks['Day']=stonks['Date'].apply(lambda x: day(x))

#execution

plt.show()
print(stonks.head(161))