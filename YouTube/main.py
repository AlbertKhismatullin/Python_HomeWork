from pytube import YouTube
from tkinter import *
from tkinter import messagebox

def clicked():  
    global txt1, txt2, txt3
    link = txt1.get()
    path = txt2.get()
    nm = txt3.get()
    nm+='.mp4'

    try:
        yt_obj = YouTube(link)

        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

        filters.get_highest_resolution().download(output_path=path, filename=nm)
        messagebox.showinfo('Урра!','Видео успешно загружено')
    except Exception as e:
        print(e)


window = Tk()
window.title("Скачивание видео с YouTube")
window.geometry('900x500')  
lbl1 = Label(window, text="Укажите адрес сайта: ", font=("Verdana", 15))  
lbl1.grid(column=0, row=0)
txt1 = Entry(window,width=80)  
txt1.grid(column=1, row=0)  
lbl2 = Label(window, text="Укажите путь для сохранения: ", font=("Verdana", 15))  
lbl2.grid(column=0, row=1)
txt2 = Entry(window,width=80)  
txt2.grid(column=1, row=1) 
lbl3 = Label(window, text="Укажите имя файла: ", font=("Verdana", 15))  
lbl3.grid(column=0, row=2)
txt3 = Entry(window,width=80)  
txt3.grid(column=1, row=2) 
btn = Button(window, text="Скачать!", bg="grey", fg="white", command=clicked)
btn.grid(column=0, row=3)
window.mainloop()

