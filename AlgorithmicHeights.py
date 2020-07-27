# Fibonacci Numbers
def fibo(n):
    if n == 0:
        return 0
    array = [0, 1]
    for i in range(2, n+1):
        array.append(array[i-1] + array[i-2])
    return array[n]

# Binary Search


file = open("path-to-a-file", "r")
msg = file.read().splitlines()
msg[0], msg[1] = int(msg[0]), int(msg[1])
msg[2], msg[3] = list(map(int, msg[2].split())), list(map(int, msg[3].split()))


def bsearch(Arr, low, high, el):
    if high >= low:
        mid = (high+low)//2
        if Arr[mid] == el:
            return mid
        elif Arr[mid] > el:
            return bsearch(Arr, low, mid-1, el)
        else:
            return bsearch(Arr, mid+1, high, el)
    else:
        return -1


def arrbsearch(n, m, Arrn, Arrm):
    results = []
    for i in range(m):
        results += [bsearch(Arrn, 0, len(Arrn)-1, Arrm[i])]
    results = [x if x == -1 else x + 1 for x in results]
    print (*results)


arrbsearch(msg[0], msg[1], msg[2], msg[3])

# Majority element
file = open("path-to-a-file", "r")
msg = file.read().splitlines()
k, n = int(msg[0].split()[0]), int(msg[0].split()[1])

for i in range(1, k+1):
    line = list(map(int, msg[i].split()))
    maxelement = max(set(line), key=line.count)
    if line.count(maxelement) >= n//2:
        print(maxelement, end=" ", flush=True)
    else:
        print (-1, end = " ", flush=True)

# Insertion sort
file = open("path-to-a-file", "r")
msg = file.read().splitlines()
n = int(msg[0])
arr = list(map(int, msg[1].split()))

def insort(n, arr):
    counter = 0
    for i in range(len(arr)):
        k = i
        while k > 0 and arr[k] < arr[k-1]:
            arr[k], arr[k-1] = arr[k-1], arr[k]
            k -= 1
            counter += 1
    print(counter)


insort(n, arr)

# Merge Two Sorted Arrays
file = open("path-to-a-file", "r")
msg = file.read().splitlines()
arr1, arr2 = list(map(int, msg[1].split())), list(map(int, msg[3].split()))
n, m = int(msg[0]), int(msg[2])


def mergesorted(n, arr1, m, arr2):
    c1 = 0
    c2 = 0
    arr3 = []
    while c1 < n and c2 < m:
        if arr1[c1] <= arr2[c2]:
            arr3.append(arr1[c1])
            c1 += 1
        else:
            arr3.append(arr2[c2])
            c2 += 1
    while c1 < n:
        arr3.append(arr1[c1])
        c1 += 1
    while c2 < m:
        arr3.append(arr2[c2])
        c2 += 1
    print(*arr3)


mergesorted(n, arr1, m, arr2)
