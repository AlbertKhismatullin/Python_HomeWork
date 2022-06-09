def keeper_dt(matr, f):
    if f == 1:
        with open(r'C:\Users\alber\Desktop\Python_HomeWork\PhoneBook\DataBase\Data.txt','a') as dt:
            for i in range(len(matr)):
                for item in matr[i]:
                    dt.write(item)
                    dt.write(' ')
                dt.write(';')
                dt.write('\n')
    elif f == 2:
        with open(r'C:\Users\alber\Desktop\Python_HomeWork\PhoneBook\DataBase\Data.csv','a') as dt:
            for i in range(len(matr)):
                for item in matr[i]:
                    dt.write(item)
                    dt.write('\n')
                dt.write(' ')
                dt.write('\n')