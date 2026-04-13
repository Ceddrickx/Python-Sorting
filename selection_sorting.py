# Selection sort default
azumi = [40, 50, 10, 30 ,20]
n = len(azumi)

for i in range(n):
    min_value = i
    for j in range(i + 1, n):
        if azumi[j] < azumi[min_value]:
            min_value = j
    temp = azumi[i]
    azumi[i] = azumi[min_value]
    azumi[min_value] = temp

print(azumi)

# Selection sort w func
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_value = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_value]:
                min_value = j
        arr[i], arr[min_value] = arr[min_value], arr[i]
    return arr

azumi = [500, 300, 400, 200, 100]
result = selection_sort(azumi)
print(result)

# Selection sort w input
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_value = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_value]:
                min_value = j
        arr[i], arr[min_value] = arr[min_value], arr[i]
    return arr

azumi = []
neg = int(input('How much numbers:'))

for i in range(neg):
    num = int(input('Enter your numbers:'))
    azumi.append(num)

result = selection_sort(azumi)
print (result)

# Selection adv
numbers = list(map(int, input('Numbers: ').split()))
n = len(numbers)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print(numbers)
