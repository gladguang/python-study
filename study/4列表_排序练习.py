#  想出五个地方，并打印出来
place = ['nanchang','shenzhen','shanghai','changsha','beijing']
print('1、想出五个地方，并打印出来')
print(place)
print('\n')

# 使用sort()按字母顺序打印这个列表,同时不要修改它
print('2、使用sort()按字母顺序打印这个列表,同时不要修改它')
print(sorted(place))
print('\n')

# 再次打印该列表，核实顺序未改变
print('3、再次打印该列表，核实顺序未改变')
print(place)
print('\n')

# 使用sort()按字母顺序相反打印这个列表,同时不要修改它
print('4、使用sort()按字母顺序相反打印这个列表,同时不要修改它')
print(sorted(place,reverse=True))
print('\n')

# 再次打印该列表，核实顺序未改变
print('5、再次打印该列表，核实顺序未改变')
print(place)
print('\n')

# 使用reverse()修改该列表
print('6、使用reverse()修改该列表')
place.reverse()
print(place)
print('\n')

#  使用reverse()再次修改列表元素排序。打印列表核实恢复原来顺序
print('7、使用reverse()再次修改列表元素排序。打印列表核实恢复原来顺序')
place.reverse()
print(place)
print('\n')

#  使用sort()修改该列表
print('8、使用sort()修改该列表')
place.sort()
print(place)
print('\n')

# 使用sort()修改该列表,并使元素相反排序
print('9、使用sort()修改该列表,并使元素相反排序')
place.sort(reverse=True)
print(place)
print('\n')