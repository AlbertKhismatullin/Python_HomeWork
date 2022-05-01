# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from math import ceil, prod


my_list = [2, 3, 4, 5, 6]

for i in range(ceil(len(my_list)/2)): 
    print(my_list[i] * my_list[-i - 1])
    # ceil - Метод ceil(x) в Python возвращает значение потолка x, т.е. наименьшее целое число, 
    # большее или равное x
    