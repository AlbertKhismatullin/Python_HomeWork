from email import header
from currency_converter import CurrencyConverter
from tkinter import *

def exchange():
    e_eur.delete(0, END)
    e_jpy.delete(0, END)
    e_gbp.delete(0, END)
    e_eur.insert(0, '%.2f' % c.convert(e_usd.get(), 'USD', 'EUR'))
    e_jpy.insert(0, '%.2f' % c.convert(e_usd.get(), 'USD', 'JPY'))
    e_gbp.insert(0, '%.2f' % c.convert(e_usd.get(), 'USD', 'GBP'))

root = Tk()
root.title('Конвертер валют')
root.geometry('400x350+400+400')
root.resizable(width=False, height=False)
root['bg'] = 'black'
c = CurrencyConverter()

header_frame = Frame(root)
header_frame.pack(fill=X)

header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

h_currency = Label(header_frame, text='Валюта', bg='black', fg='lime', font='Arial 12 bold')
h_currency.grid(row=0, column=0, sticky=EW)
h_course = Label(header_frame, text='Курс', bg='black', fg='lime', font='Arial 12 bold')
h_course.grid(row=0, column=1, columnspan=2, sticky=EW)

# EUR курс
eur_currency = Label(header_frame, text='USD', font='Arial 10')
eur_currency.grid(row=1, column=0, sticky=EW)
eur_one = Label(header_frame, text='1', font='Arial 10')
eur_one.grid(row=1, column=1, sticky=EW)
eur_converted = Label(header_frame, text='%.2f' % c.convert(1, 'EUR', 'USD'), font='Arial 10')
eur_converted.grid(row=1, column=2, sticky=EW)

# JPY курс
jpy_currency = Label(header_frame, text='JPY', font='Arial 10')
jpy_currency.grid(row=2, column=0, sticky=EW)
jpy_one = Label(header_frame, text='1', font='Arial 10')
jpy_one.grid(row=2, column=1, sticky=EW)
jpy_converted = Label(header_frame, text='%.2f' % c.convert(1, 'JPY', 'USD'), font='Arial 10')
jpy_converted.grid(row=2, column=2, sticky=EW)

# GBP курс
gbp_currency = Label(header_frame, text='GBP', font='Arial 10')
gbp_currency.grid(row=3, column=0, sticky=EW)
gbp_one = Label(header_frame, text='1', font='Arial 10')
gbp_one.grid(row=3, column=1, sticky=EW)
gbp_converted = Label(header_frame, text='%.2f' % c.convert(1, 'GBP', 'USD'), font='Arial 10')
gbp_converted.grid(row=3, column=2, sticky=EW)

calc_frame = Frame(root, bg='black')
calc_frame.pack(expand=1, fill=BOTH)
calc_frame.grid_columnconfigure(1, weight=1)

# USD
l_usd = Label(calc_frame, text='Доллары: ', bg='black', fg='lime', font='Arial 12 bold')
l_usd.grid(row=0, column=0, padx=10)
e_usd = Entry(calc_frame, justify=CENTER, font='Arial 10')
e_usd.grid(row=0, column=1, columnspan=2, pady=10, padx=10, sticky=EW)

btn_calc = Button(calc_frame, text='Конвертировать', command=exchange)
btn_calc.grid(row=1, column=1, columnspan=2, sticky=EW, padx=10)

res_frame = Frame(root)
res_frame.pack(expand=1, fill=BOTH, pady=5)
res_frame.grid_columnconfigure(1, weight=1)

# EUR
l_eur = Label(res_frame, text='EUR', font='Arial 10 bold')
l_eur.grid(row=2, column=0)
e_eur = Entry(res_frame, justify=CENTER, font='Arial 10')
e_eur.grid(row=2, column=1, columnspan=2, padx=10, sticky=EW)

# JPY
l_jpy = Label(res_frame, text='JPY', font='Arial 10 bold')
l_jpy.grid(row=3, column=0)
e_jpy = Entry(res_frame, justify=CENTER, font='Arial 10')
e_jpy.grid(row=3, column=1, columnspan=2, padx=10, sticky=EW)

# GBP
l_gbp = Label(res_frame, text='GBP', font='Arial 10 bold')
l_gbp.grid(row=4, column=0)
e_gbp = Entry(res_frame, justify=CENTER, font='Arial 10')
e_gbp.grid(row=4, column=1, columnspan=2, padx=10, sticky=EW)

root.mainloop()

# Минус данного конвертера в том, что он конвертирует валюты с опозданием