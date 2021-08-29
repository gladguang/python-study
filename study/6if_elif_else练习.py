#***********************   练习   ***********************************************************************

#  if 条件判断 石头剪刀布 random模块

#  导入随机模块
import random      

#  开始前，屏幕先提示  1代表石头，2代表剪刀，3代表布
print("请输入石头、剪刀、布(1代表石头，2代表剪刀，3代表布）")
#  input输入的是字符串型，需转换成整型
player = int(input("我要出："))
#  电脑变量 随机获取大于等于1，小于等于3的整数    random.randint(n,x)
computer = random.randint(1,3)

#  三种条件  要么输 要么平 要么赢。
if player == computer:
    print("和我出的一样。我出的是：%d,电脑出的是:%d" %(player,computer))
elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print("恭喜你，你赢了。我出的是：%d,电脑出的是:%d" %(player,computer))
else:
    print("你输了！不要灰心，下次赢回来。我出的是：%d,电脑出的是:%d" %(player,computer))
