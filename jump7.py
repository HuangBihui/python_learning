#打印1到100之间的整数，跳过可以被7整除的，以及数字中包含7的整数
for i in range(1,101):
    if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
        continue
    else:
        print(i)
