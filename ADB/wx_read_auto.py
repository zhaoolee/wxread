from uiautomator import device as d
import time
import datetime
import random
#点亮屏幕
def lightScreen():
    d.screen.on()

# 自动翻页，翻页后休息5-10秒钟
def autoSwipe():
    # 假装看书45-55秒钟(假装是人类在看书。。。)
    read_time = random.randint(45,50)
    time.sleep(read_time)
    print("阅读花费：",read_time,"秒")
    # 从（1000,500）到（30,500）
    d.swipe(1000, 500, 30, 500) #这里需要根据你的模拟器的具体坐标测试
    # 休息一段时间(休息的时间=60秒-看书的秒数)
    time.sleep(60-read_time)
    print("休息",60-read_time,"秒,放松下眼睛~")


# 执行5小时(300分钟)
if __name__ == '__main__':
    all_time = 300    
    user_input_time = input("请输入需要阅读的分钟数(请输入正整数):")
    try:
        user_input_time = int(user_input_time)
        if (user_input_time > 0):
            print("程序将会执行",user_input_time,"分钟")
            all_time = user_input_time
    except:
        print("您输入的值不合法， 将使用默认参数300， 程序将会自动执行5小时")
        pass

    for i in range(all_time):
        lightScreen()
        print("自动点亮屏幕, 开始阅读。。。")
        autoSwipe()
        print("==>已经阅读", i+1 ,"分钟", "还差", all_time-i-1,"分钟完成阅读")


