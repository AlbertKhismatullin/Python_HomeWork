#В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

with open(r'C:\Users\Альберт и Юлия\Desktop\Python\Python_HomeWork\Task35\file35.txt','r') as f:
    #stringF=list(map(int,f.readline().split()))
    stringF=[int(i) for i in f.readline().split()]
print (f' string =', stringF)
for i in range(1,len(stringF)):
    if (stringF[i]-stringF[i-1]>1):
        print(f'отсутствует элемент {stringF[i]-1}')