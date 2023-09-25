import random

def bubbleSort(a):
    loop = 1
    while loop == 1:
        swap = 0
        for i in range(len(a) - 1):
            if a[i] > a[i+1]: #if left > right, swap places
                temp = a[i+1]
                a[i+1] = a[i]
                a[i] = temp
                swap += 1
        if swap == 0: #running once through with no swaps means it's sorted
            loop = 0
    return a


def merge(a, b):
    apos = 0 #position in array a
    bpos = 0 #position in array b
    c = []
    while apos < len(a) and bpos < len(b): #runs until one array runs out of elements
        if a[apos] < b[bpos]: #arrays are already sorted, check which index is smaller
            c.append(a[apos])
            apos += 1
        else:
            c.append(b[bpos])
            bpos += 1

    while apos < len(a):
        c.append(a[apos])
        apos += 1

    while bpos < len(b):
        c.append(b[bpos])
        bpos += 1

    return c


def mergeSort(a):
    if len(a) == 1:
        return a
    mid = int(len(a) / 2) #get integer middle of array
    left = [a[i] for i in range(mid)] #first half of array
    right = [a[i] for i in range(mid, len(a))] #second half of array
    left = mergeSort(left) #sort first half
    right = mergeSort(right) #sort second half
    a = merge(left, right) #combine both halfs
    return a


def insertionSort(a):
    for i in range(len(a) - 1):
        if a[i+1] < a[i]: #if element is less than previous, swap them
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp

            j = i
            while(a[j-1] > a[j] and j > 0): #check all previous elements if they have to swap
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp
                j -= 1
    return a


def quickSort(a):

    if len(a) <= 1:
        return a

    pivot = a[-1]
    lower = []
    higher = []
    for i in range(len(a)-1):
        if a[i] < pivot:
            lower.append(a[i])
        else:
            higher.append(a[i])

    lower = quickSort(lower)
    higher = quickSort(higher)

    a = lower + [pivot] + higher
    return a


def selectionSort(a):
    b = []
    while len(a) != 0:
        lowest = a[0]
        index = 0
        for i in range(1, len(a)):
            if a[i] < lowest:
                lowest = a[i]
                index = i
        b.append(a.pop(index))

    return b


def main():
    a = [i for i in range(20)]

    random.shuffle(a)
    b = list(a)
    bubbleSort(b)
    print('Bubble sort:')
    print('Original:', a)
    print('Sorted:', b)

    random.shuffle(a)
    c = list(a)
    c = mergeSort(c)
    print('\nMerge sort:')
    print('Original:', a)
    print('Sorted:', c)

    random.shuffle(a)
    d = list(a)
    d = insertionSort(d)
    print('\nInsertion sort:')
    print('Original:', a)
    print('Sorted:', d)

    random.shuffle(a)
    e = list(a)
    e = quickSort(e)
    print('\nQuick sort:')
    print('Original:', a)
    print('Sorted:', e)

    random.shuffle(a)
    f = list(a)
    f = selectionSort(f)
    print('\nSelection sort:')
    print('Original:', a)
    print('Sorted:', f)


main()
