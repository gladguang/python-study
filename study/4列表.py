#   list()   range()

t = []                     #  空集赋值与t              
t = list(range(11))        #  将0到10数 ( 元素赋值与t)   1、list()输出为列表  2、range(x,n)取x到n-的范围
print(t)                   #  打印集合0到10
print(max(t))              #  打印列表t中最大数
print(min(t))              #  打印列表t中最小数
print(sum(t))              #  计算集合数之和

b = 0
for a in t:                 #  for x in list:   在列表list中每次循环取一个数放到x
    b = b + a
print(b)                    #  计算集合数之和
print('\n')




t = [t for t in range(1,21)]
print(t)

t = list(range(1,21))
print(t)



