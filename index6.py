# 了不起的分支与循环1
# 打飞机游戏框架：
# 加载背景音乐
# 播放背景音乐（设置单曲循环）
# 我方飞机诞生
# interval=0(间隔为0)
# while ture:
#       if 用户是否点击了关闭按钮：
#           退出程序
#       interval += 1
#       if interval == 50:（即每执行一次循环体-移动50格，飞机+1）
#           interval = 0(每诞生完一个飞机就要初始化)
#           小飞机诞生
#       小飞机移动一个位置
#       屏幕刷新
#       if 用户鼠标产生移动：
#           我方飞机中心位置 = 用户鼠标位置
#           屏幕刷新
#       if 我方飞机与小飞机发生肢体冲突：
#           我方挂，播放撞机音乐
#           修改我方飞机图案
#           打印“game over”
#           逐渐淡出停止背景音乐
