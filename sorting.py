def bubble_sort(xs):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(xs)-1):
            current = xs[i]
            if current > xs[i+1]:
                xs[i] = xs[i+1]
                xs[i+1] = current
                swapped = True

def insertion_sort(xs):
    for i in range(1, len(xs)):
        current = xs[i]
        j = i-1
        while j >= 0 and xs[j] > current:
            xs[j+1] = xs[j]
            j = j-1
        xs[j+1] = current

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

def assertEqual(first, second):
    if first == second:
        print("OK")
    else:
        print("Fail: {} != {}".format(first, second))

if __name__ == '__main__':
    xs_unsorted = [5, 2, 4, 6, 1, 3]
    xs_sorted = [1,2,3,4,5,6]
    # 1. Bubble sort (in place)
    ys = xs_unsorted.copy()
    bubble_sort(ys)
    assertEqual(ys, xs_sorted)
    # 2. Insertion sort (in place)
    ys = xs_unsorted.copy()
    insertion_sort(ys)
    assertEqual(ys, xs_sorted)
    # 3. Merge sort (out of place)
    ys = merge_sort(xs_unsorted)
    assertEqual(ys, xs_sorted)
    # 4. Quicksort (out of place)
    ys = quicksort(xs_unsorted)
    assertEqual(ys, xs_sorted)

