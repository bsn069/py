'''
ref https://www.cnblogs.com/zingp/p/6537841.html
一次归并：将现有的列表分为左右两段，将两段里的元素逐一比较，小的就放入新的列表中。比较结束后，新的列表就是排好序的。

然后递归。

时间复杂度：O(nlogn)
稳定性：稳定
'''

#coding=utf-8
import random
# 一次归并
def merge(array, low, mid, high):
    """
    两段需要归并的序列从左往右遍历，逐一比较，小的就放到
    tmp里去，再取，再比，再放。
    """
    tmp = []
    i = low
    j = mid +1
    while i <= mid and j <= high:
        if array[i] <= array[j]:
            tmp.append(array[i])
            i += 1
        else:
            tmp.append(array[j])
            j += 1
    while i <= mid:
        tmp.append(array[i])
        i += 1
    while j <= high:
        tmp.append(array[j])
        j += 1
    print(tmp)
    array[low:high+1] = tmp

def sort(array, low, high):
    if low < high:
        # print(low, high)
        mid = (low + high) // 2
        sort(array, low, mid)
        sort(array, mid+1, high)
        merge(array, low, mid, high)
 

if __name__ == '__main__':
    print("归并排序")
    a = [random.randint(1,100) for i in range(11)]
    print("\nin =", a)
    sort(a, 0, len(a) - 1)
    print("out=", a)
 