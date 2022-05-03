#Составить список простых множителей натурального числа N

import math
def primefactors(n): #отвечает за печать составного числа.
   #четное число, 
   while n % 2 == 0:
      print (2),
      n = n / 2  #n стало нечетным
   for i in range(3,int(math.sqrt(n))+1,2):
      while (n % i == 0):
         print (i)
         n = n / i
   if n > 2:
      print (n)
n = int(input("Введите натуральное число :\n"))
primefactors(n)