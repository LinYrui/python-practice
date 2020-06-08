"""
判断两个单词是否为变位词（字母个数类型都相同，但字母顺序不同）
方法一：
将第一个单词中的字母逐个与第二个单词中的字母进行比对，如果比对相同，则将第二个
单词中的这个字母划掉（避免再次进行比对，防止第一个单词中的多个相同字母与第二个单词中的
单个字母进行重复比对），直到第一个字母中的单词全部比对一遍。再将第二个字母中的单词用
上述方法与第一个字母中的单词比对过一遍。
"""





def anagramSolution(s1, s2):
    alist = list(s2)
    pos1 = 0
    stillOK = True
    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            alist[pos2] = None
        else:
            stillOK = False
        pos1 += 1
    return stillOK


def areyouok(s1,s2):
    return anagramSolution(s1, s2) and anagramSolution(s2, s1)

print(areyouok('abaacd','aadcba'))