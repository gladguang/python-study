#  计算1加到100之和

sum = 0                        #  先初始化变量sum
for a in range(1,101):          #  range(1,101)取大于等于1小于101的整数 ，即循环取1到10整数
    sum += a                   #  sum += a    等价于 sum = sum + a 
print(sum)                     #  打印和

'''
range(stop): 0~stop-1
range(start,stop): start~stop-1
range(start,stop,step): start~stop step(步长)
'''

#  求1到100之间偶数之和

sum = 0                        #  先初始化变量sum
for a in range(2,101,2):       #  range(2,101，2)取从2开始加2一直到100的和
    sum += a                   #  sum += a    等价于 sum = sum + a 
print(sum)                     #  打印和

#  求1到100之间奇数之和

sum = 0                        #  先初始化变量sum
for a in range(1,101,2):       #  range(1,101，2)取从1开始加2一直到99的和
    sum += a                   #  sum += a    等价于 sum = sum + a 
print(sum)                     #  打印和



#  有1，2，3，4四个数字,求这四个数字能生成多少个互不相同且无重复数字的三位数
i = 0
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
                if (x!=y) and (y!=z) and (z!=x):
                    i += 1
                    if i%4:
                        print("%d%d%d" % (x, y, z), end=" | ")
                    else:
                        print("%d%d%d" % (x, y, z))

#  打印9*9乘法表
for i in range(1,10):
    for j in range(1,i+1):
            print('%d * %d = %d\t' %(i,j,i*j),end='')
    print()

