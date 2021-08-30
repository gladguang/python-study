
import math

def my_quadratic(a, b, c):

    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):

        raise TypeError('bad operand type')

    d = b**2 - 4*a*c                                       # 数字和字母相乘需要‘ * ’，和数学还是有差别的

    if a == 0:                                                 # ‘ == ’在Python中是等于而‘ = ’是赋值，已踩坑

        print('该方程没有意义')

    elif d < 0:                                               # 小于零后是负数式子就不成立，所以无解

        print('该方程无解')

    elif d == 0:

        x = -b/(2*a)                                      # 

        print(f'该方程的两个解为：x1=x2={x:.1f}')

    else:

        x1 = (-b+math.sqrt(d))/(2*a)

        x2 = (-b-math.sqrt(d))/(2*a)

        print(f'该方程的两个解为：x1={x1:.1f} x2={x2:.1f}')
       


