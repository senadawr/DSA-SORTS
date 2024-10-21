def insertionSort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i-1

        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    
a = [9, 3, 2, 5]
print(a)
insertionSort(a)
print(a)