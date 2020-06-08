"""
方法二： 将两个字符串转化为列表（因为字符串为不可变对象），然后进行排序，再将两个列表逐项对比
"""




ef anagramSolution(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()
    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False
    return matches

print(anagramSolution('abaaad', 'adaaab'))


