cost = [1,2,3,4,5]
profit = [1,2,3,4,5]
money = 1
import random

def swap(l, p1, p2):
    temp = l[p2]
    l[p2] = l[p1]
    l[p1] = temp


def quick(arr, t):
    sort(arr, 0, len(arr) - 1, t)


def sort(arr, first, last, t):
    if first < last:
        num = random.randint(first, last)
        swap(arr, num, last)
        middle = sortProcess(arr, first, last, arr[last], t)
        sort(arr, first, middle[0], t)
        sort(arr, middle[1], last, t)


def sortProcess(arr, first, last, num, t):
    less = first - 1
    more = last + 1
    index = first
    if t == "c":
        while index < more:
            if arr[index].cost < num.cost:
                less += 1
                swap(arr, less, index)
                index += 1
            if arr[index].cost > num.cost:
                more -= 1
                swap(arr, more, index)
            if arr[index].cost == num.cost:
                index += 1
    if t == "p":
        while index < more:
            if arr[index].profit > num.profit:
                less += 1
                swap(arr, less, index)
                index += 1
            if arr[index].profit < num.profit:
                more -= 1
                swap(arr, more, index)
            if arr[index].profit == num.profit:
                index += 1
    return less, more


class Project:
    def __init__(self, cost, profit):
        self.cost = cost
        self.profit = profit


def do_project(cost,profit,money,k):
    c = []
    p = []
    time = 0
    for i in range(0,len(cost)):
        project = Project(cost[i],profit[i])
        c.append(project)
    quick(c,'c')
    first = c.pop(0)
    p.append(first)
    if money < first.cost:
        return 0
    else:
        while c[0].cost <= money :
            p.append(c.pop(0))
        quick(p,'p')
        while time < k and  p != []:
            money += p.pop(0).profit
            time += 1
            while  c != [] and c[0].cost <= money :
                p.append(c.pop(0))
            quick(p,'p')
    return money

print(do_project(cost,profit,money,3))