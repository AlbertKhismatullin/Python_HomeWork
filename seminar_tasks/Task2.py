# Найти максимальное из пяти чисел

from random import randint


N = 5 #количество чисел, из которых находится максимальное

numbers = [randint(1, 100) for i in range(N)] #рандомный выбор пяти чисел в диапазоне от 0 до 100 

max = numbers[0]

for i in range(N):
    if numbers[i] > max:
        max = numbers[i]
print(numbers)
print("Максимальное число из пяти: ", max)