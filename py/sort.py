import numpy as np
import random

def swap(p1, p2, l):
    temp = l[p2]
    l[p2] = l[p1]
    l[p1] = temp


def quick(L):
    sort(L, 0, len(L)-1)
    return L


def sort(L, first, right):
    if first < right:
        num = random.randint(first, right)
        swap(num,right,L)
        middle = quickSort(L, first, right, L[right])
        sort(L, first, middle[0] - 1)
        sort(L, middle[1] + 1, right)
    else:
        return


def quickSort(arr, first, last, num):
    index = first
    less = first -1
    more = last + 1
    while index < more:
        if arr[index] < num:
            less += 1
            swap(less, index, arr)
            index += 1
        if arr[index] > num:
            more -= 1
            swap(index, more, arr)
        if arr[index] == num:
            index += 1
    return less+1, more-1


s = [10,1,2,3,4,5,5,5,6,7]
print(s)
quick(s)
print(s)