# # 条件分支语法：
# # if 条件：
# #    条件为真（ture）执行的操作
# # else：
# #    条件为假（false）执行的操作
# print("---------我爱鱼C工作室--------")
# temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
# guess = int(temp)
# if guess == 8:
#     print("我草，你是小甲鱼心里的蛔虫吗？！")
#     print("哼，猜中了也没有奖励！")
# else:
#     if guess > 8:
#         print("猜错啦，大了大了～")
#     else:
#         print("猜错啦，小了小了～")
# print("游戏结束，不玩啦～")

# # while循环语法：
# # 条件为真（ture）执行的操作
# print("---------我爱鱼C工作室--------")
# temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
# guess = int(temp)
# while guess != 8:
#     temp = input("哎呀猜错了，请重新猜一猜：")
#     guess = int(temp)
#     if guess == 8:
#         print("我草，你是小甲鱼心里的蛔虫吗？！")
#         print("哼，猜中了也没有奖励！")
#     else:
#         if guess > 8:
#             print("猜错啦，大了大了～")
#         else:
#             print("猜错啦，小了小了～")
# print("游戏结束，不玩啦～")


# while循环语法：三次机会结束
temp = int(input("请输入一个理想数字(大于0，且为整数)："))
while temp <= 0:
    temp = int(input("输入数字异常，请再试一次："))
    continue
num = 0
while temp > 0:
    if num == 3:
        print("太笨了你...")
        break
    guess = int(input("请您输入猜测的数值："))
    if guess == temp:
        print("恭喜你答对了！")
        break
    else:
        print(f"猜错了呢，再来一次吧,共有3次机会,还是{2-num}次机会")
        num += 1
