#  break:跳出整个循环，不会再执行循环后续的内容

#  continue:跳出本次循环，continue后面的代码不再执行，但是还是会继续循环

#  exit()：结束程序的运行



#    for in 循环与  break使用
for i in range(3):
    user = input('请输入用户名：')
    passwd = input('请输入密码：')    
    if user=='gladguang' and passwd == 'admin':        
        print('%s用户登录成功' %user)        
        break    
    else:        
        print('密码错误，请重新输入密码,您还剩%d次机会' %(2-i))
else:
    print('超过三次，登录失败')


#   while循环 和 break使用
trycount = 0

while trycount < 3:
    name = input('用户名:')
    passwd = input('密码:')
    if name == 'gladguang' and passwd == 'admin':
        print('登录成功')
        break
    else:
        print('登录失败')
        print('您还剩余%d次机会' %(2 - trycount))
        trycount += 1
else:
    print('登录次数超过三次，请稍后登录')
