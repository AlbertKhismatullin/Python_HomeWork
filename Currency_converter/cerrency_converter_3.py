import requests
from tkinter import *


def Erase_All():
    amount_curr1.delete(0,END)
    lbl5.configure(text = '')

def Curr_Conv():
    
    currency1 = var1.get()
    currency2 = var2.get()

    api_key = "JP6GXHCUUXS9PRES"

    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

    main_url = base_url + "&from_currency=" + currency1 + "&to_currency=" + currency2 + "&apikey=" + api_key

    req_ob = requests.get(main_url)

    result = req_ob.json()
    
    Exchange_Rate = float(result['Realtime Currency Exchange Rate']['5. Exchange Rate'])

    n = float (amount_curr1.get())
    m = round (n * Exchange_Rate, 3 )
    txt = str (m)
    lbl5.configure(text = txt)


wnd = Tk()
wnd.title('Конвертер валют')
wnd.geometry('800x400')

hdlbl = Label(wnd, text = 'Добро пожаловать в Конвертер Валют!', font = ('Verdana',18))
hdlbl.grid(column = 0, row = 0)

dummy1 = Label(wnd)
dummy1.grid(row = 1, column = 0)

var1 = StringVar(wnd)
var2 = StringVar(wnd)
var1. set ( "Выберите валюту" )
var2. set ( "Выберите валюту" )

Curr_list = [ 'RUB' , 'USD' , 'EUR', 'JPY', 'AUD', 'CAD', 'CHF','GBP', 'KZT' ]


lbl1 = Label(wnd, text='Исходная валюта:', font=("Verdana", 13))  
lbl1.grid(column=0, row=2)
Curr1 = OptionMenu(wnd, var1, *Curr_list)
Curr1.grid(row = 2 , column = 1 , ipadx = 10 )

dummy2 = Label(wnd)
dummy2.grid(row = 3, column = 0)

lbl2 = Label(wnd, text='Конечная валюта:', font=("Verdana", 13))  
lbl2.grid(column=0, row=4)
Curr2 = OptionMenu(wnd, var2, *Curr_list)
Curr2.grid(row = 4 , column = 1 , ipadx = 10 )

dummy3 = Label(wnd)
dummy3.grid(row = 5, column = 0)

lbl3 = Label(wnd, text='Количество единиц исходной валюты:', font=("Verdana", 13))  
lbl3.grid(column=0, row=6)
amount_curr1 = Entry(wnd)
amount_curr1.grid(row = 6, column = 1)

dummy4 = Label(wnd)
dummy4.grid(row = 7, column = 0)

btn1 = Button(wnd, text = 'Конвертировать!', width = '30', height = '2', bg = 'light green', command = Curr_Conv)
btn1.grid(row = 8, column = 1)

dummy5 = Label(wnd)
dummy5.grid(row = 9, column = 0)

lbl4 = Label(wnd, text='Результат конвертации:', font=("Verdana", 13))  
lbl4.grid(column=0, row=10)

lbl5 = Label(wnd, font=("Verdana", 13))  
lbl5.grid(column=1, row=10)

dummy6 = Label(wnd)
dummy6.grid(row = 11, column = 0)

btn2 = Button(wnd, text = 'Очистить', width = '30', height = '2', bg = 'light blue', command = Erase_All)
btn2.grid(row = 12, column = 1)

wnd.mainloop()
