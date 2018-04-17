'''
ref https://www.cnblogs.com/zingp/p/6537841.html
列表被分为有序区和无序区两个部分。最初有序区只有一个元素。
每次从无序区选择一个元素，插入到有序区的位置，直到无序区变空。
其实就相当于摸牌
'''

#coding=utf-8
import random

def sort(target):
    length = len(target)
    for i in range(1, length): #从第2个到最后
        temp = target[i] #待排序值
        j = i - 1 #排好序最大索引
        while j >= 0 and target[j] > temp: #当前j位置的比待排序的大
            target[j+1] = target[j] #右移
            j -= 1 #前一张
        target[j+1] = temp
    return target
    
 


if __name__ == '__main__':
    print("直接插入排序")
    a = [random.randint(1,1000) for i in range(10)]
    print("\nin =", a)
    print("out=", sort(a))
 