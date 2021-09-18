
# -*- coding:UTF-8 -*-
import requests
import time
import os

url = r'https://pc.ftftx.com/pair/market/kline?pairId=2548&type=12'
resp = requests.get(url)
resp = resp.json()


for date in resp["data"]:
    sj = str(date[0])
    sj = int((sj[:-3]))
    time_local = time.localtime(sj)
    #转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    begin_price = str(date[1])
    last_price = str(date[4])
    high_price = str(date[2])
    low_price = str(date[3])
    
    # 数据写入文件
    with open('比特币价格.csv','a',encoding='utf-8') as f:
        f.write('日期:%s,开始价格:%s,收盘价格:%s,最高价格:%s,最低价格:%s,单位美元' %(dt,begin_price,last_price,high_price,low_price))
        f.write('\n')
    with open('比特币价格.txt','a',encoding='gbk') as f:
        f.write('日期:%s,开始价格:%s,收盘价格:%s,最高价格:%s,最低价格:%s,单位美元' %(dt,begin_price,last_price,high_price,low_price))
        f.write('\n')
        
print('获取成功\n')
input('按任意键关闭：')