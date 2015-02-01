from time import time
from random import randint

def bubble_sort(xs):
    xs = list(xs)
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(xs)-1):
            current = xs[i]
            if current > xs[i+1]:
                xs[i] = xs[i+1]
                xs[i+1] = current
                swapped = True
    return xs

def insertion_sort(xs):
    xs = list(xs)
    for i in range(1, len(xs)):
        current = xs[i]
        j = i-1
        while j >= 0 and xs[j] > current:
            xs[j+1] = xs[j]
            j = j-1
        xs[j+1] = current
    return xs

def merge_sort(xs):
    if not xs:
        return []
    n = len(xs)
    if n == 1:
        return xs
    q = n // 2 + n % 2
    left = merge_sort(xs[:q])
    right = merge_sort(xs[q:])
    i, j = 0, 0
    merged = []
    sentinel = 'stop'
    left += [sentinel]
    right += [sentinel]
    for k in range(n):
        if left[i] == sentinel:
            merged += [right[j]]
            j += 1
        elif right[j] == sentinel:
            merged += [left[i]]
            i += 1
        elif left[i] <= right[j]:
            merged += [left[i]]
            i += 1
        else:
            merged += [right[j]]
            j += 1
    return merged

def quicksort(xs):
    if not xs:
        return []
    else:
        pivot = xs[0]
        lhs, rhs = [], []
        for x in xs[1:]:
            if x < pivot:
                lhs += [x]
            else:
                rhs += [x]            
        return quicksort(lhs) + [pivot] + quicksort(rhs)


### Main body ###
# generate array of random integers
xs = [randint(0, 1e6) for i in range(10000)]

# sort using different methods and measure time of 
# execution of each algorithm
times = []
# 1. bubble sort
start = time()
bubble_sort(xs)
stop = time()
times += [stop - start]

# 2. insertion sort
start = time()
insertion_sort(xs)
stop = time()
times += [stop - start]

# 3. merge sort
start = time()
merge_sort(xs)
stop = time()
times += [stop - start]

# 4. quicksort
start = time()
quicksort(xs)
stop = time()
times += [stop - start]

# output sorting times to screen, and
# plot results if matplotlib installed
labels = ['bubble', 'insertion', 'merge', 'quicksort']
for label, t in zip(labels, times):
    print('%s sort: %f seconds' % (label.capitalize(), t))
try:
    import matplotlib.pyplot as plt
    plt.figure()
    x = [1,2,3,4]
    plt.plot(x, times, 'ro')
    plt.xticks(x, labels, rotation=35)
    plt.ylabel('Execution time, [sec]')
    plt.grid()
    plt.savefig('sorting.pdf')
except ImportError:
    pass

