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
