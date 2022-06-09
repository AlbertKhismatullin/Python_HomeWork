def search_surname():
    a = input('Введите фамилию: ')
    return a

def search_result(matrx):
    if matrx ==[]: print('По Вашему запросу ничего не найдено')
    else: print('Результаты поиска: ')
    for item in matrx:
        print(item)