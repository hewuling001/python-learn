# 打了激素的数组：
# 从列表中获取元素：
member = ["小甲鱼", "向日葵", "小布丁", "黑夜", "白昼", "小乌堆"]
temp = member[0]
member[0] = member[1]
member[1] = temp
print(member)

# 从列表删除元素：
# .remove(),不需要知道元素的位置，只要清楚名字，根据元素/值删除；
member.remove("小布丁")
print(member)

# del 语句,根据位置/索引删除，也可以整个；
del member[0]
print(member)

# pop(),删除最后一个值并返回这个值；如果pop(索引)，则删除索引位置的元素并返回该元素；
name = member.pop()
print(name)

list = member.pop(1)
print(list)

# slice[这是开始截取的数，最后截取的数但不包含它自己]，包头不包尾；
test = member[1:3]
print(test)            # [:]可以得到整个数组的拷贝
