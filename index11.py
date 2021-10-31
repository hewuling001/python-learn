# 比较操作符，逻辑操作符，连接操作符，重复操作符和成员关系操作符
list1 = [123]
list2 = [234]
a = (list1 < list2)
print(a)

list1 = [123, 456]
list2 = [234, 456]
b = list1 > list2   # 数组里有多个元素，对比时分别拿最开始的第0个比较；
print(b)

list3 = [123, 456]
c = (list1 < list2) and (list1 == list3)
print(c)

list4 = list1 + list2
print(list4)   # 数组相加要加相同的数据类型，不能拿123+文字；

d = list3 * 3
print(d)

e = 123 in list3
print(e)
e = "小甲鱼" not in list3
print(e)

list5 = [123, ["小甲鱼", "牡丹花"], 456]
f = "小甲鱼" in list5
print(f)         # in 或者 not in 都只能在第一层，而小甲鱼是在数组的数组里
f = "小甲鱼" in list5[1]     # 在list5的第一个索引中
print(f)
print(list5[1][1])
# 获得“牡丹花”，因为list5中的[1]是list5中的第一个索引["小甲鱼", "牡丹花"]，
# 后边[1]是"小甲鱼", "牡丹花"]中的第一个索引位置的值；

# 列表的内置函数

# print(dir(list))
# count函数是计算其参数在列表中出现的次数    .表示范围
print(d.count(123))     # 本来是求123在list3中的次数，上边把list3赋值给d了；

# index索引，会返回其参数在列表中的位置,如果只有一个索引，那就是查找其第一次出现的位置；
print(d.index(123))
print(d.index(123, 3, 6))  # 第一个是查找的值123，第二个3是指从第几个位置开始找，第三个6是指截止最后找的位置
# 最后返回4，因为d=[123, 456, 123, 456, 123, 456]，从索引3开始数，第4个索引就是123；

# reverse把元素反转，前边的靠后，后边的靠前；倒数第二的会排顺数第二；（没有返回，需要变形之后再输出返回）
d.reverse()
print(d, 'reverse的打印结果')

# sort 用指定的方式对列表成员排序，默认从小到大进行排队；（没有返回，需要变形之后再输出返回）
list6 = [4, 3, 2, 5, 8, 66]
list6.sort()
print(list6)
# 如果想从大到小排队，可以先sort排小到大，再用reserve翻转；
# 更快的方法使用：
list6.sort(reverse=True)
print(list6)

list7 = list6[:]
# slice分片，[:]可以得到整个数组的拷贝，list7拷贝过来的[4, 3, 2, 5, 8, 66]，传递的拷贝内容，当另一个改变时，它拷贝出来的内容并没有改变；
print(list7, "list7的值")
list8 = list6     # list8赋值和指针，当另一个指针方向/地址改变了，另一个也跟着改变，传递的地址；
print(list8, "list8的值")
list6.sort()
print(list6, "翻转list6")
print(list7)
print(list8)
