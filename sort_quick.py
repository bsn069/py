'''
ref https://www.cnblogs.com/zingp/p/6537841.html
取一个元素p（通常是第一个元素，但是这是比较糟糕的选择），使元素p归位（把p右边比p小的元素都放在它左边，在把空缺位置的左边比p大的元素放在p右边）；
列表被p分成两部分，左边都比p小，右边都比p大

时间复杂度：O(nlogn)，一般情况是O(nlogn)，最坏情况（逆序）：O（n^2）
稳定性：不稳定
特点：就是快
'''

#coding=utf-8
import random

 
def sort(array, left, right):
    if left < right:
        mid = partition(array, left, right)
        sort(array, left,  mid-1)
        sort(array, mid+1, right)

def partition(array, left, right):
    p = left #左为基准值索引
    tmp = array[p] #基准值
    while left < right:
        # 向左找第一个<tmp的索引
        while left < right:
            if array[right] < tmp: # 找到比tmp小的 跳出
                break
            right -= 1       
        # 向右找第一个>tmp的索引
        while left < right:
            if array[left] > tmp: # 找到比tmp大的 跳出
                break
            left += 1
        #交换左右值
        print(left, right)
        array[left], array[right] = array[right], array[left]
    #找到tmp的排序位置 left==right 交换
    array[p] = array[left]
    array[left] = tmp
    return left

if __name__ == '__main__':
    print("快速排序")
    a = [random.randint(1,100) for i in range(100)]
    print("\nin =", a)
    sort(a, 0, len(a) - 1)
    print("out=", a)
 