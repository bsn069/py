#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
ref https://www.cnblogs.com/zingp/p/6537841.html
希尔排序是一种分组插入排序算法。
首先取一个整数d1=n/2，将元素分为d1个组，每组相邻量元素之间距离为d1，在各组内进行直接插入排序；
取第二个整数d2=d1/2，重复上述分组排序过程，直到di=1，即所有元素在同一组内进行直接插入排序。希尔排序每趟并不使某些元素有序，而是使整体数据越来越接近有序；最后一趟排序使得所有数据有序。

时间复杂度:O((1+τ)n)
不是很快，位置尴尬
'''

#coding=utf-8
import random

def sort(li):
    """希尔排序"""
    count = len(li)
    gap = count // 2
    while gap > 0:
        print("gap=", gap)
        for i in range(gap, count):
            tmp = li[i] #待排序值
            j = i - gap #排好序最大索引
            print("i=", i, "j=", j)
            while j >= 0 and tmp < li[j]:
                li[j + gap] = li[j]
                j -= gap
            li[j + gap] = tmp
        gap //= 2

if __name__ == '__main__':
    print("希尔排序")
    a = [random.randint(1,100) for i in range(11)]
    print("\nin =", a)
    sort(a)
    print("out=", a)
 