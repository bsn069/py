'''
ref https://blog.csdn.net/minxihou/article/details/51738013
这里外层循环用来控制这个序列长度和比较次数。第二层循环用来交换。
按照惯例，来分析一下时间复杂度。我们先来定义比较次数记为C，元素的移动次数记为M。若我们随机到正好一一串从小到达排序的数列，那我们比较的一趟比较就能完事，那比较次数只与你定义的数列长度有关，则C=n-1，因为正好是从小到达排列的所以不需要在移动了，所以M=0。所以这个时候冒泡排序为最为理想的时间复杂度O（n）。
那么我们现在再来考虑一个极端的情况，整个序列都是反序的。则完成排序需要n-1次排序，每次排序需要n-i次比较(1<=i<=n-i),在算法上比较之后移动数据需要三次操作。在这种情况下，比较和移动的数均达到了最大值。

Cmax=n(n-1)/2=O(n^2)
Mmax=3n(n-1)/2=O(n^2)
所以，冒泡算法总的平均时间复杂度为O（n^2）
'''

#coding=utf-8
import random

def bubblesort(target):
    length = len(target)
    # print(length)
    while length > 0: 
        length -= 1
        cur = 0
        while cur < length:  
            if target[cur] > target[cur + 1]:
                target[cur], target[cur + 1] = target[cur + 1], target[cur]
            cur += 1
    return target
    
def bubblesort1(target):
    length = len(target)
    # print(target)
    for i in range(length - 1):
        # print("i=", i)
        for j in range(length - 1 - i):
            # print(j)
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]
    return target

def bubblesort2(target):
    length = len(target)
    for i in range(length - 1):
        bSwap = False
        for j in range(length - 1 - i):
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]
                bSwap = True
        if not bSwap:
            break
    return target
            


if __name__ == '__main__':
    print("冒泡排序")
    a = [random.randint(1,1000) for i in range(10)]
    print("\nin=", a)
    print(bubblesort(a))

    a = [random.randint(1,1000) for i in range(10)]
    print("\nin=", a)
    print(bubblesort1(a))

    a = [random.randint(1,1000) for i in range(10)]
    print("\nin=", a)
    print(bubblesort2(a))
 