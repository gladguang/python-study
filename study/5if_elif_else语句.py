a = input("请输入一个数：")                            #  提示屏幕输入一个数字
a = float(a)                                          #  将输入的字符型数字转换为浮点型
if a > 0:                                             #  当 a>0 时候条件执行冒号后面缩进语句
    print("a是正数。且a=%.2f" %a)
elif a == 0:                                          #  当 a=0 时候条件执行冒号后面缩进语句               
    print('a等于0')
else:                                                 #  当 a不满足上面if与elif条件时 ，执行冒号后面缩进语句
    b = abs(a)
    print("a是负数，a的绝对值为%.2f,且a=%.2f"%(b,a))