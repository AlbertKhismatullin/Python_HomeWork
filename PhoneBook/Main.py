
import Controller as C

while True:
    print('===========================================')
    print('Выберите режим работы со справочником')
    print('1 - Создание новой записи')
    print('2 - Поиск по фамилии')
    print('3 - Вывести на экран все записи')
    k = int(input())
    if k ==1: C.add_db()
    elif k ==2: C.srch_smbd(k)
    elif k ==3: C.srch_smbd(k)
    else: print('Введите 1, 2 или 3')
