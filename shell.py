def shellSort(a, n):
    gap = n//2

    while gap > 0:
        j = gap

        while j < n:
            i = j - gap

            while i >= 0:
                if a[i + gap] > a[i]:
                    break
                else:
                    a[i + gap], a[i] = a[i], a[i + gap]
                i = i-gap

            j += 1
        gap = gap//2

a = [9, 3, 2, 5]
n = len(a)
print(a)
shellSort(a, n)
print(a)