"""
插入排序法跟我打斗地主时的排序思维是一样的。先把第一张设定好，然后左边作为排好序的，右边作为还没有排序准备要插入进来的。
将右边还没有排序的部分一张张插入到左边已经排好次序的序列里面且放在合适的位置，这样就可以使得左边拍好序的部分越来越大，待插入排序的牌愈来愈少，最后
全部插入排序完成。
时间复杂度依然是O(n^2)
"""

def insertionsort(alist):
    for index in range(len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position -1

        alist[position] = currentvalue

testlist = [55, 21, 33, 65, 98, 14, 47]
insertionsort(testlist)
print(testlist)