import time
import os

# 倒数时间（秒）
countdown = 60 * 60 * 26

while countdown:
    # 将秒转换为分钟和秒
    mins, secs = divmod(countdown, 60)
    # 格式化时间并打印倒数计时器
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    # 等待一秒钟
    time.sleep(1)
    # 减少倒数时间
    countdown -= 1

# 播放提示音
os.system('say "Time is up!"')
