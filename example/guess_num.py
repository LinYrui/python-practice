"""
在1-100之间随机产生一个数字让用户猜测
根据用户猜测数字给予猜大了，猜小了还是猜对了的反馈，
猜对结束游戏，只能够猜测5次
"""

import random

m = random.randint(1,100)

count = 0  #猜的次数
total = 5

while True:
    n = int(input('请猜一个数字： '))

    if n < m:
        print('猜小了')
    elif n > m:
        print('猜大了')
    else:
        print('猜对了')
        break
    count = count + 1
    if count >= total:
        print(f'你猜了{total}次了，游戏结束')
        break