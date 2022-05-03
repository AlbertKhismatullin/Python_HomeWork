# Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
# Используя дополнительные библиотеки*


print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
discr = b ** 2 - 4 * a * c
print(f"Дискриминант D = {round(discr,2)}")
 
if discr > 0:
    x1 = (-b + (discr**0.5)) / (2 * a)
    x2 = (-b - (discr**0.5)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")