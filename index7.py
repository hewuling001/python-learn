# 了不起的分之循环2
# 例子：按照100分制，90分以上成绩A，80-90为B,60-80为C，60以下为D，大于100则“输入错误～”

# 方法一：
score = int(input("请输入一个分数"))
if 100 >= score >= 90:
    print("A")
if 90 > score >= 80:
    print("B")
if 80 > score >= 60:
    print("C")
if 60 > score > 0:
    print("D")
if 0 > score > 100:
    print("输入错误～")

# 方法二：
score = int(input("请输入一个分数"))
if 100 >= score >= 90:
    print("A")
else:
    if 90 > score >= 80:
        print("B")
    else:
        if 80 > score >= 60:
            print("C")
        else:
            if 60 > score > 0:
                print("D")
            else:
                if 0 > score > 100:   # 这步也可以省略；
                    print("输入错误～")

# 方法三：
score = int(input("请输入一个分数"))
if 100 >= score >= 90:
    print("A")
elif 90 > score >= 80:
    print("B")
elif 80 > score >= 60:
    print("C")
elif 60 > score > 0:
    print("D")
else:
    print("输入错误～")

# 二、悬挂else:是指else会和就近的if匹配，但如果想和第一个if匹配就需要对齐第一个；容易造成悬挂,下列就是错误事例；
# if (hi > 2):
#    if(hi > 7):
#        printif("哇好棒呀")
# else:   # else在这就是和第一个if对齐，若要和第二个，则需要tab缩紧；
#    printif("切")

# 三、条件表达式（三元操作符--指这个操作符有3个操作数）
# x, y = 4, 5
# if x < y:        # 条件
#    small = x    # 赋值号两侧是操作数，即二元操作符
#    else:
#        small = y
# 例子可以改进为：
# small = x if x < y else y   # 操作符语法：x if 条件 else y

# 四、断言（assert关键字），当关键字后边的条件为假时，程序自动崩溃并弹出assertionError的异常；
assert 3 > 4    # 系统会弹出AssertionError;当需要确保程序中某个条件一定为真才能让程序正常运行时，assert就管用；
