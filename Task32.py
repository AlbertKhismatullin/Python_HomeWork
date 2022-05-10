#Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
import numbers

numbers = [1, 2, 3, 5, 1, 5, 3, 10] 

# def get_unique_numbers(numbers):
#     list_of_unique_numbers = [] #пустой список, который будет включать все уникальные числа
#     unique_numbers = set(numbers) #используется set для получения уникальных чисел из списка numbers

#     for number in unique_numbers: #В итоге имеется перечень из уникальных чисел. Осталось сделать из него список. 
#                                   #Для этого можно использовать цикл, перебирая каждый из элементов.
#         list_of_unique_numbers.append(number) #На каждой итерации текущее число добавляется в список

#     return list_of_unique_numbers #именно этот список возвращается в конце программы.

# print(get_unique_numbers(numbers))

#короткий вариант кода с set:
unique_numbers = list(set(numbers))
print(unique_numbers)