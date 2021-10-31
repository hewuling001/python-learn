# for 目标 in 表达式： 最常搭配range，break,continue;
# 循环体
favour = "yanchao"
for i in favour:
    print(i, end="-")   # end=是用来连接

member = ["小甲鱼", "小布丁", "小乌龟", "王八"]
for each in member:
    print(each, len(each))   # len是计算长度并返回；


# range()内置函数，语法：range([start,]stop[,step=1]),这个BIF有3个参数，用中括号扩起来的是表示可选；
# step默认是1，如果是2，则从开始的那个数就要加2,每次递增2；
# range的作用是生成一个从start参数的值开始到stop参数的值结束的数字序列；
i = range(5)
print(i)   # 则返回range(0,5)，因为返回的是一个对象；

a = list(range(5))
for a in range(5):
    print(a)    # 如果没有for in，返回的是[0,1,2,3,4],生成一个列表；在for in里则循环成0，1，2，3，4；
# 同时，只有一个参数时，默认从0开始，不包含最后stop的数值；

for i in range(2, 9):
    print(i)

for i in range(1, 10, 2):
    print(i)

# break:终止当前循环，跳出循环体
bingo = "宋彦超是小乌堆"
answer = input("请输入宋彦超最想听到的一句话：")
while True:
    if answer == bingo:
        break
    answer = input("oh sorry~请重新输入（答案正确才能退出游戏哦）：")
print("哎哟帅哦～")
print("你真是小彦超肚子里的小蛔虫～")

# continue:终止本轮循环并开始下一轮循环,开始下一轮循环前会先测试条件，只有为Ture才会开始，否则退出；
for i in range(10):
    if i % 2 != 0:   # 即余数为2，不等于0即不是偶数的话，输出奇数，如是偶数，则i+2再输出；
        print(i)
        continue
    i += 2
    print(i)
#    （0，1，2，3，4，5，6，7，8，9）分别除以2，看余数是偶数还是奇数，偶数+2再输出，奇数直接输出；
