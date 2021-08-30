#  猜大小
#  导入random模块
import random
#  猜1到10之间的数 包含1和10
num = random.randint(1,10)
i = 1
print('猜大小！猜1到10之间的数，包含1和10。\n你一共有3次机会')
shuru = input("想要来一局吗？yes/no：\n")

while shuru == 'no':
    break

if shuru == 'yes':
    while i <= 3:
        ans = int(input("请猜数："))
        if ans > num:
            print("大了，还剩%d次机会"%(3-i))
        elif ans < num:
            print("小了,还剩%d次机会"%(3-i))
        else:
            print("恭喜您猜对了！！！\t答案就是%d"%num)
            break
        i += 1
