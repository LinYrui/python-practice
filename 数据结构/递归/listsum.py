"""
递归求和,使用递归的方法来求列表的和
1.递归必须要有一个基本的结束条件（最小规模的问题直接给答案）
2.递归算法要能够向基本结束条件方向演进（规模逐渐减小）
3.递归算法必须调用自身（解决减小了规模的相同问题）
"""

def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])

print(listsum([1, 2, 3, 4, 5, 6]))