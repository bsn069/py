import random


def bubblesort(target):
    length = len(target)
    print(length)
    while length > 0: 
        length -= 1
        cur = 0
        while cur < length:  
            if target[cur] > target[cur + 1]:
                target[cur], target[cur + 1] = target[cur + 1], target[cur]
            cur += 1
    return target
    
if __name__ == '__main__':
    a = [random.randint(1,1000) for i in range(100)]
    print(bubblesort(a))