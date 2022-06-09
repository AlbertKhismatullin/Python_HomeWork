def new_entry():
    print('Создание новой записи справочника')
    f = 'д'
    b=[]
    while f == 'д':
        srnm = input('Фамилия: ')
        while srnm == "":
            srnm = input('Поле "Фамилия" должно быть заполнено: ')
        nm = input('Имя: ')
        while nm == "":
            nm = input('Поле "Имя" должно быть заполнено: ')
        tl = input('Телефон: ')
        while tl == "":
            tl = input('Поле "Телефон" должно быть заполнено: ')
        pr = input('Примечание: ')
        while pr == "":
            pr = input('Поле "Примечание" должно быть заполнено: ')
        a=(srnm,nm,tl,pr)
        b.append(a)
        f=input('Желаете ввести еще данные? д/н ')
    return b