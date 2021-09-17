# -*- coding: utf-8 -*-

"""
#定义一个空列表
info = {}
#  定义变量id 
id = input('请输入用户名:')
>>> 请输入用户名:tom
#  让用户名首字母大写
id = id.title()
#  将id和密码放入字典 info
info[id] = input('请输入密码:')
>>> 请输入密码:123

#  打印字典info
print(info)
>>> {'Tom': '123'} 

#  修改id密码
info[id] = input('请输入新的密码：')
>>> 请输入新的密码：456
#  打印修改后字典信息
print(info)
>>> {'Tom': '456'}

# del  键-值删除   id和密码注销
del info[id]
# 打印测试是否删除
print(info)
>>> {}
"""

#*****************  批量注册  *****************
#  初始化登录数据
info = {}
#  循环1000次
for x in range(1,1001):
    #  输入用户名信息
    id = input('请输入用户名:')
    # 将用户名和密码相匹配输入字典
    info[id] = input('请输入密码：')
    # 询问是否继续注册
    act = input('是否继续批量注册(yes/no):')
    if act == 'no':
        break
# 打印字典存储的注册信息
print(info)
print(len(info))



