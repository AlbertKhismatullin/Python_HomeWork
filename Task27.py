# Строка содержит набор чисел. Показать большее и меньшее число. Символ-разделитель - пробел

def String_Min_and_Max(str):
    list1 = str.split(' ')
    min = int(list1[0])
    max = int(list1[0])
    for i in range(len(list1)):
        list1[i] = int(list1[i])
        if list1[i] < min:
            min = list1[i]
        if list1[i] > max:
            max = list1[i]
    return min, max

a = input('Введите строку, состоящую из набора чисел. В качестве символа-разделителя используйте пробел ')
print(String_Min_and_Max(a))