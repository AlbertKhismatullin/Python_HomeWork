#Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов

def get_kef(my_str):
    kef_1 = 0
    kef_2 = 0
    kef_3 = 0
    
    kef_3 = int(my_str.split(' ')[-1])
    if my_str.split(' ')[-2] == '-':
        kef_3 *= -1
    space_raz = my_str.split(' ')
    
    kef_2 = int(space_raz[2].split('x')[0])
    if my_str.split(' ')[1] == '-':
        kef_2 *= -1
    
    kef_1 = int(my_str.split('x')[0])
    return kef_1, kef_2, kef_3

data1 = open(r'C:\Users\Альберт и Юлия\Desktop\Python\Python_HomeWork\Task34\polynomial1.txt','r')
data2 = open(r'C:\Users\Альберт и Юлия\Desktop\Python\Python_HomeWork\Task34\polynomial2.txt','r')

a = get_kef(data1.read())
b = get_kef(data2.read())

data1.close()
data2.close()

summ = []
for i in range(3):
    summ.append(a[i] + b[i])

data3 = open(r'C:\Users\Альберт и Юлия\Desktop\Python\Python_HomeWork\Task34\polynomial3.txt','w')

for i in range(1,3):
    if summ[i] > 0:
        summ[i] = '+' + str(summ[i])
data3.writelines(f'{summ[i]}x**2 {summ[1]}x {summ[2]} ')