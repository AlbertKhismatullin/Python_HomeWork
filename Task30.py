	#Вычислить число π c заданной точностью d

from math import acos

d = int(input('C какой точностью вы хотите вычислить число π (количество цифр после запятой)? '))

def printValueOfPi():
    pi = round(2 * acos(0.0), d)
    print(pi)
if __name__ == "__main__" :
    printValueOfPi()