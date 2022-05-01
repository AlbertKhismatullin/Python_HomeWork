# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

from random import uniform  #(переменная) равномерная: (a: float, b: float) -> float. 
#Получите случайное число в диапазоне [a, b) или [a, b] в зависимости от округления.
n = 5
frst = 1
last = 10
def get_real_nums (n, frst, last): #((функция) get_real_nums: (n: Любой, первый: Любой, последний: Любой) -> список[с плавающей точкой]
    return [round(uniform(frst,last), 2) for i in range(n)]

def find_diff(my_list):
    nums = [round(x - int(x), 2) for x in (my_list)]
    return max(nums) - min(nums)


my_list = get_real_nums(n, frst, last)

print (my_list)
print(find_diff(my_list))