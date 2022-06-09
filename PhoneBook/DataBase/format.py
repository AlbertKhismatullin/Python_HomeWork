def choose_format():
    print('Выберите формат хранения записей:')
    print('1 - txt')
    print('2 - csv')
    frm = int(input())
    while frm not in (1,2):
        print('Введите 1 или 2')
        frm = int(input())
    return frm