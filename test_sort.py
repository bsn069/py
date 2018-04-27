#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import random
import sort.bubble
import sort.sort_heap

if __name__ == '__main__':
    print('test_sort 作为主程序运行')
    a = [random.randint(1,1000) for i in range(10)]
    print(a)
    # sort.bubble.sort(a)
    sort.sort_heap.sort(a)
    print(a)
else:
    print('test_sort 初始化')
