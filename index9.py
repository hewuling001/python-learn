# 打了激素的数组：列表
# 创建一个普通列表
member = ["小甲鱼", "小布丁", "黑夜", "白昼"]
print(member)

number = ["1", "2", "3"]
print(number)

# 创建一个混合列表
mix = ["小甲鱼", 3.14, [1, 2, 3]]
print(mix)

# 创建一个空列表，将来使用
empty = []
print(empty)

# 向列表添加元素：
# .append()  .是范围; append只能增加一个参数；增加的数往最后补；
member.append("小武玲")
print(member)
print(len(member))

# .extend([]),可以增加多个参数，使用一个列表来扩展另一个列表，所以参数应该为一个列表；增加的数往最后补；
number.extend(["88", "66"])
print(number)
print(len(number))

# insert(代表列表中的索引位置，要在第一个参数的位置插入的元素)；增加的数排是可以指定在前边位置;(顺序索引都是从0开始)
mix.insert(0, "向日葵")
print(mix)
