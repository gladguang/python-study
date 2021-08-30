name = 'ada wEn'

print(name.title())       #  .title  作用是让每个单词首字母大写显示

print(name.upper())       #  .upper  作用是让字符串全部大写

print(name.lower())       #  .lower  作用是让字符串全部小写




first_name = 'ada'

last_name = 'guang'

full_name = first_name + ' ' + last_name        #  可以用加号拼接字符串

print(full_name)


#****************************    删除空白    **************************

shanchu_jiewei_kongbai = '删除结尾空白测试  '

shanchu_jiewei_kongbai.rstrip()                     #  .rstrip() ***在调用变量时  删除字符串结尾空白字符 
                                            #   本体储存变量没有任何改变。 
shanchu_jiewei_kongbai = shanchu_jiewei_kongbai.rstrip()    #  将结果再次赋值变量。此时变量结尾空白符则没了


print(shanchu_jiewei_kongbai)                   #   打印



shanchu_kaitou_kongbai = '  删除开头空白测试'

shanchu_kaitou_kongbai.lstrip()                     #  .lstrip() 用法跟.strip()一样

shanchu_kaitou_kongbai = shanchu_kaitou_kongbai.lstrip()

print(shanchu_kaitou_kongbai)

#**********************************************************************











