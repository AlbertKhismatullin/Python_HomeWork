# Считайте два числа из файла (одно число в одной строке). Напишите программу, которая найдёт НОК 
# (наименьшее общее кратное) этих двух чисел.

import math
list1=[]
with open(r'C:\Users\Альберт и Юлия\Desktop\Python\Python_HomeWork\Task29\Numbrs.txt', 'r') as data:
    for item in data:
        list1.append(item)
    for i in range(len(list1)):
        list1[i] = int(list1[i])
    print(math.lcm(list1[0], list1[1]))