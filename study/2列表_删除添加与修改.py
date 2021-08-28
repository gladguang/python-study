names = [' wen ','zhang','li','liu','wu','zhao','qian','sun','zhou','wu','zheng','wang']
#     列表 list 用[]表示
print(len(names))       # len() 用于计算字符串字符数、列表里个数

print(names)            # 打印列表内部表示包括方括号

print(names[0])         # 打印列表里第一个元素   列表序标从0开始

print(names[0].title().lstrip().strip())  # 打印列表里第一个元素 且 首字母大写 且 去除首尾空白符，但内存里首尾空白符未改变

first_name = names[0].title().lstrip().strip()      #  将列表里第一个元素 首字母大写且去除首尾空白符 赋值于first_name              

#print(first_name)                                  #  打印观察 列表元素是否去除空白               

message = 'My first name is ' + first_name + '!'    # 字符串 加法 拼接

print(message)                                      # 打印观察是否拼接成功

print(('Hello,Mr %s.'+ message) % (first_name))     # 输出




#****************************************    修改、添加、删除元素    ****************************************

names = [' wen ','zhang','li','liu','wu','zhao','qian','sun','zhou','wu','zheng','wang']

#  修改元素

names[0] = 'xiao'   #  修改列表首位元素

print(names)        #  打印测试是否修改

#  添加元素 插入元素  .append()  .insert()

names.append('guang')    #  在列表末尾添加元素'guang'

print(names)             #  打印测试是否添加

names.insert(-2,'wen')   #  在倒数第二位元素前 添加元素'wen'

print(names)             #  打印测试是否添加

#  删除元素        用法： 1、del 列表变量名[序标] 2、列表.pop()   ****** .pop()删除最后一个元素   .pop(序标)  删除序标元素

del names[-2]                             #  删除倒数第二个元素     

print(names)                              #  打印测试是否删除

last_pop_list = names.pop()             #  1、删除names列表最后一个元素   2、将names列表删除的元素赋值与last_pop_list

print(names)                              #  打印测试是否删除

print(last_pop_list)                    #  打印删除的元素

print('I delete last element is ' + last_pop_list.title() + '.' )  #  打印输出 删除最后一个的元素首字母大写



#  .pop()  .remove()  

first_pop_list = names.pop(0)                                      # 1、删除names列表第一个元素   2、将names列表删除的元素赋值与first_pop_list

print (names)                                                      #  打印测试是否删除

print(first_pop_list)                                              #  打印删除的元素

print('I delete first element is ' + first_pop_list.upper() + '.' )  #  打印输出 删除的元素首字母全部大写




names.remove('wen')      #  .remove(删除的元素)  remove用于已知的元素删除，pop用于删除列表序号所在的元素   ***remove只能删除列表出现多次的第一个。要想全部删除需要用循环语句

print(names)             #  打印测试是否删除 












