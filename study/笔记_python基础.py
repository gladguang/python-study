#!/usr/bin/env pyhon3
# -*- coding: utf-8 -*-
'''
name = input("Please input you name:")  #input 从屏幕输入变量
print("you name is",name)
'''

'''
a = 100
if a >= 0:
    print(a)
else:
    print(-a)
    '''

'''
print('I\'m \"OK\"!')   #反斜杠 \ 表示转义。
print("I'm \"OK\"!")
'''

'''
a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)
'''
'''
b= 7//3   #地板除，取除尽整数部分
print(b)
'''

"""n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n,"\n",f,"\n",s1,"\n",s2,"\n",s3,"\n",s4)
"""

# 练习
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：

'''
past_grade = 72
now_grade = 85
percentage = (now_grade - past_grade)/past_grade*100

print('%s成绩提升了:%.1f%%' % ('小明',percentage)) 

print('{0}成绩提升了:{1:.1f}%'.format('小明',percentage))   # format用法 {0} {1} .format(变量0，变量1)

print(f'小明成绩提升了:{percentage:.1f}%')  以f开头的字符串，字符串如果包含{xxx}，就会以对应的变量替换
'''

#  廖雪峰py进度   https://www.liaoxuefeng.com/wiki/1016959663602400/1017092876846880        2021.08.23

#  变量 list 和 元组 tuple
'''
classmates = ["wen","liu","wang"]  #  list (列表)                       变量 = [变量0，变量1，变量2，...] 变量类型可以不同

classmates[0]                      #  取第一个变量 "wen" 
classmates[-1]                     #  取最后一个变量 "wang"

classmates.append("zhao")          #  在列表最后 添加变量 "zhao"          变量.append = [变量n,变量n+1,变量n+2,...]
classmates.insert(1, "xue")        #  在列表索引 [1] 的位置插入 "xue"     变量.insert = [索引序号,插入的变量]

classmates.pop()                   #  在列表删除最后一个索引              变量.pop()
classmates.pop(1)                  #  删除列表索引 [1] 的位置数据         变量 .pop(索引序号)

classmates[1] = "li"               #  把索引位置 [1] 的变量替换为 "li"    变量[序号索引] = 变量


classmates = ("wen","liu","wang")  #  元组tuple一旦初始化就不能修改      变量 = (变量0，变量1，变量2，...)
#  1、现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。
#  2、其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
#  3、因为tuple不可变，所以代码更安全

# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
'''

#条件判断

'''
age = int(input('Please input int:'))              #  input输入的为字符串类型，小括号括起来用int强制转换为整数型
if age >= 18:                                      #  条件判断是否大于18岁
    print('your age is', age)         
    print('adult')                                 #  成立则打印
else:
    print('You are juveniles.\nYou age is', age)   #  不成立打印

'''

'''
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
 '''   

# 练习
#  小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

#  低于18.5：过轻
#  18.5-25：正常
#  25-28：过重
#  28-32：肥胖
#  高于32：严重肥胖
#     身高 height 体重 weight BMI指数 BMI_index_number
'''
height = float(input('请输入你的身高。单位是m，保留两位小数:'))
weight = float(input('请输入您的体重。单位是kg，保留两位小数:'))
BMI_index_number = weight / (height**2)
if BMI_index_number <= 18.5:
    print('过轻')
elif 18.5 < BMI_index_number <= 25:
    print('正常')
elif 25 < BMI_index_number <= 28:
    print('过重')
elif 28 < BMI_index_number <= 32:
    print ('肥胖')
else:
    print('严重肥胖')
print(BMI_index_number)
'''

#  循环
'''
names = ['Michael', 'Bob', 'Tracy']
for name in names:                               #  for...in循环，依次把list或tuple中的每个元素迭代出来
    print(name)                                  #  for 变量A in 变量 B
'''

'''
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
'''

#  range 
# list(range(100))             # [0,1,2,3,4]列出列表 0到4 五个数

# while
# 1加到999之和

"""
sum = 0
n = 0
while n < 1000:
    sum = sum + n
    n += 1
print(sum,n)            #  打印结果sum为1+2+'''+n-1之和 ， n的值
"""

"""
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("Hello,",name)
"""

#  break
'''
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

'''

#  continue

'''
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:   # 如果n是偶数，执行continue语句
        continue     # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

'''
#  *******    break 和 continue 搭配 if 语句使用      ******* 

#   廖雪峰py进度   https://www.liaoxuefeng.com/wiki/1016959663602400/1017104324028448     2021.08.24

#  使用dict和set


"""
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}        #  变量 = {'变量':数值，‘变量':数值,...}
d['Michael']                                       #  变量['变量']
95

要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
'Thomas' in d
False


二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
d.get('Thomas')
d.get('Thomas', -1)       #变量 'Thomas' 不在字典里则返回数值为-1.其中-1可以自己设定其他数值
-1


要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Bob')
d
{'Michael': 95, 'Tracy': 85}                                   #  输出结果已删除 Bob

"""


#   dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，
#   需要牢记的第一条就是dict的key必须是不可变对象。

#   这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。
#   这个通过key计算位置的算法称为哈希算法（Hash）。

#   要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。
#   而list是可变的，就不能作为key：



#    set

'''set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

要创建一个set，需要提供一个list作为输入集合：'''

 #   s = set([1, 2, 3])         #  变量 = set(['aq',2,1.31,   ....])
 #                             显示的顺序也不表示set是有序的。重复元素在set中自动被过滤：

 # 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
'''
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.add(4)
>>> s
{1, 2, 3, 4}'''

#   通过remove(key)方法可以删除元素：
'''
>>> s.remove(4)
>>> s
{1, 2, 3}
'''
#****************set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作********
'''
>>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1 & s2
{2, 3}
>>> s1 | s2
{1, 2, 3, 4}
'''

"""再议不可变对象
上面我们讲了，str是不变对象，而list是可变对象。

对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：

>>> a = ['c', 'b', 'a']
>>> a.sort()
>>> a
['a', 'b', 'c']
而对于不可变对象，比如str，对str进行操作呢：

>>> a = 'abc'
>>> a.replace('a', 'A')
'Abc'
>>> a
'abc'
虽然字符串有个replace()方法，也确实变出了'Abc'，但变量a最后仍是'abc'，应该怎么理解呢？

我们先把代码改成下面这样：

>>> a = 'abc'
>>> b = a.replace('a', 'A')
>>> b
'Abc'
>>> a
'abc'
要始终牢记的是，a是变量，而'abc'才是字符串对象！有些时候，
我们经常说，对象a的内容是'abc'，但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'：

┌───┐                  ┌───────┐
│ a │─────────────────>│ 'abc' │
└───┘                  └───────┘
当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，
而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，
变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：

┌───┐                  ┌───────┐
│ a │─────────────────>│ 'abc' │
└───┘                  └───────┘
┌───┐                  ┌───────┐
│ b │─────────────────>│ 'Abc' │
└───┘                  └───────┘
所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
"""
