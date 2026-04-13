print('==========Enter Number==========')
numbers = list(map(int, input('Numbers: ').split()))
print('==========Choose Sort==========')
print('A. Bubble Sort')
print('B. Selection Sort')
print('C. Insertion Sort')
choice = str(input('Choice: '))

if choice == 'A':
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    print(numbers)

elif choice == 'B':
    n = len(numbers)
    for i in range(n):
        mid_index = i

        for j in range(i + 1, n):
            if numbers[j] < numbers[mid_index]:
                mid_index = j
        numbers[i], numbers[mid_index] = numbers[mid_index], numbers[i]
    print(numbers)

elif choice == 'C':
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j+1] = numbers[j]
            j -= 1

        numbers [j+1] = key
    print(numbers)

else:
    print('invalid input!')
