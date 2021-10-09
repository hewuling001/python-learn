print("---------我爱鱼C工作室--------")
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = input(temp)
if guess == 8:
    print("我草，你是小甲鱼心里的蛔虫吗？！")
    print("哼，猜中了也没有奖励！")
else:
    print("猜错啦，小甲鱼现在心里想的是8！")
print("游戏结束，不玩啦～")

# BIF==Built- in function == 内置函数
# input、print都是BIF;
# "=" 是赋值，“==” 是等于；

name = input("请输入您的姓名：")   # 运行后可以输入名字
print('你好，' + name + '!')     # 最后输出“你好，xxx！“

temp = input("请输入1到100之间的数字")
num = int(temp)             
if 1<= num <=100:
    print("你妹妹好漂亮")
else:
    print("你大爷好丑呀")
  
#  input 是为name 赋值， int 是为 temp变为整数，转整形；
