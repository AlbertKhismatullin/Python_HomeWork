#Дано число обозначающее день недели. Вывести его название и указать является ли он выходным

weekday = ['Понедельник', 'Вторник', 'Среда', 'Чеверг', 'Пятница', 'Суббота', 'Воскресенье']
i = int(input('Введите число от 1 до 7, обозначающее день недели: '))

print (weekday[i-1])
if (i<6):
    print ('День не является выходным')
else:
    print ('День является выходным')