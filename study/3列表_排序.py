#*************************************    组织列表    ************************************

#  .sort() 正向排序   .sort(revers=True)反向排序   sort用于永久性排序 直接作用于内存。是永久性的，无法恢复原来内存

names = ['ZI','AL','AB','a','z','k']

names.sort()        #  列表names 排序

print(names)        #  打印输出排序后的列表

names.sort(reverse=True)   # 列表names反向排序 .sort(revers=True)

print(names)               # 打印输出排序后的列表

print('\n')


#  sorted(变量列表)  用于临时排序，不作用内存原始数据。

grapheme = ['ZI','AL','AB','a','z','k']                    #  原始列表

print('Original list is %s.' % grapheme)            #  打印列表

t = sorted(grapheme)                                #  将临时排序后的列表赋值与变量t

print('New list is %s' % t)                         #  打印排序后的列表

print('Unchanged list is %s.' % grapheme)           #  查看原始列表未改变

s = sorted(grapheme,reverse=True)                   #  将临时反向排序后的列表赋值与变量s

print(s)                                            #  打印临时反向排序后的列表
print('\n')



#    .reverse()  反转列表排序。1、在列表序号为0的元素和列表序号为n的元素调位子。 2、 直接作用于内存，如需恢复则再用.reverse()一次

p = ['ZI','AL','AB','a','z','k']

p.reverse()         #  反转列表排序

print(p)            #  打印反转列表

p.reverse()         #  再次反转列表。  两次反转列表等于恢复原样

print(p)            #  打印再次后的反转列表
print('\n')


# len()   确定列表长度、字符串字符数

p = ['ZI','AL','AB','a','z','k']

print(len(p))

x = 'ZIALAcBazk'   #  打印列表长度

print(len(x))      #  打印字符串字符数
