import datetime as dt

def log_data(st):
    with open(r'E:\GeekEducation\Python\Python Tasks\Calc\DataBase\Data.txt','a') as dat:
        dat.write(str(dt.datetime.now().strftime('%D: %H:%M')))
        dat.write(' ')
        dat.write(st)
        dat.write('\n')
