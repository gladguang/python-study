


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




