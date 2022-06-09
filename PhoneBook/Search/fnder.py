def srch_srnm(srnm):
    res = []
    with open(r'C:\Users\alber\Desktop\Python_HomeWork\PhoneBook\DataBase\Data.txt','r') as dt:
        body = dt.readlines()
        if srnm == '':
            for line in body:
                a = line.split(';')
                res.append(a[0])        
        else:
            for line in body:
                if srnm in line:
                    a = line.split(';')
                    res.append(a[0])
    with open(r'C:\Users\alber\Desktop\Python_HomeWork\PhoneBook\DataBase\Data.csv','r') as dt:
        
        if srnm == '':
            body = dt.read()
            body1 = body.split('\n \n')
            for item in body1:
                item = item.replace('\n',' ')
                res.append(item)     
        else:
            a=''
            body = dt.readlines()
            for i in range(len(body)):
                if srnm in body[i]:
                    a+=body[i].split('\n')[0]+' '+body[i+1].split('\n')[0]+' '+body[i+2].split('\n')[0]+' '+body[i+3].split('\n')[0]
                    res.append(a)
                    a=''

    return res


