# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))

def get_fibonacci(n):
    fib = []
    a, b = 1, 1
    for i in range(n-1):
        fib.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fib.insert(0, a)
        a, b = b, a - b
    return fib

fib = get_fibonacci(n)
print(get_fibonacci(n))