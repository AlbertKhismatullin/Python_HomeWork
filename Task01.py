#По двум заданным числам проверить является ли одно квадратом второго

number1 = int(input("Введите первое число "))
number2 = int(input("Введите второе число "))

if (number1**2) == number2:
    print ("Второе число является квадратом первого")
elif (number2**2) == number1:
    print ("Первое число является квадратом второго")
else:
    print ("Числа не являются квадратами друг друга")