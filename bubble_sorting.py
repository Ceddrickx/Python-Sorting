# Bubble sort default
azumi = [20, 10, 30, 50, 40]
n = len(azumi)

for i in range(n):
    for j in range(0, n - i - 1):
        if azumi[j] > azumi[j + 1]:
            temp = azumi[j]
            azumi[j] = azumi[j + 1]
            azumi[j + 1] = temp
print(azumi)

# Bubble sort w func
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

azumi1 = [200, 100, 300, 500, 400]
result = bubble_sort(azumi1)
print(result)

# Bubble sort w input
def bubble_sort1(arr1):
    n1 = len(arr1)
    for i in range(n1):
        for j in range(0, n1 - i - 1):
            if arr1[j] > arr1[j + 1]:
                arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
    return arr1

azumi2 = []
n1 = int(input('How much numbers:'))

for i in range(n1):
    num = int(input('Enter numbers:'))
    azumi2.append(num)

result1 = bubble_sort1(azumi2)
print(result1)

# Bubble adv
arr  = list(map(int, input('Provide Numbers: ').split()))
n = len(arr)

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print(arr)
