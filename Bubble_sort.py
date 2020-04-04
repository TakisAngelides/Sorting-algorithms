import random as r
from time import time
import matplotlib.pyplot as plt

def swap(l, el, next_el):
    tmp = l[el]
    l[el] = l[next_el]
    l[next_el] = tmp

def bubble_sort(list_to_sort):
    # print(f'The list to sort is: {list_to_sort}')
    start_time = time()
    no_swap = False
    for sweep in range(len(list_to_sort)):
        if no_swap:
            break
        score = 0
        for element in range(len(list_to_sort) - 1):
            next_element = element + 1
            if list_to_sort[element] > list_to_sort[next_element]:
                swap(list_to_sort, element, next_element)
                score += 1
        if score == 0:
            no_swap = True

    finish_time = time()
    duration = finish_time - start_time
    # print(f'The sorted list is: {list_to_sort}')
    # print(f'The time taken to sort a list of length {len(list_to_sort)} was {duration:.3f} seconds')
    return duration

def coctail_sort(list_to_sort):
    # print(f'The list to sort is: {list_to_sort}')
    start_time = time()
    no_swap = False
    forward_sweep_end_index = len(list_to_sort) - 1
    for sweep in range(len(list_to_sort)):
        if no_swap:
            break
        score = 0
        for element in range(len(list_to_sort) - 1):
            next_element = element + 1
            if list_to_sort[element] > list_to_sort[next_element]:
                swap(list_to_sort, element, next_element)
                score += 1
        for element in range(forward_sweep_end_index - 1, 1, -1):
            previous_element = element - 1
            if list_to_sort[element] < list_to_sort[previous_element]:
                swap(list_to_sort, previous_element, element)
                score += 1
        if score == 0:
            no_swap = True
        forward_sweep_end_index -= 1
    finish_time = time()
    duration = finish_time - start_time
    # print(f'The sorted list is: {list_to_sort}')
    # print(f'The time taken to sort a list of length {len(list_to_sort)} was {duration:.3f} seconds')
    return duration

def compare_algorithms():
    x = []
    y_bs = []
    y_cs = []
    for i in range(200):
        length = i*10 + 10
        list_to_sort = tuple([r.randint(-100, 100) for _ in range(length)])
        duration_bs = bubble_sort(list(list_to_sort))
        duration_cs = coctail_sort(list(list_to_sort))
        x.append(length)
        y_bs.append(duration_bs)
        y_cs.append(duration_cs)
    plt.plot(x, y_bs, color = 'k')
    plt.plot(x, y_cs, color = 'r')
    plt.legend(['Bubble sort', 'Coctail sort'])
    plt.title('Bubble sort vs Coctail sort')
    plt.ylabel('Duration / Seconds')
    plt.xlabel('Length of list to sort')
    plt.ylim(bottom = 0)
    plt.savefig('comparison.png')
    plt.show()

compare_algorithms()
