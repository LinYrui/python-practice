"""
方法三：
将每个词与26个字母进行比较，得出字母中包含的26个字母的个数，例如a有3个，b有2个.....
最终看看两个词中所含字母个数是否相同
注意：该方法对字母大小写有要求
本代码中，所有的字母必须为小写
"""


def anagramSoulution(s1, s2):
    # 设置两个计数器
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        # ord()函数的作用:接受长度为1的字符串转化为ASCII码  大写字母A与小写字母A的ASCII码不一样！
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j += 1
        else:
            stillOK = False
    return stillOK

print(anagramSoulution('apple', 'pleap'))








