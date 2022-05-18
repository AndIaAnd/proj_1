# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a algoritm  file.
"""
def quick_sort(array): # быстрая сортировка
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        
        great = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(great)

print(quick_sort([76,3,93,5,15,44,55,765,93]))
"""
from sklearn import datasets

dig = datasets.load_digits()  
dig.images[0] 
import matplotlib.pyplot as plt
plt.imshow(dig.images[0], cmap=plt.cm.gray_r) 
import numpy as np

a = np.matrix.flatten(dig.images[0])
print(a)
"""
def binary_search(list1, item): # бинарный поиск
    low = 0
    high = len(list1)-1
    
    while low <= high:
        mid = (low + high)
        guess = list1[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 4, 6, 9, 55, 33]

print(binary_search(my_list, 33))

def find_small(arr): # поиск наименьшего
    small = arr[0]
    small_ind = 0
    for i in range(1, len(arr)):
        if arr[i] < small:
            small =  arr[i]
            small_ind = i
    return small_ind
def selecSort(arr):
    newArr = []
    for i in range(len(arr)):
        small = find_small(arr)
        newArr.append(arr.pop(small))
    return newArr

print(selecSort([55, 44, 124, 22, 35, 1, 2, 3]))

def coudow(a): # поиск
    print(a)
    if a <= 0:
        return a
    else:
        coudow(a)
book = dict()      
book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49
print(book)

graph = {}

graph["you"] = ["alice", "bob", "claire"] #графы
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["peggy"] = []
graph["thom"] = []
graph["anuj"] = []
graph["jonny"] = []

from collections import deque 

sear_que = deque()
sear_que += graph["you"]
print(sear_que)

def a(sear_que):
    while sear_que:
        person = sear_que.popleft()
        if person_is_seller(person):
            print(person)
            return True
        else:
            sear_que += graph[person]
    return False

def person_is_seller(name):
    return name[-1] == 'm'
a(sear_que)
def search(name):
    sear_que = deque()
    sear_que += graph[name]
    searched = []
    while sear_que:
        person = sear_que.popleft()
        if not person in searched:
            if person_is_seller(person):
                print("is a mango seller!", person)
                return True
            else:
                sear_que += graph[person]
                searched.append(person)
    return False
search("you")

graph1 = {}
graph1["start"] = {}
graph1["start"]["a"] = 6
graph1["start"]["b"] = 2

a1 = graph1["start"].keys()
print(a1)
