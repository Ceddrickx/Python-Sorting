# Insertion sort default
azumi = [4, 1, 3, 2, 5]
n = len(azumi)

for i in range(1, n):
    key = azumi[i]
    while azumi[i - 1] > key and i > 0:
        azumi[i], azumi[i - 1] = azumi[i - 1], azumi[i]
        i -= 1
print(azumi)

# Insertion sort w func
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        while arr[i - 1] > key and i > 0:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr

azumi = [30, 20 ,40, 50, 10]
result = insertion_sort(azumi)
print(result)

# Insertion sort w inputs
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        while arr[i - 1] > key and i > 0:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr

azumi = []
neg = int(input('How much numbers:'))

for i in range(neg):
    num = int(input('Enter numbers:'))
    azumi.append(num)
result = insertion_sort(azumi)
print(result)
