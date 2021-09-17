import requests
import time
import os

url = r'https://pc.ftftx.com/pair/market/kline?pairId=2548&type=12'
resp = requests.get(url)
resp = resp.json()

for date in resp["data"]:
    sj = date[0]
    sj = str(sj)
    sj = sj[:-3]
    sj = int(sj)
    time_local = time.localtime(sj)
    #转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    begin_price = str(date[1])
    last_price = str(date[4])
    high_price = str(date[2])
    low_price = str(date[3])
    print(dt,begin_price,last_price,high_price,low_price)
