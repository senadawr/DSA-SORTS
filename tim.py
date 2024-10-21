def insertionSort(a, left = 0, right = None):
    for i in range(left + 1, right + 1):
        key = a[i]
        j = i - 1

        while j >= left and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        
        a[j + 1] = key
    
    return a

def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])
    
def timSort(a):
    minRun = 2
    n = len(a)

    for i in range(0, n, minRun):
        insertionSort(a, i, min(i + minRun - 1, (n-1)))

    size = minRun
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size
            end = min((start + size * 2 - 1), (n - 1))
            mergedA = merge(a[start:mid], a[mid:end + 1])
            a[start:start + len(mergedA)] = mergedA
        size *= 2
    return a

a = [9, 3, 2, 5]
print(a)
timSort(a)
print(a)