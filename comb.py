def combSort(a):
    n = len(a)
    gap = n
    swapped = True

    while gap > 1 or swapped:
        gap = int(gap//1.3)

        if gap < 1:
            gap = 1
        
        swapped = False

        for i in range(n - gap):

            if a[i] > a[i+gap]:
                a[i],a[i+gap] = a[i+gap],a[i]
                swapped = True
        
a = [9, 3, 2, 5]
print(a)
combSort(a)
print(a)
