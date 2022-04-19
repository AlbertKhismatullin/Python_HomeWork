# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

from random import randint

N = 1
x = [randint(0, 1) for i in range(N)]
y = [randint(0, 1) for i in range(N)]
z = [randint(0, 1) for i in range(N)]
print(x, y, z)

left = not (x or y or z)
right = not x and not y and not z
truth = left == right
print (truth)