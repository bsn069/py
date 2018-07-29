#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
ref https://www.cnblogs.com/zingp/p/6537841.html
选择排序法：每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放到序列的起始位置，直到全部排完。
'''

#coding=utf-8
import random

def sort(target):
    length = len(target)
    for i in range(length - 1):
        min = i
        for j in range(i+1, length):
            if target[j] < target[min]:
                min = j
        if min != i:
            target[min], target[i] = target[i], target[min]
    return target
    
 


if __name__ == '__main__':
    print("直接选择排序")
    a = [random.randint(1,1000) for i in range(10)]
    print("\nin =", a)
    print("out=", sort(a))
 