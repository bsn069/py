'''
ref https://www.cnblogs.com/zingp/p/6537841.html
步骤：
　　建立堆
　　得到堆顶元素，为最大元素
　　去掉堆顶，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序。
　　堆顶元素为第二大元素。
　　重复步骤3，直到堆变空

时间复杂度：O(nlogn)，
稳定性：不稳定
特点：通常都比快排慢
'''

#coding=utf-8
import random

# [rootIndex, endIndex]
def rootDown(array, rootIndex, endIndex):
    childIndex = 2*rootIndex + 1   # rootIndex的左孩子
    rootValue = array[rootIndex]     # 当前调整的堆的根节点
    while childIndex <= endIndex:    # 如果孩子还在堆的边界内
        # 如果rootIndex有右孩子,且右孩子比左孩子大
        if childIndex < endIndex and array[childIndex] < array[childIndex+1]:   
            childIndex = childIndex + 1 # 大孩子就是右孩子

        # 比较根节点和大孩子 
        #如果根节点比大孩子小
        if rootValue < array[childIndex]:
            # 大孩子上位
            array[rootIndex] = array[childIndex] 
            # 新调整的堆的父节点
            rootIndex = childIndex 
            # 新调整的堆中rootIndex的左孩子
            childIndex = 2*rootIndex + 1
        # 否则就是父节点比大孩子大，则终止循环 
        else: 
            break
    # 最后rootIndex的位置由于是之前大孩子上位了，是空的，而这个位置是根节点的正确位置。
    array[rootIndex] = rootValue 

def sort(array):
    n = len(array)
    
    # 建堆，从最后一个有孩子的父亲开始，直到根节点
    for i in range(n//2 - 1, -1, -1):
        # 每次调整i到结尾
        rootDown(array, i, n-1)

    # 挨个出数
    for i in range(n-1, -1, -1):
        # 把根节点和调整的堆的最后一个元素交换
        array[0], array[i] = array[i], array[0]
        # 再调整，从0到i-1
        rootDown(array, 0, i-1)
 

if __name__ == '__main__':
    print("堆排序")
    a = [random.randint(1,100) for i in range(11)]
    print("\nin =", a)
    sort(a)
    print("out=", a)
 