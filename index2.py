# 变量：
# 在使用变量之前要先对其赋值；
# 变量名包括字母、数字和下划线；但不能以数字开头，且字母大小写是不同的；
# 等号是赋值意思，左边是名字，右边是值；
teacher = "小甲鱼"
print(teacher)
teacher = "小宝贝"
print(teacher)

first = 3
second = 8
third = first + second 
print(third)

myboss = "宋彦超"
yourboss = "真帅"
ourboss = myboss + yourboss
print(ourboss)



# 字符串：
#如果字符串中有单引号或双引号，可以用转义符号（\）对字符串中的引号进行转义：
print ("let\'s go!")
print("Let's go!")

# 原始字符串：
str = "C:\now"
print(str)   #出来的结果是C：下一行ow  ,即把\n当作了分隔的转义字符了；所以可以用反斜杠对反斜杠进行转义
str = "C:\\now"
print(str)    #这样结果就是正常的；（反斜杠不可加在最后）
#如果一个字符串中有多个反斜杠\，可在整个字符串前加字母r：
str = r"C:\now\one\two\three"
print(str)

# 长字符串，使用三重引号字符串：
str = """一二三四五
上山打老虎
老虎不在家
去找小松鼠
松鼠在吃蛙
一起乐哈哈......
"""
print(str)