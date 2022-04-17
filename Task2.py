# Найти максимальное из пяти чисел

from random import randint


N = 5
numbers = [randint(1, 100) for i in range(N)]

max = numbers[0]

for i in range(N):
    if numbers[i] > max:
        max = numbers[i]
print(numbers)
print("Максимальное число из пяти: ", max)