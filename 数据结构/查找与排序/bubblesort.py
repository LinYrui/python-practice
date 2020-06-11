"""
冒泡排序:相邻两位进行比对，把更大的那一项通过交换放在最右边，从左到右比对一次就可以把最大的那一项放在整个数列的最右。
然后对除去最右一项后剩下的数列再次比对，结果是次大的项在倒数第二位。再把去掉第一项第二项的数列取第三大的数，依此进行。最后可以对整个数列进行排序。

选择排序的不同之处在于，它也是和冒泡排序一样进行比对，但它不比对后交换。而是标记最大那一项的索引，在对比完整个数列后将最大的那一项跟最后一行进行交换。
选择排序就是将第一项的索引设置为最大值的索引，然后和每一个值进行依此比较。大的那个值的索引作为新的最大值索引。比较一轮后就可以确定整行数列的最大值。
然后把这个值更最边上的值进行位置交换。

两者时间复杂度都是o(n^2)，但选择排序交换次数少，比冒泡排序法要优
"""

def bubblesort(alist):
    for count in range(len(alist)-1):
        for i in range(len(alist)-1-count):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def selectsort(alist):
    for count in range(len(alist)-1):
        indixofmax = 0
        for i in range(len(alist)-count):
            if alist[i] > alist[indixofmax]:
                indixofmax = i

        temp = alist[len(alist)-1-count]
        alist[len(alist)-1-count] = alist[indixofmax]
        alist[indixofmax] = temp





alist = [57, 24, 24,  31, 28, 21, 20, 69]
selectsort(alist)
print(alist)