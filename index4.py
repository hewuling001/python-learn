# python数据类型转换：int(整数)，str(字符串)，float(浮点数)；
a = 5.99
b = int(a)    # 比较特殊：int是使整形，但是要把小数整形的话使用的是截段处理，截取第一位数字；且int不能把文字整形；
print(b)

a = "520"
b = float(a)
print(b)

a = 520
b = str(a)
print(b)

# 获取类型的数据：type , isinstance(数据，对应的类型)--即会返回ture or false；
a = "520"
print(type(a))

a = "520"
print(isinstance(a, str))
print(isinstance(320, int))
print(isinstance(320.32, float))
