#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

decimal  = 35
 
binary = ''
 
while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal = decimal // 2
 
print(binary)