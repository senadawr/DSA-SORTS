def insertionSort(b):
    for i in range(1, len(b)):
        key = b[i]
        j = i - 1
        while j >= 0 and b[j] > key:
            b[j + 1] = b[j]
            j -= 1
        b[j+1] = key

def bucketSort(a):
    n = len(a)
    bs = [[] for _ in range(n)]

    for num in a:
        bi = int(n * num)
        bs[bi].append(num)

    for b in bs:
        insertionSort(b)
    
    index = 0
    for b in bs:
        for num in b:
            a[index] = num
            index += 1
a = [0.9, 0.3, 0.2, 0.5]
print(a)
bucketSort(a)
print(a)